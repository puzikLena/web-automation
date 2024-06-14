import logging
import os
import time

import load_config
from page_objects import CommonLocators
from page_objects import TestStandHelper, ContactPageHelper

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "lake.png")

UNAUTH_CODE = "401"

data = load_config.load_config()
username = data["username"]
password = data["password"]


def test_unsuccessful_login(site):
    logging.info("Test step 1 \"Check unsuccessful login\" starting")
    page_helper = TestStandHelper(site)
    page_helper.go_to_site()
    logging.info("Input invalid data")
    page_helper.enter_login("test")
    page_helper.enter_pass("test")
    page_helper.click_login_button()
    logging.info("Check that error text is equals with predefined value")
    assert page_helper.get_error_text() == UNAUTH_CODE


def test_successful_login(site):
    logging.info("Test step 2 \"Check successful login\" starting")
    page_helper = TestStandHelper(site)
    page_helper.go_to_site()
    logging.info("Input valid data")
    page_helper.enter_login(username)
    page_helper.enter_pass(password)
    page_helper.click_login_button()
    hello_text = page_helper.find_element_with_time(CommonLocators.LOCATOR_HELLO_TEXT).text
    logging.info("Check that hello text is equals with predefined value")
    assert hello_text == f"Hello, {username}"


def test_post_creation(site):
    logging.info("Test step 3 \"Post creation by user\" starting")
    page_helper = TestStandHelper(site)
    page_helper.go_to_site()
    page_helper.enter_login(username)
    page_helper.enter_pass(password)
    page_helper.click_login_button()
    page_helper.click_on_create_post_btn()
    page_helper.enter_title(data["post_title"])
    page_helper.enter_description(data["post_description"])
    page_helper.enter_content(data["post_content"])
    page_helper.attach_image(file_path)
    page_helper.save_post()
    page_helper.find_element_with_time(CommonLocators.LOCATOR_POST_IMAGE)
    post_title = page_helper.find_element_with_time(CommonLocators.LOCATOR_POST_TITLE).text
    logging.info(f"Check the post title is equals with expected value")
    assert post_title == data["post_title"]


def test_check_contact_us(site):
    logging.info("Test step 4 \"Check contact us info\" starting")
    page_helper = TestStandHelper(site)
    page_helper.go_to_site()
    page_helper.login(username, password)
    page_helper.contact_btn()
    contact_page_helper = ContactPageHelper(site)
    contact_page_helper.input_name(data["contact_name"])
    contact_page_helper.input_email(data["contact_email"])
    contact_page_helper.input_content(data["contact_content"])
    contact_page_helper.submit_form()
    time.sleep(2)
    text = contact_page_helper.get_text_from_alert()
    assert text == "Form successfully submitted"
