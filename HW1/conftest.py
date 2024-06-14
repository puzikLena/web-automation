import pytest
import requests

import load_config

data = load_config.load_config()


@pytest.fixture()
def user_token():
    request_body = {'username': data['username'], 'password': data['password']}
    response = requests.post(url=data['login_host'], data=request_body)
    if response.status_code == 200:
        return response.json()['token']


@pytest.fixture()
def post_title():
    return 'My firt post'
