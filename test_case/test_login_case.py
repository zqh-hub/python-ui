import pytest
from data import login_data


@pytest.mark.usefixtures("access_web")
class TestLoginCase:
    @pytest.mark.parametrize("error_data", login_data.error_info_middle)
    def test_error_alert_middle(self, access_web, error_data):
        access_web[1].submit_login(error_data["username"], error_data["password"])
        assert access_web[1].def_get_username_password_error_alert_text(), error_data["msg"]

    @pytest.mark.usefixtures("refresh_page")
    @pytest.mark.parametrize("success_data", login_data.success_login)
    def test_success_login(self, access_web, success_data):
        access_web[1].submit_login(success_data["username"], success_data["password"])
        assert access_web[2].def_get_welcome_title() == success_data["msg"]
