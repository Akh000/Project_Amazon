from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Login_Amazon:
    login_link_xpath = (By.XPATH, "//*[@id='nav-link-accountList']")
    click_sign_in_xpath = (By.XPATH, "//div[@id='nav-flyout-ya-signin']//span[@class='nav-action-inner']["
                                     "normalize-space()='Sign in']")
    enter_email_id_id = (By.ID, "ap_email")
    click_continue_button_xpath = (By.XPATH, "//*[@id='continue']")
    enter_password_xpath = (By.XPATH, "//*[@id='ap_password']")
    click_sign_button_xpath = (By.XPATH, "//*[@id='signInSubmit']")
    click_sign_out_xpath = (By.XPATH, "//*[@id='nav-item-signout']/span")

    def __init__(self, driver):
        self.driver = driver

    def click_on_login_link(self):
        action = ActionChains(self.driver)
        login_link = self.driver.find_element(*Login_Amazon.login_link_xpath)
        click_sign_in = self.driver.find_element(*Login_Amazon.click_sign_in_xpath)
        action.move_to_element(login_link).move_to_element(click_sign_in).click().perform()

    def enter_email_id(self, email):
        self.driver.find_element(*Login_Amazon.enter_email_id_id).send_keys(email)

    def click_on_continue_button(self):
        self.driver.find_element(*Login_Amazon.click_continue_button_xpath).click()

    def enter_password(self, passwd):
        self.driver.find_element(*Login_Amazon.enter_password_xpath).send_keys(passwd)

    def click_on_signin_button(self):
        self.driver.find_element(*Login_Amazon.click_sign_button_xpath).click()

    def click_on_sign_out(self):
        action = ActionChains(self.driver)
        login_link = self.driver.find_element(*Login_Amazon.login_link_xpath)
        log_out = self.driver.find_element(*Login_Amazon.click_sign_out_xpath)
        action.move_to_element(login_link).move_to_element(log_out).click().perform()
