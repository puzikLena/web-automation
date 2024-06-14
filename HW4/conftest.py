import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import load_config
from site_helper import TestStandSite

data = load_config.load_config()


@pytest.fixture()
def login():
    response = requests.post(data["login_host"],
                             data={'username': data["username"], 'password': data["password"]})
    if response.status_code == 200:
        return response.json()["token"]


@pytest.fixture
def site():
    site_instance = TestStandSite(data["test_host"])
    yield site_instance
    site_instance.driver.quit()


@pytest.fixture(scope="function")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
