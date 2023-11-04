from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Amazon_Address_Change:
    click_account_list_xpath = (By.XPATH, "//*[@class='nav-a nav-a-2 nav-truncate   nav-progressive-attribute']")
    click_address_setting_xpath = (By.XPATH, "//*[@id='a-page']/div[1]/div/div[3]/div[1]/a/div/div/div")
    click_edit_link = (By.LINK_TEXT, "Edit")
    show_error_class = (By.CLASS_NAME, "a-section")
    click_cancel_xpath = (By.XPATH, "//*[@id='editAddressModal-0-cancel-btn-announce']")

    click_add_address_xpath = (By.XPATH, "//*[@id='ya-myab-plus-address-icon']")
    select_country_xpath = (By.XPATH, "//*[@id='address-ui-widgets-countryCode']/span/span")
    enter_f_name_l_name_xpath = (By.XPATH, "//*[@id='address-ui-widgets-enterAddressFullName']")
    enter_mob_number_xpath = (By.XPATH, "//*[@id='address-ui-widgets-enterAddressPhoneNumber']")
    enter_pin_code_xpath = (By.XPATH, "//*[@id='address-ui-widgets-enterAddressPostalCode']")
    enter_flat_no_house_xpath = (By.XPATH, "//*[@id='address-ui-widgets-enterAddressLine1']")
    enter_area_street_xpath = (By.XPATH, "//*[@id='address-ui-widgets-enterAddressLine2']")
    enter_landmark_xpath = (By.XPATH, "//input[@id='address-ui-widgets-landmark']")
    enter_city_xpath = (By.XPATH, "//*[@id='address-ui-widgets-enterAddressCity']")
    select_state_xpath = (By.XPATH, "//*[@id='address-ui-widgets-enterAddressStateOrRegion']/span/span/span")
    click_mark_default_address_xpath = (By.XPATH, "//*[@id='address-ui-widgets-use-as-my-default']")
    click_add_address_button_xpath = (By.XPATH, "//*[@id='address-ui-widgets-form-submit-button']/span/input")

    def __init__(self, driver):
        self.driver = driver

    def click_on_account_list(self):
        self.driver.find_element(*Amazon_Address_Change.click_account_list_xpath).click()

    def click_on_address_setting_option(self):
        self.driver.find_element(*Amazon_Address_Change.click_address_setting_xpath).click()

    def click_on_edit_link(self):
        self.driver.find_element(*Amazon_Address_Change.click_edit_link).click()

    def click_on_cancel_button(self):
        self.driver.find_element(*Amazon_Address_Change.click_cancel_xpath).click()

    def click_on_add_address(self):
        self.driver.find_element(*Amazon_Address_Change.click_add_address_xpath).click()

    def select_country(self):
        country = self.driver.find_element(*Amazon_Address_Change.select_country_xpath).text
        print(country)
        if country == 'India':
            assert True, 'Selected Country matched'
            pass
        else:
            Select(self.driver.find_element(*Amazon_Address_Change.select_country_xpath)).select_by_value("India")
            assert False

    def enter_firstName_LastName(self, first_last):
        self.driver.find_element(*Amazon_Address_Change.enter_f_name_l_name_xpath).clear()
        self.driver.find_element(*Amazon_Address_Change.enter_f_name_l_name_xpath).send_keys(first_last)

    def enter_mobile_no(self, mob):
        if len(mob) > 10:
            assert False
        else:
            self.driver.find_element(*Amazon_Address_Change.enter_mob_number_xpath).send_keys(mob)
            return True

    def enter_pin_code(self, pin):
        if len(pin) > 6:
            assert False
        else:
            self.driver.find_element(*Amazon_Address_Change.enter_pin_code_xpath).send_keys(pin)
            return True

    def enter_flat_no_house(self, flat_house):
        self.driver.find_element(Amazon_Address_Change.enter_flat_no_house_xpath).clear()
        self.driver.find_element(Amazon_Address_Change.enter_flat_no_house_xpath).send_keys(flat_house)

    def enter_area_street(self, area_street):
        self.driver.find_element(*Amazon_Address_Change.enter_area_street_xpath).clear()
        self.driver.find_element(*Amazon_Address_Change.enter_area_street_xpath).send_keys(area_street)

    def enter_landmark(self, landmark):
        self.driver.find_element(*Amazon_Address_Change.enter_landmark_xpath).send_keys(landmark)

    def enter_city(self, city):
        self.driver.find_element(*Amazon_Address_Change.enter_city_xpath).send_keys(city)

    def select_state(self, state):
        Select(self.driver.find_element(*Amazon_Address_Change.select_state_xpath)).select_by_visible_text(state)

    def click_add_address_button(self):
        self.driver.find_element(*Amazon_Address_Change.click_add_address_button_xpath).click()