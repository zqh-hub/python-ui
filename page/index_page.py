from locate.index_locate import IndexLocate as loc
from common.base_page import BasePage


class IndexPage(BasePage):
    def def_get_welcome_title(self):
        return self.get_text(loc.login_user)
