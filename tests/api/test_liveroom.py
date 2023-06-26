import os
import time

import pytest
import requests
import json
import loadData.payloadData as Payload
from datetime import datetime
import allure


@allure.feature('test_liveroom_page')
class TestLivePage:
    @allure.title('test_follow_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_follow_user(self, get_config_data, viewer1_auth_header):
        """
        viewer: viewer1_username follow streamer: automation
        """
        print(get_config_data['chest_info'])
        print(type(get_config_data['chest_info']))
        with allure.step('before follow streamer: automation not in sidebar following list'):
            before_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                        json=Payload.sidebar_follow_user_list())
            before_side_response_json = json.loads(before_response.text)
            assert before_response.status_code == 200
            before_side_follow_list = before_side_response_json['data']['me']['private']['followeeFeed']['list']
            print(before_side_follow_list)
            for i in before_side_follow_list:
                if i['displayname'] == get_config_data['follow_streamer']:
                    print('follow streamer already on sidebar following list')
                    assert False

        with allure.step('start to follow streamer'):
            follow_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                            json=Payload.follow_user(get_config_data['follow_streamer']))
            follow_response_json = json.loads(follow_response.text)
            assert follow_response.status_code == 200
            assert follow_response_json['data']['follow']['err'] is None
        time.sleep(15)
        with allure.step('after follow streamer: automation in sidebar following list'):
            after_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                           json=Payload.sidebar_follow_user_list())
            after_side_response_json = json.loads(after_response.text)
            after_side_follow_list = after_side_response_json['data']['me']['private']['followeeFeed']['list']
            user_follow_list = False
            for i in after_side_follow_list:
                print(i['displayname'])
                if i['displayname'] == get_config_data['follow_streamer']:
                    print('after follow streamer, streamer in sidebar following list')
                    user_follow_list = True
                    break
            assert user_follow_list is True

    @allure.title('test_unfollow_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_unfollow_user(self, get_config_data, viewer1_auth_header):
        """
        viewer: viewer1_username unfollow streamer: automation
        """
        with allure.step('start to unfollow streamer'):
            follow_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                            json=Payload.unfollow_user(get_config_data['follow_streamer']))
            follow_response_json = json.loads(follow_response.text)
            assert follow_response.status_code == 200
            assert follow_response_json['data']['unfollow']['err'] is None
        time.sleep(10)
        with allure.step('after unfollow streamer: automation not in sidebar following list'):
            after_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                           json=Payload.sidebar_follow_user_list())
            after_side_response_json = json.loads(after_response.text)
            after_side_follow_list = after_side_response_json['data']['me']['private']['followeeFeed']['list']
            print(after_side_follow_list)
            for i in after_side_follow_list:
                if i['displayname'] == get_config_data['follow_streamer']:
                    print('after unfollow streamer, streamer still in sidebar following list')
                    assert False

    @allure.title('test_send_message_and_emo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_send_message_and_emo(self, get_config_data, viewer1_auth_header):
        """"
        viewer1 send message and emo to streamer: automation chat
        """
        with allure.step('Send message and emo to chat'):
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H%M%S")
            print(currentTime)
            message = "AAA " + get_config_data['send_message'] + '_' + currentTime
            response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                     json=Payload.send_chat(get_config_data['follow_streamer'],
                                                            message, [0, 2]))
            assert response.status_code == 200
            response_json = json.loads(response.text)
            print(response_json)
        with allure.step('check response error code is null and message is the send message'):
            assert response_json['data']['sendStreamchatMessage']['err'] is None
            assert response_json['data']['sendStreamchatMessage']['message']['content'] == message

    @allure.title('test_donate_1_lemon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_donate_1_lemon(self, get_config_data, viewer1_auth_header):
        """"
        viewer1 donate 1 lemon to streamer: automation chat
        """
        with allure.step('Get viewer1 origin total lemon'):
            all_lemon = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                      json=Payload.sidebar_follow_user_list())
            assert all_lemon.status_code == 200
            response_json = json.loads(all_lemon.text)
            origin_lemon = response_json['data']['me']['wallet']['balance'][:-5]
            print('origin lemon is: ' + origin_lemon)
        with allure.step('Start to donate 1 lemon'):
            print('donate lemon is: ' + str(get_config_data['donate_value']))
            response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                     json=Payload.donate_lemon(get_config_data['follow_streamer_permlink'],
                                                               get_config_data['donate_value']))
            response_json = json.loads(response.text)
            print(response_json)
            with allure.step('verify no error code in response and account is the as in config file'):
                assert response_json['data']['donate']['err'] is None
                assert response_json['data']['donate']['recentCount'] == get_config_data['donate_value']
        time.sleep(10)
        with allure.step('Check account reduction lemon is correct'):
            after_donate_all_lemon = requests.post(get_config_data['url'], headers=viewer1_auth_header,
                                                   json=Payload.sidebar_follow_user_list())
            response_json = json.loads(after_donate_all_lemon.text)
            after_donate_lemon = response_json['data']['me']['wallet']['balance'][:-5]
            print('after donate lemon is: ' + after_donate_lemon)
            lemon = int(origin_lemon) - int(get_config_data['donate_value'])
            assert int(after_donate_lemon) == lemon


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_liveroom.py', '--alluredir', 'results'])
    os.system('allure generate ./results -o ./report --clean')
