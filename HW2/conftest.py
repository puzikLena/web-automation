import pytest

import load_config
from site_helper import TestStandSite

data = load_config.load_config()


@pytest.fixture
def login_field():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture
def password_field():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture
def error():
    return '/html/body/div/main/div/div/div[2]/h2'


@pytest.fixture
def submit_button():
    return "button"


@pytest.fixture
def unauth_result():
    return "401"


@pytest.fixture
def site():
    site_instance = TestStandSite(data["test_host"])
    yield site_instance
    site_instance.close()
