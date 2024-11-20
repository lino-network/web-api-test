import json

import requests
from loadData import payloadData


def api_post(url, header, payload):
    response = requests.post(url, headers=header, json=payload)
    response_json = json.loads(response.text)
    return response_json


def get_login_auth_header(url, username, password):
    response = api_post(url, payloadData.normal_header(), payloadData.login(username, password))
    auth_token = response['data']['loginWithEmail']['me']['private']['accessToken']
    return {'authorization': auth_token}


def get_account_lemon(url, header):
    all_lemon = requests.post(url, headers=header, json=payloadData.sidebar_follow_user_list())
    response_json = json.loads(all_lemon.text)
    lemon = response_json['data']['me']['wallet']['balance'][:-5]
    return lemon


def get_video_permlink(url, header, payload, title):
    permlink_name = ''
    resp = requests.post(url=url, headers=header, json=payload)
    response_json = json.loads(resp.text)
    permlink_list = response_json['data']['userByDisplayName']['videos']['list']
    is_link = False
    print(permlink_list)
    for link in permlink_list:
        if link['title'] == title:
            permlink_name = link['permlink']
            is_link = True
            assert True
            break
    if is_link is False:
        assert False, '找不到相应的video 视频'
    return permlink_name


if __name__ == '__main__':
    # print(type(get_login_auth_header('https://graphigo.stg.dlive.tv/', 'automation@nqmo.com', 'Pwd@1234')))
    # print(get_login_auth_header('https://graphigo.stg.dlive.tv/', 'automation@nqmo.com', 'Pwd@1234'))
    url = 'https://graphigo.stg.dlive.tv/'
    email = 'automation@nqmo.com'
    password = 'Pwd@1234'
    data = payloadData.MyProfileAPI().LivestreamProfileVideo('automation')
    auth = (get_login_auth_header(url, email, password))
    link = get_video_permlink(url, auth, data, 'automationTitle_171605')
    print(link)
