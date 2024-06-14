import requests

import load_config

data = load_config.load_config()

XAUTH_HEADER = "X-Auth-Token"


class ApiHelper:
    @staticmethod
    def get_response_get_posts(login, order="ASC"):
        return requests.get(
            data["posts_api_host"],
            headers={XAUTH_HEADER: login},
            params={"owner": "notMe", "order": order}
        )

    @staticmethod
    def create_post(login):
        response = requests.post(
            url=data['posts_gateway_host'],
            headers={XAUTH_HEADER: login},
            data={
                'title': data['post_title'],
                'description': data['post_description'],
                'content': data['post_content']
            }
        )
        return response
