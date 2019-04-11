#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Logger import logger
from Utils.ParseConfig import TEST_SET_SOURCE
from Utils.Paths import TEST_CASE_FILE_PATH
from Utils.ParseExcel import ExcelParser
from importlib import import_module
import unittest
import argparse
import re


def _convert_params(params):
    """
    将测试用例中的参数由字符串转换成python数据结构
    :param params: 测试用例的参数
    :return: 参数字典，dict type
    """
    if params is None:
        return None
    else:
        param_dict = dict()
        for param in params:
            param_name = param.split('=')[0]
            param_val = ''.join(param.split('=')[1:])  # 如果有多个=，需要将第一个=后的所有内容再次拼接成字符串
            try:
                param_dict[param_name] = eval(param_val)
            except (NameError, SyntaxError):
                param_dict[param_name] = param_val
        return param_dict


def get_raw_test_set():
    """
    读取TestCases.xlsx中所有的数据，并在每一条case中加入标识符_Hidden
    :return: [dict(case), dict(case)...]形式的测试集，其中每条case dict包含一条多余的字段_Hidden表示是否是隐藏数据，
    如果有必要，在后续处理中会过滤被隐藏的case
    """
    excel = ExcelParser(TEST_CASE_FILE_PATH, 'TestCases')
    test_set = []
    titles = [x for x in excel.get_row_values(1)]
    values = []
    temp_row_hidden = False
    for row in range(2, excel.max_row + 1):
        ddt_params = False if excel.get_cell_value(row=row, column=1) else True  # 某行数据是否是ddt参数
        row_hidden = excel.worksheet.row_dimensions[row].hidden  # 获取该行是否被隐藏
        if ddt_params:
            test_case = {"_Hidden": temp_row_hidden}
            # 如果该行是ddt参数，取上一行的其他数据和该行的参数组成用例
            _values = list(filter(lambda x: x is not None, [x for x in excel.get_row_values(row)]))
            values = values[:len(values)-len(_values)] + _values
        else:
            test_case = {"_Hidden": row_hidden}
            values = [x for x in excel.get_row_values(row)]
            temp_row_hidden = row_hidden  # 记录非ddt参数行的隐藏状况
        if len(values) < len(titles):
            for i in range(len(titles) - len(values)):
                values.append(None)
        for idx, (title, value) in enumerate(zip(titles, values)):
            if title != 'CaseParameters':
                test_case[title] = value
            else:
                params = values[idx:] if values[idx] is not None else None
                new_params = _convert_params(params)
                test_case[title] = new_params
        test_set.append(test_case)
    return test_set


def filter_test_case(test_set, **titles):
    """
    根据测试用例的title过滤测试用例
    :param test_set: 测试集
    :param titles: 关键字参数，每个参数名对应表格中的title
    :return: [dict(case), dict(case)...]形式的测试集
    """
    if titles:
        for title, value in titles.items():
            test_set = list(filter(lambda d: title in d.keys(), test_set))
            test_set = list(filter(lambda d: d[title] == value, test_set))
    return test_set


def test_set_from_excel(filter_hidden=True):
    """
    根据TestCases.xlsx的过滤情况生成可用的测试集
    :param filter_hidden: 是否过滤TestCases.xlsx中被隐藏的测试用例
    :return: 过滤后的测试集
    """
    test_set = get_raw_test_set()
    if filter_hidden:
        test_set = filter_test_case(test_set, _Hidden=False)
    for idx, test_case in enumerate(test_set):
        _test_case = {k: v for k, v in test_case.items() if k != "_Hidden"}
        test_set[idx] = _test_case
    return test_set


