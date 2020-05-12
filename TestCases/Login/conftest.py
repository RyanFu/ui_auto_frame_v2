# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 22:53
# @Author  : chineseluo
# @Email   : 848257135@qq.com
# @File    : conftest.py
# @Software: PyCharm
import pytest
from PageObject.login_page import Login_page

@pytest.fixture(scope="module")
def login_page_class_load(session_driver):
    login_page = Login_page(session_driver)
    yield login_page
