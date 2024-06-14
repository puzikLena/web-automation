import logging
import os
import time

import load_config
from locators import CommonLocators
from page_objects import TestStandHelper, ContactPageHelper
from api_helper import ApiHelper

UNAUTH_CODE = "401"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "lake.png")

data = load_config.load_config()

username = data["username"]
password = data["password"]


def test_unsuccessful_login(site):
    logging.info("Test1 Starting")
    site_helper = TestStandHelper(site)
    site_helper.go_to_site()
    site_helper.enter_login("test")
    site_helper.enter_pass("test")
    site_helper.click_login_button()
    time.sleep(0.5)
    assert site_helper.get_error_text() == UNAUTH_CODE


def test_successful_login(site):
    logging.info("Test2 Starting")
    page_helper = TestStandHelper(site)
    page_helper.go_to_site()
    page_helper.enter_login(username)
    page_helper.enter_pass(password)
    page_helper.click_login_button()
    hello_text = page_helper.find_element_with_time(CommonLocators.LOCATOR_HELLO_TEXT).text
    assert hello_text == f"Hello, {username}"


def test_user_can_create_post(site):
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
    time.sleep(2)
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


def test_api_get_posts(login):
    # response = ApiHelper.get_response_get_posts(login)
    # titles = [i["title"] for i in response.json()["data"]]
    # logging.info(f"We have got posts")
    # assert response.status_code == 200 and data["title_test_rest"] in titles

    logging.info("Test Step 1 \"Check title in posts\" starting")
    response = ApiHelper.get_response_get_posts(login)
    logging.info("Check the response is successful")
    assert response.status_code == 200
    titles = [item['title'] for item in response.json()['data']]
    logging.info("Check is defined title contains in response")
    assert "My firt post" in titles


def test_api_create_post(login):
    response = ApiHelper.create_post(login)
    logging.info("New post was created")
    response2 = ApiHelper.get_response_get_posts(login, order="DESC")
    descriptions = [i["description"] for i in response2.json()["data"]]
    if response.status_code == response2.status_code == 200:
        assert "erfwergfwergerg" in descriptions
