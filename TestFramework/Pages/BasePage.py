#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Lib.WebDriver.Browser import Browser
from Lib.WebDriver.Element import Element
from Lib.WebDriver.Wait import Wait
# from Lib.WebDriver.Actions import KeyActions, MouseActions
from TestFramework.TestEngine.ElementLocator import ParseLocator
import inspect


class BasePage:
    """POM中所有页面类的基类"""

    def __init__(self, driver):
        self.driver = driver
        self.browser = Browser(self.driver)
        self.wait = Wait(self.driver)
        # self.key_actions = KeyActions(self.driver)
        # self.mouse_actions = MouseActions(self.driver)

    def _define_element(self, get_locator=False):
        element_path = '{0}.{1}'.format(self.__class__.__name__, inspect.stack()[1][3])
        parse_locator = ParseLocator()
        locator = parse_locator.get_locator(element_path)
        if get_locator:
            return locator
        else:
            return Element(self.driver, element_path, locator)


if __name__ == '__main__':
    pass
