import requests
import json
import loadData.payloadData as Payload


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
        break

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
        else:
            print('after follow streamer, streamer not in sidebar following list')
            assert False
        break


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
