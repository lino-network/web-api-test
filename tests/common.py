import json

import requests
from loadData import payloadData


def api_post(url, header, payload):
    response = requests.post(url, headers=header, json=payload)
    response_json = json.loads(response.text)
    return response_json


def get_login_auth_header(url, username, password):
    response = api_post(url, payloadData.normal_header(), payloadData.login(username, password))
    print(response)
    auth_token = response['data']['loginWithEmail']['me']['private']['accessToken']
    return {'authorization': auth_token}


def get_account_lemon(url, header):
    all_lemon = requests.post(url, headers=header, json=payloadData.sidebar_follow_user_list())
    response_json = json.loads(all_lemon.text)
    lemon = response_json['data']['me']['wallet']['balance'][:-5]
    return lemon


if __name__ == '__main__':
    print(type(get_login_auth_header('https://graphigo.stg.dlive.tv/', 'automation@nqmo.com', 'Pwd@1234')))
    print(get_login_auth_header('https://graphigo.stg.dlive.tv/', 'automation@nqmo.com', 'Pwd@1234'))

