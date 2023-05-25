import json
import requests


import loadData.payloadData as Payload


def test_follow_user(get_config_data, auth_header):
    print(get_config_data)
    response = requests.post(get_config_data['url'], headers=auth_header,
                             json=Payload.follow_user(get_config_data['follow_user']))
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 200
    assert response_json['data']['follow']['err'] is None


def test_follow_user_in_sidebar(get_config_data, auth_header):
    response = requests.post(get_config_data['url'], headers=auth_header,
                             json=Payload.sidebar_follow_user_list())
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 200
    follow_list = response_json['data']['me']['private']['followeeFeed']['list']
    print(follow_list)
    for i in follow_list:
        if i['username'] == 'appletron':
            print('44444')
            assert True



