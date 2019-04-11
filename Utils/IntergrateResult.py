#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Utils.Logger import logger
from Utils.Paths import *
import time
import shutil
import os

now_date = time.strftime("%Y-%m-%d")
backup_date_dir = os.path.join(BACKUP_RESULT_DIR, now_date)
backup_logs_dir = os.path.join(backup_date_dir, "Logs")
backup_reports_dir = os.path.join(backup_date_dir, "Reports")
backup_screenshots_dir = os.path.join(backup_date_dir, "Screenshots")


def init_test_result_folders():
    logger.info("Initialize TestResult dir")
    if not os.path.exists(TEST_RESULT_DIR):
        os.mkdir(TEST_RESULT_DIR)


def init_backup_folders():
    logger.info("Initialize BackupResult and inner dirs")
    if not os.path.exists(BACKUP_RESULT_DIR):
        os.mkdir(BACKUP_RESULT_DIR)
    if not os.path.exists(backup_date_dir):
        os.mkdir(backup_date_dir)
    if not os.path.exists(backup_logs_dir):
        os.mkdir(backup_logs_dir)
    if not os.path.exists(backup_reports_dir):
        os.mkdir(backup_reports_dir)
    if not os.path.exists(backup_screenshots_dir):
        os.mkdir(backup_screenshots_dir)


def init_last_folders():
    logger.info("Initialize LastResult and inner dirs")
    if not os.path.exists(LAST_RESULT_DIR):
        os.mkdir(LAST_RESULT_DIR)
    if not os.path.exists(LAST_LOGS_DIR):
        os.mkdir(LAST_LOGS_DIR)
    if not os.path.exists(LAST_REPORTS_DIR):
        os.mkdir(LAST_REPORTS_DIR)
    if not os.path.exists(LAST_SCREENSHOTS_DIR):
        os.mkdir(LAST_SCREENSHOTS_DIR)


def backup_results(file_type, results_folder_path, target_folder_path):
    for root, dirs, files in os.walk(results_folder_path):
        for file in files:
            if file.split(".")[1] == file_type:
                file_path = os.path.join(results_folder_path, file)
                target_path = os.path.join(target_folder_path, file)
                # 如果有相同文件则覆盖
                if os.path.exists(target_path):
                    os.remove(target_path)
                shutil.copy(file_path, target_path)
    logger.info("BackupResult {0}".format(results_folder_path))
    shutil.rmtree(results_folder_path, ignore_errors=True)


def integrate_results():
    try:
        init_test_result_folders()
        init_backup_folders()
        if os.path.exists(LAST_LOGS_DIR):
            backup_results("log", LAST_LOGS_DIR, backup_logs_dir)
        if os.path.exists(LAST_REPORTS_DIR):
            backup_results("html", LAST_REPORTS_DIR, backup_reports_dir)
        if os.path.exists(LAST_SCREENSHOTS_DIR):
            backup_results("png", LAST_SCREENSHOTS_DIR, backup_screenshots_dir)
        init_last_folders()
    except Exception as e:
        logger.error("Fail to integrate former results: {0}".format(e))
        raise e


if __name__ == "__main__":
    integrate_results()
