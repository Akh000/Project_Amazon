import time

import pytest

from pageObject.Profile_object import Profile_Information
from pageObject.Login_object import Login_Amazon
from Utilities.Logger import LogGenerator
from Utilities.ReadConfig import ReadConfig


class Test_profile_info:
    logs = LogGenerator.Loggen()
    username = ReadConfig.GetUserName()
    password = ReadConfig.GetPassword()

    @pytest.mark.skip
    def test_change_photo_003(self, setup):
        self.logs.info("Browser is Opening")
        self.driver = setup
        self.log = Login_Amazon(self.driver)
        self.logs.info("User login to account")
        self.log.click_on_login_link()
        self.log.enter_email_id(self.username)
        self.log.click_on_continue_button()
        self.log.enter_password(self.password)
        self.log.click_on_signin_button()
        self.logs.info("*** Opening Profile Manage setting ***")
        self.pf = Profile_Information(self.driver)
        self.logs.info("*** click on Manage profile ***")
        self.pf.click_on_manage_profile()
        self.logs.info("*** click on Profile setting ***")
        self.pf.click_on_profile_setting()
        time.sleep(5)
        self.logs.info("*** click on Image Icon***")
        self.pf.click_on_image()
        time.sleep(5)
        self.logs.info("*** click on Upload text***")
        self.pf.click_on_upload("D:\\Python\\Revision 1\\Amazon\\testdata\\baby.jpg")
