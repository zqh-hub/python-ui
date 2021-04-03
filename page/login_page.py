from locate.login_locate import LoginLocate as loc
from common.base_page import BasePage


class LoginPage(BasePage):
    def submit_login(self, username, password):
        self.ele_input_key(loc.username_input, username)
        self.ele_input_key(loc.password_input, password)
        self.click_ele(loc.submit_but)

    def def_get_username_password_error_alert_text(self):
        return self.get_text(loc.username_password_error_alert)
