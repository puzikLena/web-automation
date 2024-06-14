import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpCondition
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import load_config

data = load_config.load_config()
browser = data["browser"]


class TestStandSite:

    def __init__(self, address):
        self.address = address
        if browser == "chrome":
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)
        elif browser == "firefox":
            service = Service(executable_path=GeckoDriverManager().install())
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=service, options=options)

        time.sleep(data["sleep_time"])

    def wait_and_maximize(self):
        self.driver.implicitly_wait(data['implicitly_wait_timeout_sec'])
        self.driver.maximize_window()

    def find_element(self, mode="", path=""):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def find_element_with_time(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ExpCondition.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_element_property(self, mode, path, element_property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(element_property)

    def go_to_site(self):
        return self.driver.get(self.address)

    def close(self):
        self.driver.close()

    def get_text_from_alert(self):
        return self.driver.switch_to.alert.text
