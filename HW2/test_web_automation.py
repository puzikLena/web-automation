import logging
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import load_config

XPATH = "xpath"
CSS = "css"
INVALID_DATA = "invalid_data"
FIND_TIMEOUT = 4

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "lake.png")

data = load_config.load_config()
username = data["username"]


def test_failed_login(login_field, password_field, submit_button, error, unauth_result, site):
    site.go_to_site()
    logging.info("Test Step 1 \"Test Failed login\" starting")

    logging.info("Find login and password fields")
    login_text_field = site.find_element(XPATH, login_field)
    password_text_field = site.find_element(XPATH, password_field)

    logging.info("Input invalid auth data")
    login_text_field.send_keys(INVALID_DATA)
    password_text_field.send_keys(INVALID_DATA)

    logging.info("Find and click at login button")
    login_button = site.find_element(CSS, submit_button)
    login_button.click()
    time.sleep(0.5)
    error_text = site.find_element(XPATH, error)

    logging.info("Check error text is equals with predefined")
    assert error_text.text == unauth_result


def test_success_login(login_field, password_field, submit_button, error, unauth_result, site):
    site.go_to_site()
    logging.info("Test Step 2 \"Test success login\" starting")

    logging.info("Find login and password fields")
    input1 = site.find_element(XPATH, login_field)
    input2 = site.find_element(XPATH, password_field)

    logging.info("Input correct auth data")
    input1.send_keys(username)
    input2.send_keys(data["password"])

    logging.info("Find and click at login button")
    login_button = site.find_element(CSS, submit_button)
    login_button.click()

    time.sleep(1)

    logging.info("Find and check is username equals with username")
    hello_text = site.find_element(XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a').text
    assert hello_text == f"Hello, {username}"


def test_success_post_creation(site, login_field, password_field, submit_button):
    site.go_to_site()
    logging.info("Find login and password fields")
    input1 = site.find_element(XPATH, login_field)
    input2 = site.find_element(XPATH, password_field)

    logging.info("Input correct auth data")
    input1.send_keys(username)
    input2.send_keys(data["password"])

    logging.info("Find and click at login button")
    login_button = site.find_element(CSS, submit_button)
    login_button.click()

    WebDriverWait(site.driver, FIND_TIMEOUT).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#create-btn")))

    logging.info("Find create post field and fill them")
    site.find_element(CSS, "#create-btn").click()
    site.find_element(XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label')\
        .send_keys(data['post_title'])
    site.find_element(XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label')\
        .send_keys(data['post_description'])
    site.find_element(XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label')\
        .send_keys(data['post_content'])
    site.find_element(XPATH, '//*[@id="create-item"]/div/div/div[6]/div/div/label/input')\
        .send_keys(file_path)

    logging.info("Click on create post button")
    site.find_element(XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')\
        .click()

    WebDriverWait(site.driver, FIND_TIMEOUT).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))

    logging.info("Find and check post title is equals with predefined")
    post_title = site.find_element(XPATH, '//*[@id="app"]/main/div/div[1]/h1').text
    assert data["post_title"] == post_title, "Hello, World!"
