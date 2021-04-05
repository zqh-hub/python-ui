from selenium.webdriver.common.by import By


class IndexLocate:
    # welcome_title = (By.XPATH, '//div[@class="empty-state-block"]/h1')
    login_user = (By.XPATH, "//div[contains(@class,'page-header__hyperlinks')]/a[@class]/span'")
