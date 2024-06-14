import pytest

import load_config
from site_helper import TestStandSite

data = load_config.load_config()


@pytest.fixture
def site():
    site_instance = TestStandSite(data["test_host"])
    yield site_instance
    site_instance.driver.quit()
