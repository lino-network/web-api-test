import os
import time
import pytest
import requests
import json
import loadData.payloadData as Payload
from datetime import datetime
import allure
import tests.common as common


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

    @allure.title('test one viewer gift 5 sub and 5 user to claim')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_give_5_sub_in_channel(self, get_config_data):
        """
        one viewer gift 5 sub in channel, and 5 viewer to claim
        :param get_config_data:
        :return:
        """
        header = common.get_auth_header(get_config_data['gift_sub_info']['give_sub_gift_user_auth'])
        print('11111111')
        print(header)
        with allure.step('viewer ' + str(get_config_data['gift_sub_info']['give_sub_gift_user'])
                         + ' gift 5 sub in ''channel ' + str(get_config_data['gift_sub_info']['streamer'])):
            gift_response = requests.post(get_config_data['url'], headers=header,
                                          json=Payload.add_gift_sub(get_config_data['gift_sub_info']['streamer'], 5))
            with allure.step('verify give gift sub response error code is 200'):
                assert gift_response.status_code == 200
            gift_response_json = json.loads(gift_response.text)
            print(gift_response_json)
            with allure.step('verify response error message is null'):
                assert gift_response_json['data']['giftSub']['err'] is None
        claim_list = get_config_data['gift_sub_info']['claim_user']
        for i in claim_list:
            viewer_header = common.get_auth_header(i['get_gift_sub_user_auth'])
            with allure.step('viewer' + str(i['get_gift_sub_user']) + ' start to claim gift'):
                claim_response = requests.post(get_config_data['url'], headers=viewer_header,
                                        json=Payload.add_gift_sub_claim(get_config_data['gift_sub_info']['streamer']))
                with allure.step('verify user ' + str(i['get_gift_sub_user']) + ' claim gift sub response error code is 200'):
                    assert claim_response.status_code == 200
                claim_response_json = json.loads(claim_response.text)
                with allure.step('verify user ' + str(i['get_gift_sub_user']) + ' claim response error message is null'):
                    assert claim_response_json['data']['giftSubClaim']['err'] is None

    @allure.title('test_streamer_add_lemon_to_chest')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_streamer_add_lemon_to_chest(self, get_config_data):
        """
        1. streamer add 20 lemon to chest
        2. user1: test_streamer_add_lemon_to_chest send message to chat and open chest
        3. user2: chest_donate_user2_auth donate lemon and open chest
        4. user3: chest_user_no_point_auth no point to open chest
        :param get_config_data:
        :param viewer1_auth_header:
        :return:
        """
        # with allure.step('streamer: automation check chest lemon and add lemon to chest'):
        #     origin_chest_lemon = requests.post(get_config_data['url'],
        #                                        headers=])common.get_auth_header(get_config_data['follow_streamer_auth',
        #                                        json=Payload.sidebar_follow_user_list())
        #     response_json = json.loads(origin_chest_lemon.text)
        #     origin_lemon = response_json['data']['me']['wallet']['balance'][:-5]
        print('origin chest lemon is: ')


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_liveroom.py', '--alluredir', 'results-20230628'])
    os.system('allure generate ./results-20230628 -o ./report-20230628 --clean')
