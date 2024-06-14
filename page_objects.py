import logging

from locators import CommonLocators, ContactPageLocators
from site_helper import TestStandSite


class TestStandHelper:

    def __init__(self, site: TestStandSite):
        self.site = site

    def find_element_with_time(self, location, time=5):
        return self.site.find_element_with_time(location, time)

    def go_to_site(self):
        return self.site.go_to_site()

    def enter_login(self, username):
        login_field = self.site.find_element_with_time(CommonLocators.LOCATOR_LOGIN_FIELD)
        logging.info("Clear login text field")
        login_field.clear()
        logging.info(f"Try to input {username} to element {CommonLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field.send_keys(username)

    def enter_pass(self, password):
        pass_field = self.find_element_with_time(CommonLocators.LOCATOR_PASS_FIELD)
        logging.info("Clear password text field")
        pass_field.clear()
        logging.info(f"Try to input {password} to element {CommonLocators.LOCATOR_PASS_FIELD[1]}")
        pass_field.send_keys(password)

    def click_login_button(self):
        logging.info("Click at login button")
        self.find_element_with_time(CommonLocators.LOCATOR_LOGIN_BTN).click()

    def login(self, login, passwd):
        self.enter_login(login)
        self.enter_pass(passwd)
        self.click_login_button()

    def get_error_text(self):
        error_field = self.find_element_with_time(CommonLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"We found text {text} in error field {CommonLocators.LOCATOR_ERROR_FIELD[1]}")
        logging.info(f"Field {CommonLocators.LOCATOR_ERROR_FIELD[1]} contains text {text}")
        return text

    def click_on_create_post_btn(self):
        self.find_element_with_time(CommonLocators.LOCATOR_CREATE_POST_BTN).click()

    def enter_title(self, title):
        self.find_element_with_time(CommonLocators.LOCATOR_TITLE_INPUT).send_keys(title)

    def enter_description(self, description):
        self.find_element_with_time(CommonLocators.LOCATOR_DESCRIPTION_INPUT).send_keys(description)

    def enter_content(self, content):
        self.find_element_with_time(CommonLocators.LOCATOR_CONTENT_INPUT).send_keys(content)

    def attach_image(self, path):
        self.find_element_with_time(CommonLocators.LOCATOR_ATTACH_IMAGE).send_keys(path)

    def save_post(self):
        self.find_element_with_time(CommonLocators.LOCATOR_SAVE_POST_BTN).click()

    def contact_btn(self):
        self.find_element_with_time(CommonLocators.LOCATOR_CONTACT_BTN).click()


class ContactPageHelper:

    def __init__(self, site: TestStandSite):
        self.site = site

    def find_element_with_time(self, location, time=5):
        return self.site.find_element_with_time(location, time)

    def input_name(self, name):
        self.find_element_with_time(ContactPageLocators.LOCATOR_CONTACT_NAME_INPUT).send_keys(name)

    def input_email(self, email):
        self.find_element_with_time(ContactPageLocators.LOCATOR_CONTACT_EMAIL_INPUT).send_keys(email)

    def input_content(self, content):
        self.find_element_with_time(ContactPageLocators.LOCATOR_CONTACT_CONTENT_INPUT).send_keys(content)

    def submit_form(self):
        self.find_element_with_time(ContactPageLocators.LOCATOR_CONTACT_SUBMIT_BTN).click()

    def get_text_from_alert(self):
        return self.site.get_text_from_alert()
