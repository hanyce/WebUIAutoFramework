#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# ROOT DIR
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# CONFIG DIR
CONFIG_DIR = os.path.join(ROOT_DIR, "Config")
FRAME_CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, 'FrameConfig.ini')
ELEMENT_LOCATOR_FILE_PATH = os.path.join(CONFIG_DIR, 'ElementLocator.json')
TEST_CASE_FILE_PATH = os.path.join(CONFIG_DIR, 'TestCases.xlsx')

# TEST FRAMEWORK DIR
TEST_FRAMEWORK_DIR = os.path.join(ROOT_DIR, "TestFramework")

# TEST RESULTS DIR
TEST_RESULT_DIR = os.path.join(TEST_FRAMEWORK_DIR, "TestResults")
LAST_RESULT_DIR = os.path.join(TEST_RESULT_DIR, "LastResult")
LAST_LOGS_DIR = os.path.join(LAST_RESULT_DIR, "Logs")
LAST_REPORTS_DIR = os.path.join(LAST_RESULT_DIR, "Reports")
LAST_SCREENSHOTS_DIR = os.path.join(LAST_RESULT_DIR, "Screenshots")
BACKUP_RESULT_DIR = os.path.join(TEST_RESULT_DIR, "BackupResult")
# TEST SUITE DIR
TEST_SUITE_DIR = os.path.join(TEST_FRAMEWORK_DIR, "TestSuite")

# LIB DIR
LIB_DIR = os.path.join(ROOT_DIR, "Lib")
DRIVERS_DIR = os.path.join(LIB_DIR, "Drivers")
CHROME_DRIVER_PATH = os.path.join(DRIVERS_DIR, "Chrome", "chromedriver.exe")
FIREFOX_DRIVER_PATH = os.path.join(DRIVERS_DIR, "Firefox", "geckodriver.exe")
IE_DRIVER_PATH = os.path.join(DRIVERS_DIR, "IE", "IEDriverServer.exe")
SELENIUM_GRID_PATH = os.path.join(DRIVERS_DIR, "SeleniumGrid", "selenium-server-standalone-3.9.1.jar")

if __name__ == "__main__":
    print('ROOT_DIR = {0}'.format(str(os.path.exists(ROOT_DIR))))
    print('CONFIG_DIR = {0}'.format(str(os.path.exists(CONFIG_DIR))))
    print('FRAME_CONFIG_FILE_PATH = {0}'.format(str(os.path.exists(FRAME_CONFIG_FILE_PATH))))
    print('ELEMENT_LOCATOR_FILE_PATH = {0}'.format(str(os.path.exists(ELEMENT_LOCATOR_FILE_PATH))))
    print('TEST_CASE_FILE_PATH = {0}'.format(str(os.path.exists(TEST_CASE_FILE_PATH))))
    print('TEST_FRAMEWORK_DIR = {0}'.format(str(os.path.exists(TEST_FRAMEWORK_DIR))))
    print('TEST_RESULT_DIR = {0}'.format(str(os.path.exists(TEST_RESULT_DIR))))
    print('LAST_RESULT_DIR = {0}'.format(str(os.path.exists(LAST_RESULT_DIR))))
    print('LAST_LOGS_DIR = {0}'.format(str(os.path.exists(LAST_LOGS_DIR))))
    print('LAST_REPORTS_DIR = {0}'.format(str(os.path.exists(LAST_REPORTS_DIR))))
    print('LAST_SCREENSHOTS_DIR = {0}'.format(str(os.path.exists(LAST_SCREENSHOTS_DIR))))
    print('BACKUP_RESULT_DIR = {0}'.format(str(os.path.exists(BACKUP_RESULT_DIR))))
    print('TEST_SUITE_DIR = {0}'.format(str(os.path.exists(TEST_SUITE_DIR))))
    print('LIB_DIR = {0}'.format(str(os.path.exists(LIB_DIR))))
    print('DRIVERS_DIR = {0}'.format(str(os.path.exists(DRIVERS_DIR))))
    print('CHROME_DRIVER_PATH = {0}'.format(str(os.path.exists(CHROME_DRIVER_PATH))))
    print('FIREFOX_DRIVER_PATH = {0}'.format(str(os.path.exists(FIREFOX_DRIVER_PATH))))
    print('IE_DRIVER_PATH = {0}'.format(str(os.path.exists(IE_DRIVER_PATH))))
    print('SELENIUM_GRID_PATH = {0}'.format(str(os.path.exists(SELENIUM_GRID_PATH))))
