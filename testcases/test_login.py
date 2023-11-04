import pytest
from selenium.webdriver.common.by import By

from Utilities.Logger import LogGenerator
from pageObject.Login_object import Login_Amazon


class Test_Login:
    logs = LogGenerator.Loggen()

    @pytest.mark.skip
    def test_title_001(self, setup):
        self.logs.info("**Browser is Started**")
        self.driver = setup
        title = self.driver.title
        self.logs.info("*****Title is asserting****")
        if title == ("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - "
                     "Amazon.in"):
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_login_002(self, setup):
        self.logs.info("**Browser is Started**")
        self.driver = setup
        self.lg = Login_Amazon(self.driver)
        self.logs.info("****Amazon account is Logging****")
        self.lg.click_on_login_link()
        self.logs.info("Enter the email address")
        self.lg.enter_email_id("akhmangalkar2010@gmail.com")
        self.lg.click_on_continue_button()
        self.logs.info("Enter password")
        self.lg.enter_password("31awasani.")
        self.lg.click_on_signin_button()
        hello_msg = self.driver.find_element(By.XPATH, "//*[@id='nav-link-accountList-nav-line-1']").text
        self.logs.info("Asserting message after Login")
        if hello_msg == "Hello, Akhil":
            print(hello_msg, "***Pass Test***")
            assert True
        else:
            self.driver.save_screenshot("D:\\Python\\Revision 1\\Amazon\\screenshot\\test_login_002_Fail.png")
            print("Fail Test")
            assert False
        self.logs.info("****Sign out the account****")
        self.lg.click_on_sign_out()
