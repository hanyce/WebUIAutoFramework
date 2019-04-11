# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from TestFramework.TestEngine.PUnittest import PUnittest
from TestFramework.TestEngine.DDT import ddt
from Utils.Logger import logger


@ddt
class TestDDT(PUnittest):

    def test_ddt(self, condition, username, password):
        """测试登录"""
        logger.info("username: {}".format(username))
        logger.info("password: {}".format(password))
        self.assertTrue(condition)
        self.assertTrue(username)
        self.assertTrue(password)


if __name__ == '__main__':
    pass
