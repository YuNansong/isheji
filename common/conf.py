#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, sys
from selenium.webdriver.common.by import By

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'data')

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }


cm = ConfigManager()
# if __name__ == '__main__':
#     print(cm.BASE_DIR)
