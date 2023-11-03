import time

from pageObject.Login_object import Login_Amazon
from Utilities.Logger import LogGenerator
from Utilities.ReadConfig import ReadConfig
from pageObject.BillingAddress_object import Amazon_Address_Change


class Test_Billing_Address:
    logs = LogGenerator.Loggen()
    username = ReadConfig.GetUserName()
    password = ReadConfig.GetPassword()

    def test_change_address_004(self, setup):
        self.logs.info("Browser is Opening")
        self.driver = setup
        self.login = Login_Amazon(self.driver)
        self.logs.info("User login to account")
        self.login.click_on_login_link()
        self.logs.info("Enter Username")
        self.login.enter_email_id(self.username)
        self.logs.info("Click on Continue Button")
        self.login.click_on_continue_button()
        self.logs.info("Enter Password")
        self.login.enter_password(self.password)
        self.logs.info("Click on Sign In button")
        self.login.click_on_signin_button()
        self.logs.info("******* Create Object for Billing Address *******")
        self.bill_add = Amazon_Address_Change(self.driver)
        self.logs.info("Click on Account & List link")
        self.bill_add.click_on_account_list()
        self.logs.info("Click on address setting")
        self.bill_add.click_on_address_setting_option()
        self.logs.info("Click on edit option address window")
        self.bill_add.click_on_edit_link()
        self.driver.save_screenshot("D:\\Python\\Revision 1\\Amazon\\screenshot\\popup_win.png")
        curr_window = self.driver.current_window_handle
        print(curr_window.title())
        print(curr_window)
        self.driver.switch_to.window(curr_window)
        self.logs.info("click on cancel button")
        self.bill_add.click_on_cancel_button()
        time.sleep(5)
        # curr_window = self.driver.current_window_handle
        # self.driver.switch_to.window(curr_window)
        # time.sleep(5)
        self.logs.info("click on add address")
        self.bill_add.click_on_add_address()
        self.logs.info("select country")
        self.bill_add.select_country()
        self.logs.info("Enter first Name and Last Name")
        self.bill_add.enter_firstName_LastName("Akhil Mangalkar")
