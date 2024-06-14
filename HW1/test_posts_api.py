import logging

import requests

import load_config

AUTH_TOKEN_HEADER = 'X-Auth-Token'

data = load_config.load_config()


def test_check_title_in_posts_title(user_token, post_title):
    logging.info("Test Step 1 \"Check title in posts\" starting")
    response = requests.get(url=data['posts_api_host'], headers={AUTH_TOKEN_HEADER: user_token},
                            params={'owner': 'notMe', 'order': 'ASC'})
    logging.info("Check the response is successful")
    assert response.status_code == 200
    titles = [item['title'] for item in response.json()['data']]
    logging.info("Check is defined title contains in response")
    assert post_title in titles


def test_check_post_description(user_token):
    logging.info("Test Step 2 \"Check post description\" starting")
    create_post_body = {
        'title': data['post_title'],
        'description': data['post_description'],
        'content': data['post_content']
    }
    logging.info("Trying to execute add post request")
    create_post_response = requests.post(
        url=data['posts_gateway_host'],
        headers={AUTH_TOKEN_HEADER: user_token},
        data=create_post_body,
    )
    logging.info("Check is the add post request is successful")
    assert create_post_response.status_code == 200

    logging.info("Trying to execute get posts request")
    get_posts_response = requests.get(
        url=data['posts_api_host'],
        headers={AUTH_TOKEN_HEADER: user_token},
    )

    logging.info("Check is the get posts request is successful")
    assert get_posts_response.status_code == 200

    descriptions = [post_item["description"] for post_item in get_posts_response.json()['data']]
    logging.info("Check is the predefined post description contains in the posts")
    assert data['post_description'] in descriptions