def test_set_from_cmd():
    """
    从命令行获取测试集的过滤条件，并生成新的测试集
    :return: [dict(case), dict(case)...]形式的测试集
    """
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Organize Test Suite')

    parser.add_argument(dest='args', metavar='args', nargs='*')
    parser.add_argument('-f', '--test_file_name', metavar='TestFileName',
                        dest='file_name', action='append',
                        help='Indicate test file name')
    parser.add_argument('-cl', '--test_class_name', metavar='TestClassName',
                        dest='class_name', action='append',
                        help='Indicate test class name')
    parser.add_argument('-ca', '--test_case_name', metavar='TestCaseName',
                        dest='case_name', action='append',
                        help='Indicate test case name')
    parser.add_argument('-p', '--test_case_priority', metavar='TestCasePriority',
                        dest='priority', action='store',
                        help='Indicate test case priority')
    args = parser.parse_args()
    test_file = args.file_name
    test_class = args.class_name
    test_case = args.case_name
    priority = args.priority

    test_set = get_raw_test_set()
    for idx, case in enumerate(test_set):
        _case = {k: v for k, v in case.items() if k != "_Hidden"}
        test_set[idx] = _case
    if test_file:
        test_set = list(filter(lambda d: d["TestFile"] in test_file, test_set))
    if test_class:
        test_set = list(filter(lambda d: d["TestClass"] in test_class, test_set))
    if test_case:
        test_set = list(filter(lambda d: d["TestCase"] in test_case, test_set))
    if priority:
        test_set = filter_test_case(test_set, Priority=priority)
    return test_set


def get_test_set():
    """
    根据测试集的数据源生成相应的测试集
    :return: [dict(case), dict(case)...]形式的测试集
    """
    if TEST_SET_SOURCE == "ExcelTable":
        test_set = test_set_from_excel()
    elif TEST_SET_SOURCE == "CmdLineArgs":
        test_set = test_set_from_cmd()
    else:
        test_set = test_set_from_excel(filter_hidden=False)
    return test_set


TEST_SET = get_test_set()


def make_test_suite():
    """
    利用测试集生成PUnittest能识别的TestSuite对象
    :return: TestSuite对象
    """
    test_suite = unittest.TestSuite()

    # 将原始的测试集做处理，去除CaseParameters字段后再去重，获取真实的测试集，
    # 这样可以排除DDT参数导致测试集膨胀的问题，DDT模块里会根据该真实测试集和DDT参数，
    # 重新生成新的测试套件TestSuite
    test_set = []
    for test_case in TEST_SET:
        # 新生成一份用例字典而不是对原始用例字典进行修改是为了保证TEST_SET的常量属性
        _test_case = {k: v for k, v in test_case.items() if k != "CaseParameters"}
        if _test_case not in test_set:
            test_set.append(_test_case)

    if len(test_set) > 0:
        for test_case in test_set:
            _dir_name = test_case['TestDir'] if 'TestDir' in test_case else None
            _file_name = test_case['TestFile'] if 'TestFile' in test_case else None
            _cls_name = test_case['TestClass'] if 'TestClass' in test_case else None
            _case_name = test_case['TestCase'] if 'TestCase' in test_case else None
            try:
                package = import_module('TestFramework.{0}.{1}'.format(_dir_name, _file_name))  # 加载测试模块，间接加载DDT模块
                cls = getattr(package, _cls_name)   # 加载测试类
                for name, func in list(cls.__dict__.items()):   # 遍历测试类中的测试方法（测试用例）
                    _name = re.sub(r'_#.*', '', name)   # 将DDT改变后的测试方法名称改成原始测试方法名称
                    if _name == _case_name:  # 如果测试方法名称符合测试集中的名称
                        case = cls(name)    # 获取测试套件中测试用例对象
                        test_suite.addTest(case)    # 将测试用例对象加入测试套件
            except Exception as e:
                logger.warning('Fail to load test case <{0}><{1}><{2}>: {3}'.format(_file_name, _cls_name, _case_name, e))
    else:
        logger.error('Fail to load any test case, please check')
    return test_suite


if __name__ == '__main__':
    test_suite = make_test_suite()
    print(test_suite)
