import json

import requests
from loadData import payloadData


def get_auth_header(auth_token):
    token = {'authorization': auth_token}
    return token


def api_post(url, header, payload):
    response = requests.post(url, headers=header, json=payload)
    response_json = json.loads(response.text)
    return response_json


def get_login_auth(url, username, password):
    response = api_post(url, payloadData.normal_header(), payloadData.login(username, password))
    text = response.json()
    auth_token = text['data']['loginWithEmail']['me']['private']['accessToken']
    return auth_token


def get_account_lemon(url, header):
    all_lemon = requests.post(url, headers=header, json=payloadData.sidebar_follow_user_list())
    response_json = json.loads(all_lemon.text)
    lemon = response_json['data']['me']['wallet']['balance'][:-5]
    return lemon


