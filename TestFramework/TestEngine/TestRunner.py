#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Logger import logger
from Utils.ParseConfig import HTML_REPORT_TITLE
from Utils.ParseConfig import HTML_REPORT_DESCRIPTION, HTML_REPORT_TESTER
from Utils.Paths import LAST_REPORTS_DIR
from TestFramework.TestEngine.HTMLTestRunner import HTMLTestRunner
import unittest
import time
import os


def text_test_runner(test_suite):
    runner = unittest.TextTestRunner()
    logger.info("Start to test...\n")
    runner.run(test_suite)
    logger.info("Finish testing...")


def html_test_runner(test_suite, report_title=HTML_REPORT_TITLE, report_description=HTML_REPORT_DESCRIPTION,
                     tester=HTML_REPORT_TESTER):
    now_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_name = "{0}_HtmlTestReport.html".format(now_time)
    full_report_name = os.path.join(LAST_REPORTS_DIR, report_name)
    with open(full_report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title=report_title, description=report_description, tester=tester)
        logger.info("Start to test...\n")
        runner.run(test_suite)
        logger.info("Finish testing...")
