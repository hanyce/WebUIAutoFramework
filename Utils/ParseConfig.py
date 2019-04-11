#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Paths import FRAME_CONFIG_FILE_PATH
from configparser import ConfigParser

config = ConfigParser()
config.read(FRAME_CONFIG_FILE_PATH)

# ***************************************** LogConfig *****************************************

CONSOLE_LOG_SWITCH = True if config.get('LogConfig', 'ConsoleSwitch') != "False" else False
CONSOLE_LOG_LEVEL = config.get('LogConfig', 'ConsoleLevel')
FILE_LOG_SWITCH = True if config.get('LogConfig', 'FileSwitch') != "False" else False
FILE_LOG_LEVEL = config.get('LogConfig', 'FileLevel')

# ***************************************** TimeConfig *****************************************

IMPLICITY_WAIT_TIME = float(config.get('TimeConfig', 'ImplicityWaitTime'))
WAIT_UNTIL_TIMEOUT = float(config.get('TimeConfig', 'WaitUntilTimeout'))
WAIT_UNTIL_NOT_TIMEOUT = float(config.get('TimeConfig', 'WaitUntilNotTimeout'))
WAIT_FREQUENCY = float(config.get('TimeConfig', 'WaitFrequency'))

# ************************************* TestFrameworkConfig *************************************

TEST_SET_SOURCE = config.get('TestFramework', 'TestSetSource')
EXCEPTION_SCREENSHOTS_SWITCH = True if config.get('TestFramework', 'ExceptionScreenshotSwitch') != 'False' else False
TEST_CASE_FAIL_RERUN_NUM = int(config.get('TestFramework', 'TestCaseFailRerunNum'))

# ************************************* BrowserRunnerConfig **************************************

BROWSER_NAME = config.get('BrowserRunner', 'BrowserName')
BROWSER_WINDOW_SIZE = config.get('BrowserRunner', 'BrowserWindowSize')

# **************************************** TestInfoConfig *****************************************

HTML_REPORT_SWITCH = False if config.get('TestInfo', 'HtmlReportSwitch') != 'True' else True
HTML_REPORT_TITLE = config.get('TestInfo', 'HtmlReportTitle')
HTML_REPORT_DESCRIPTION = config.get('TestInfo', 'HtmlReportDescription')
HTML_REPORT_TESTER = config.get('TestInfo', 'HtmlReportTester')

if __name__ == '__main__':
    print("CONSOLE_LOG_SWITCH", type(CONSOLE_LOG_SWITCH), CONSOLE_LOG_SWITCH)
    print("CONSOLE_LOG_LEVEL", type(CONSOLE_LOG_LEVEL), CONSOLE_LOG_LEVEL)
    print("FILE_LOG_SWITCH", type(FILE_LOG_SWITCH), FILE_LOG_SWITCH)
    print("FILE_LOG_LEVEL", type(FILE_LOG_LEVEL), FILE_LOG_LEVEL)

    print("IMPLICITY_WAIT_TIME", type(IMPLICITY_WAIT_TIME), IMPLICITY_WAIT_TIME)
    print("WAIT_UNTIL_TIMEOUT", type(WAIT_UNTIL_TIMEOUT), WAIT_UNTIL_TIMEOUT)
    print("WAIT_UNTIL_NOT_TIMEOUT", type(WAIT_UNTIL_NOT_TIMEOUT), WAIT_UNTIL_NOT_TIMEOUT)
    print("WAIT_FREQUENCY", type(WAIT_FREQUENCY), WAIT_FREQUENCY)

    print("TEST_SET_SOURCE", type(TEST_SET_SOURCE), TEST_SET_SOURCE)
    print("EXCEPTION_SCREENSHOTS_SWITCH", type(EXCEPTION_SCREENSHOTS_SWITCH), EXCEPTION_SCREENSHOTS_SWITCH)
    print("TEST_CASE_FAIL_RERUN_NUM", type(TEST_CASE_FAIL_RERUN_NUM), TEST_CASE_FAIL_RERUN_NUM)

    print("BROWSER_NAME", type(BROWSER_NAME), BROWSER_NAME)
    print("BROWSER_WINDOW_SIZE", type(BROWSER_WINDOW_SIZE), BROWSER_WINDOW_SIZE)

    print("HTML_REPORT_SWITCH", type(HTML_REPORT_SWITCH), HTML_REPORT_SWITCH)
    print("HTML_REPORT_TITLE", type(HTML_REPORT_TITLE), HTML_REPORT_TITLE)
    print("HTML_REPORT_DESCRIPTION", type(HTML_REPORT_DESCRIPTION), HTML_REPORT_DESCRIPTION)
    print("HTML_REPORT_TESTER", type(HTML_REPORT_TESTER), HTML_REPORT_TESTER)
