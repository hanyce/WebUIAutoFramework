#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Paths import LAST_LOGS_DIR
from Utils.ParseConfig import CONSOLE_LOG_SWITCH, CONSOLE_LOG_LEVEL, FILE_LOG_SWITCH, FILE_LOG_LEVEL
from logging.handlers import TimedRotatingFileHandler
import logging
import time
import os


class Logger:
    def __init__(self, logger_name=__name__):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.formatter = logging.Formatter('[%(asctime)s][%(levelname)s]: %(message)s')
        self.console_output_level = CONSOLE_LOG_LEVEL
        self.file_output_level = FILE_LOG_LEVEL
        self.backup_count = 20

    def get_logger(self, console_switch=CONSOLE_LOG_SWITCH, file_switch=FILE_LOG_SWITCH):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:
            if console_switch:
                console_handler = logging.StreamHandler()
                console_handler.setLevel(self.console_output_level)
                console_handler.setFormatter(self.formatter)
                self.logger.addHandler(console_handler)
            if file_switch:
                now_time = time.strftime("%Y-%m-%d_%H-%M-%S")
                self.log_file_name = '{0}.log'.format(now_time)
                if not os.path.exists(LAST_LOGS_DIR):
                    os.makedirs(LAST_LOGS_DIR)
                self.log_file_path = os.path.join(LAST_LOGS_DIR, self.log_file_name)
                file_handler = TimedRotatingFileHandler(filename=self.log_file_path, when='D', interval=1,
                                                        backupCount=self.backup_count, delay=True, encoding='utf-8')
                file_handler.setLevel(self.file_output_level)
                file_handler.setFormatter(self.formatter)
                self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()


if __name__ == '__main__':
    logger.info('hello world')
