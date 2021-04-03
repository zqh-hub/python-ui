from selenium.webdriver.common.by import By


class LoginLocate:
    username_input = (By.XPATH, '//*[@id="j_username"]')
    password_input = (By.XPATH, '//*[@name="j_password"]')
    submit_but = (By.XPATH, '//*[@name="Submit"]')
    username_password_error_alert = (
        By.XPATH, '//form[@action="j_spring_security_check"]/div[contains(@class,"alert-danger")]')
