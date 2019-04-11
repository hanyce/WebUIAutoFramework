#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Lib.WebDriver.BrowserEngine import ENGINE
from TestFramework.Pages.BasePage import BasePage
from TestFramework.Pages.HomePage import HomePage
from TestFramework.Pages.NavigateBar import NavigateBar

driver = ENGINE.get_driver()
homePage = HomePage(driver)
navigateBar = NavigateBar(driver)


class LoginPage(BasePage):

    def username_textbox(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def username_empty_prompt(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def password_textbox(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def password_empty_prompt(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def access_account_button(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def wrong_credential_label(self, get_locator=False):
        return self._define_element(get_locator=get_locator)

    def LoginWebsite(self, username, password):
        """
        登录网站
        :param username: 用户名
        :param password: 密码
        :return: 二元组，login_status代表登录状态，result代表验证状态
        """
        self.username_textbox().clear()
        self.username_textbox().send_keys(username)
        self.password_textbox().clear()
        self.password_textbox().send_keys(password)
        self.access_account_button().click()
        if homePage.expand_navigate_button().is_displayed():
            homePage.ExpandNavigateBar()
            assert_result = True
            login_status = True
        elif self.username_empty_prompt().is_displayed():
            assert_result = True
            login_status = False
        elif self.password_empty_prompt().is_displayed():
            assert_result = True
            login_status = False
        elif self.wrong_credential_label().is_displayed():
            assert_result = True
            login_status = False
        else:
            assert_result = False
            login_status = False
        return login_status, assert_result


if __name__ == '__main__':
    pass
