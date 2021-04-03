import pytest
from selenium import webdriver
from data import common_data
from page.index_page import IndexPage
from page.login_page import LoginPage

driver = None


# 声明这个函数是fixture
@pytest.fixture(scope="class")
def access_web():
    # 前置
    global driver
    driver = webdriver.Chrome(common_data.driver)
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    driver.get("http://localhost:7070/login?from=%2F")
    driver.maximize_window()
    yield driver, login_page, index_page
    driver.close()


@pytest.fixture()
def refresh_page():
    global driver
    yield
    driver.refresh()
