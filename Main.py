#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.ParseConfig import HTML_REPORT_SWITCH
from TestFramework.TestEngine.TestSet import make_test_suite
from TestFramework.TestEngine.TestRunner import html_test_runner, text_test_runner
from Utils.IntergrateResult import integrate_results
from Lib.WebDriver.BrowserEngine import ENGINE


def main(html_report=HTML_REPORT_SWITCH):
    integrate_results()
    # ENGINE.launch_local_browser()
    test_suite = make_test_suite()
    if html_report:
        html_test_runner(test_suite)
    else:
        text_test_runner(test_suite)
    # ENGINE.quit_browser()


if __name__ == '__main__':
    main()
