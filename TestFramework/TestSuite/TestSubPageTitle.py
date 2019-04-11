#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from TestFramework.Pages.NavigateBar import NavigateBar
from TestFramework.Pages.HomePage import HomePage
from TestFramework.TestEngine.PUnittest import PUnittest
from TestFramework.TestEngine.DDT import ddt
from Lib.WebDriver.BrowserEngine import ENGINE
import unittest
import time


@ddt
class TestSubPageTitle(PUnittest):

    driver = ENGINE.get_driver()
    homePage = HomePage(driver)
    navigateBar = NavigateBar(driver)

    @classmethod
    def setUpClass(cls):
        super(TestSubPageTitle, cls).setUpClass()
        cls.homePage.browser.navigate_to('https://www.utest.com/')

    def test_articles_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.articles_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Articles')

    def test_training_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.training_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Courses')

    def test_forums_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.forums_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'xxxxxxxxxxxxxxxx')

    def test_tools_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.tools_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'Software Testing Tool Reviews')

    def test_projects_title(self):
        navigate_bar_visible = self.navigateBar.navigate_bar().is_displayed()
        if not navigate_bar_visible:
            self.homePage.expand_navigate_button().click()
        self.navigateBar.projects_button().click()
        time.sleep(2)
        title_label_text = self.homePage.title_label().get_text()
        self.assertEqual(title_label_text, 'xxxxxxxxxxxxxxxxxxx')


if __name__ == '__main__':
    unittest.main()
