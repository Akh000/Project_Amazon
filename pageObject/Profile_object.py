import time
from selenium.webdriver.common.by import By


class Profile_Information:
    click_sign_link_xpath = (By.XPATH, "//*[@class='nav-a nav-a-2 nav-truncate   nav-progressive-attribute']")
    click_profile_xpath = (By.XPATH, "//a[normalize-space()='Profile']")
    click_image_xpath = (By.XPATH, "//*[@id='customer-profile-avatar-image']/div/span/div/div/div/div[1]/img")
    click_upload_xpath = (By.XPATH, "//*[@id='a-popover-content-1']/div/div/div/label/span")

    def __init__(self, driver):
        self.driver = driver

    def click_on_manage_profile(self):
        self.driver.find_element(*Profile_Information.click_sign_link_xpath).click()

    def click_on_profile_setting(self):
        profile = self.driver.find_element(*Profile_Information.click_profile_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", profile)
        self.driver.find_element(*Profile_Information.click_profile_xpath).click()

    def click_on_image(self):
        self.driver.find_element(*Profile_Information.click_image_xpath).click()

    def click_on_upload(self, image):
        self.driver.find_element(*Profile_Information.click_upload_xpath).send_keys(image)
