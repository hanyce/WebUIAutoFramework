#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from TestFramework.TestEngine.TestSet import TEST_SET, filter_test_case
from functools import wraps


def mk_test_name(name, condition):
    """
    生成测试方法的新名称
    :param name: 原始名称
    :param condition: 后缀，也是测试集中DDT参数中的condition参数
    :return: 新名称
    """
    test_name = '{0}_#{1}'.format(name, condition)
    return test_name


def feed_data(func, new_name, *args, **kwargs):
    """
    装饰函数，改变原始函数的属性
    :param func: 被装饰函数
    :param new_name: 被装饰函数的新名称
    :param args: 被装饰函数的参数
    :param kwargs: 被装饰函数的参数
    :return: 装饰后的函数
    """
    @wraps(func)
    def wrapper(self):
        return func(self, *args, **kwargs)
    wrapper.__name__ = new_name
    wrapper.__wrapped__ = func
    if func.__doc__:
        try:
            wrapper.__doc__ = func.__doc__.format(*args, **kwargs)
        except (IndexError, KeyError):
            pass
    return wrapper


def add_test(cls, test_name, func, *args, **kwargs):
    """
    为测试类添加新属性（测试方法）
    :param cls: 测试类
    :param test_name: 测试方法名称
    :param func: 测试方法
    :param args: 测试方法的参数
    :param kwargs: 测试方法的参数
    :return:
    """
    setattr(cls, test_name, feed_data(func, test_name, *args, **kwargs))


def ddt(cls):
    """
    装饰测试类，解析参数并修改测试方法在测试类中的注册方式
    :param cls: 被装饰的测试类
    :return: 装饰后的测试类
    """
    for name, func in list(cls.__dict__.items()):   # 遍历测试类中的属性
        if 'test_' in name:     # 如果是测试方法
            test_dir = ".".join(cls.__module__.split(".")[1:-1])    # 获取测试模块的目录
            test_file = cls.__module__.split(".")[-1]   # 获取测试模块的名称
            # 从测试集中筛选出相应的测试用例（包括DDT参数膨胀后的同名测试用例）
            test_cases = filter_test_case(TEST_SET, TestDir=test_dir, TestFile=test_file, TestClass=cls.__name__, TestCase=name)
            for test_case in test_cases:    # 遍历测试用例
                func.__doc__ = test_case['CaseDescription']     # 将用例描述指定为测试方法的文档属性
                _ddt = test_case['DDT']
                _params = test_case['CaseParameters']
                if _ddt is True and _params is not None:    # 如果是DDT的测试用例
                    test_name = mk_test_name(name, _params["condition"])    # 将condition的value拼进测试用例名称
                    add_test(cls, test_name, func, *_params.values())
                elif _ddt is False and _params is not None:     # 如果不是DDT的测试用例并且有参数
                    test_name = mk_test_name(name, "")
                    add_test(cls, test_name, func, *_params.values())
                else:
                    test_name = mk_test_name(name, "")
                    add_test(cls, test_name, func)
            delattr(cls, name)
    return cls
