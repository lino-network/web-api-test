import requests
import json
import loadData.payloadData as Payload
from datetime import datetime


def test_follow_user(get_config_data, viewer1_auth_header):
    """
    viewer: viewer1_username follow streamer: automation
    """

    # before follow streamer: automation not in sidebar following list
    before_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                    json=Payload.sidebar_follow_user_list())
    before_side_response_json = json.loads(before_response.text)
    assert before_response.status_code == 200
    before_side_follow_list = before_side_response_json['data']['me']['private']['followeeFeed']['list']
    for i in before_side_follow_list:
        if i['displayname'] == get_config_data['follow_streamer']:
            print('follow streamer already on sidebar following list')
            assert False

    # start to follow streamer
    follow_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                    json=Payload.follow_user(get_config_data['follow_streamer']))
    follow_response_json = json.loads(follow_response.text)
    assert follow_response.status_code == 200
    assert follow_response_json['data']['follow']['err'] is None

    # after follow streamer: automation in sidebar following list
    after_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                   json=Payload.sidebar_follow_user_list())
    after_side_response_json = json.loads(after_response.text)
    after_side_follow_list = after_side_response_json['data']['me']['private']['followeeFeed']['list']
    for i in after_side_follow_list:
        if i['displayname'] == get_config_data['follow_streamer']:
            print('after follow streamer, streamer in sidebar following list')
            assert True
            break
        else:
            print('after follow streamer, streamer not in sidebar following list')
            assert False


def test_unfollow_user(get_config_data, viewer1_auth_header):
    """
    viewer: viewer1_username unfollow streamer: automation
    """
    # start to unfollow streamer
    follow_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                    json=Payload.unfollow_user(get_config_data['follow_streamer']))
    follow_response_json = json.loads(follow_response.text)
    assert follow_response.status_code == 200
    assert follow_response_json['data']['unfollow']['err'] is None

    # after unfollow streamer: automation not in sidebar following list
    after_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                   json=Payload.sidebar_follow_user_list())
    after_side_response_json = json.loads(after_response.text)
    after_side_follow_list = after_side_response_json['data']['me']['private']['followeeFeed']['list']
    print(after_side_follow_list)
    for i in after_side_follow_list:
        if i['displayname'] == get_config_data['follow_streamer']:
            print('after unfollow streamer, streamer still in sidebar following list')
            assert False


def test_send_message_and_emo(get_config_data, viewer1_auth_header):
    """"
    viewer1 send message and emo to streamer: automation chat
    """
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H%M%S")
    print(currentTime)
    message = "AAA " + get_config_data['send_message'] + '_' + currentTime
    response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                             json=Payload.send_chat(get_config_data['follow_streamer'],
                                                    message, [0, 2]))
    assert response.status_code == 200
    response_json = json.loads(response.text)
    assert response_json['data']['sendStreamchatMessage']['err'] is None
    assert response_json['data']['sendStreamchatMessage']['message']['content'] == message


def test_donate_1_lemon(get_config_data, viewer1_auth_header):
    """"
    viewer1 donate 1 lemon to streamer: automation chat
    """
    # Get viewer1 total lemon
    all_lemon = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                              json=Payload.sidebar_follow_user_list())
    assert all_lemon.status_code == 200
    response_json = json.loads(all_lemon.text)
    origin_lemon = response_json['data']['me']['wallet']['balance'][:-5]


