import time

from selenium.webdriver.common.by import By

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
        # self.logs.info("Click on edit option address window")
        # self.bill_add.click_on_edit_link()
        # self.driver.save_screenshot("D:\\Python\\Revision 1\\Amazon\\screenshot\\popup_win.png")
        # curr_window = self.driver.current_window_handle
        # self.driver.set_window_size(400, 250, curr_window)
        # all_win = self.driver.window_handles
        # print(all_win)
        # self.logs.info("Create condition to choose window")
        # if curr_window == all_win[0]:
        #     self.logs.info("switch to 2nd window")
        #     self.driver.switch_to.window(all_win[1])
        #     time.sleep(3)
        #     self.logs.info("Close 2nd window")
        #     self.driver.close()
        #     time.sleep(3)
        #     self.logs.info("switch to current window")
        #     self.driver.switch_to.window(curr_window)
        #     time.sleep(3)
        #     self.logs.info("click on cancel button")
        #     self.bill_add.click_on_cancel_button()
        self.logs.info("click on add address")
        self.bill_add.click_on_add_address()
        self.logs.info("select country")
        self.bill_add.select_country()
        self.logs.info("Enter first Name and Last Name")
        self.bill_add.enter_firstName_LastName("Akhil Mangalkar")
        self.logs.info("Enter 10 digit mobile no")
        self.bill_add.enter_mobile_no("9975563502")
        print(True)
        self.logs.info("Enter 6 digit pin code")
        self.bill_add.enter_pin_code("444605")
        print(True)
        self.logs.info("Enter Flat No and House No")
        self.driver.execute_script("window.scrollBy(0, 300)", " ")
        time.sleep(3)
        self.bill_add.enter_flat_no_house("32A, Shri. Siddhivinayak Colony, Behind Ghanshyam Nagar")
        self.logs.info("Enter Area or Street")
        self.bill_add.enter_area_street("Saturna Parisar, Badnera Road")
        self.logs.info("Enter Landmark")
        self.bill_add.enter_landmark("Near Ganesh Temple")
        self.logs.info("Enter City")
        self.bill_add.enter_city("Amravati")
        self.logs.info("Select State")
        self.bill_add.select_state("MAHARASHTRA")
        bd = self.driver.find_element(By.TAG_NAME, "body").text
        self.logs.info("All Body", bd)
        print(bd)
        self.logs.info("Click 0n Add Address Button")
        self.bill_add.click_add_address_button()
        time.sleep(5)
        self.driver.save_screenshot("D:\\Python\\Revision 1\\Amazon\\screenshot\\complete_address.png")

