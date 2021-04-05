from selenium.webdriver.common.by import By


class IndexLocate:
    login_user = (By.XPATH, "//div[contains(@class,'page-header__hyperlinks')]/a[@class]/span")
