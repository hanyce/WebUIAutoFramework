#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.ParseConfig import EXCEPTION_SCREENSHOTS_SWITCH, TEST_CASE_FAIL_RERUN_NUM
from Utils.Logger import logger
from functools import wraps
import sys


def wrapped_unittest_assertion(func):
    """用来装饰PUnittest类中所有的AssertXxx方法"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger.debug('[Assert]: {0} >> {1}'.format(func.__name__, format(args[1:])))
            return func(*args, **kwargs)
        except AssertionError as e:
            args[0].Exc_Stack.append(e)
    return wrapper


def wrapped_testcase(screenshot=EXCEPTION_SCREENSHOTS_SWITCH, rerun=TEST_CASE_FAIL_RERUN_NUM):
    """用来装饰所有的测试用例，提供失败后截图和失败后重跑功能"""
    def wrapper(func):
        @wraps(func)
        def on_call(*args, **kwargs):
            # 失败重跑次数
            if rerun is False:
                rerun_time = 1
            elif isinstance(rerun, int):
                rerun_time = rerun
            else:
                rerun_time = 3
            # _browser是获取测试用例实例的browser属性，因为跨越了xxxPage属性层，所以用到了循环
            _testcase_name = args[0]._testMethodName
            _testclass_name = args[0].__class__.__name__
            _browser = None
            for attr in dir(args[0]):
                if hasattr(getattr(args[0], attr), 'browser'):
                    _browser = getattr(getattr(args[0], attr), 'browser')
                    break
            # 循环执行测试用例
            _rerun_time = rerun_time
            while rerun_time > 0:
                try:
                    logger.info((' TestRunNo: >> {0} '.format(_rerun_time - rerun_time + 1)).center(100, '-'))
                    result = func(*args, **kwargs)
                    # 用例执行完毕抛出所有可能存在的AssertionError异常
                    args[0].raise_exc()
                    logger.info(' TestResult: '.center(100, '-'))
                    logger.info('[TestSuccess]: {0} >> {1} '.format(_testclass_name, _testcase_name))
                    return result
                except Exception:
                    if screenshot:
                        _filename = 'Error_' + _testcase_name
                        _browser.take_screenshot(_filename)
                    rerun_time -= 1
                    if rerun_time == 0:
                        exc_type, exc_msg, _ = sys.exc_info()
                        logger.info(' TestResult: '.center(100, '-'))
                        logger.error('[TestFail]: {0}: {1}'.format(exc_type.__name__, exc_msg))
                        raise
        return on_call
    return wrapper


if __name__ == '__main__':
    pass
