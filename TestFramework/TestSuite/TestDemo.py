#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from TestFramework.TestEngine.PUnittest import PUnittest
from TestFramework.TestEngine.DDT import ddt
from Utils.Logger import logger


@ddt
class TestDemo01(PUnittest):

    def test_articles_title(self, param1, param2):
        logger.info("param1: {}".format(param1))
        logger.info("param2: {}".format(param2))
        self.assertEqual(param1, "param")
        self.assertEqual(param2, "param")

    def test02(self):
        self.assertEqual(1, 2)


@ddt
class TestDemo02(PUnittest):

    def test_training_title(self):
        [].index(2)
        self.assertTrue(1 != 2)

    def test_articles_title(self):
        self.assertEqual(1, 2)
        self.assertEqual(2, 3)
        self.assertEqual(1, 1)
