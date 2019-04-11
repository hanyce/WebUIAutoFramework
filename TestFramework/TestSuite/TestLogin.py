#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from TestFramework.Pages.NavigateBar import NavigateBar
from TestFramework.Pages.HomePage import HomePage
from TestFramework.Pages.LoginPage import LoginPage
from TestFramework.TestEngine.PUnittest import PUnittest
from TestFramework.TestEngine.DDT import ddt
from Lib.WebDriver.BrowserEngine import ENGINE


@ddt
class TestLogin(PUnittest):
    driver = ENGINE.get_driver()
    homePage = HomePage(driver)
    navigateBar = NavigateBar(driver)
    loginPage = LoginPage(driver)

    def test_login(self, condition, username, password):
        """测试登录"""
        self.homePage.browser.navigate_to('https://www.utest.com/')
        self.homePage.sign_in_button().click()
        login_status, check_result = self.loginPage.LoginWebsite(username, password)
        self.assertTrue(check_result)
        if 'success' in condition:
            self.assertTrue(login_status)
            self.homePage.Logout()
        elif 'fail' in condition:
            self.assertFalse(login_status)


if __name__ == '__main__':
    pass
