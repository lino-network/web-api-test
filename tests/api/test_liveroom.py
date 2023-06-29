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
        api: FollowUser, MeSidebar

        viewer: viewer1_username follow streamer: automation
        """
        with allure.step('check before follow streamer: automation not in sidebar following list'):
            before_side_response_json = common.api_post(get_config_data['url'], viewer1_auth_header,
                                                        Payload.sidebar_follow_user_list())
            before_side_follow_list = before_side_response_json['data']['me']['private']['followeeFeed']['list']
            print(before_side_follow_list)
            for i in before_side_follow_list:
                if i['displayname'] == get_config_data['follow_streamer']:
                    print('follow streamer already on sidebar following list before following')
                    assert False

        with allure.step('start to follow streamer'):
            follow_response_json = common.api_post(get_config_data['url'], viewer1_auth_header,
                                                   Payload.follow_user(get_config_data['follow_streamer']))
            assert follow_response_json['data']['follow']['err'] is None
        time.sleep(15)
        with allure.step('check after follow streamer: automation in sidebar following list'):
            after_side_response_json = common.api_post(get_config_data['url'], viewer1_auth_header,
                                                       Payload.sidebar_follow_user_list())
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
        api: sidebar_follow_user_list, UnfollowUser

        viewer: viewer1_username unfollow streamer: automation
        """
        with allure.step('start to unfollow streamer'):
            follow_response_json = common.api_post(get_config_data['url'], viewer1_auth_header,
                                                   Payload.unfollow_user(get_config_data['follow_streamer']))
            # follow_response = requests.post(get_config_data['url'], headers=viewer1_auth_header,
            #                                 json=Payload.unfollow_user(get_config_data['follow_streamer']))
            # follow_response_json = json.loads(follow_response.text)
            # assert follow_response.status_code == 200
            assert follow_response_json['data']['unfollow']['err'] is None
        time.sleep(10)
        with allure.step('check after unfollow streamer: automation not in sidebar following list'):
            after_side_response_json = common.api_post(get_config_data['url'], viewer1_auth_header,
                                                       Payload.sidebar_follow_user_list())
            after_side_follow_list = after_side_response_json['data']['me']['private']['followeeFeed']['list']
            print(after_side_follow_list)
            for i in after_side_follow_list:
                if i['displayname'] == get_config_data['follow_streamer']:
                    print('after unfollow streamer, streamer still in sidebar following list')
                    assert False

    @allure.title('test_send_message_and_emo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_send_message_and_emo(self, get_config_data, viewer1_auth_header):
        """
        api: SendStreamChatMessage

        viewer1 send message and emo to streamer: automation chat
        """
        with allure.step('Send message and emo to chat'):
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H%M%S")
            print(currentTime)
            message = "AAA " + get_config_data['send_message'] + '_' + currentTime
            response_json = common.api_post(get_config_data['url'], viewer1_auth_header,
                                            Payload.send_chat(get_config_data['follow_streamer'], message, [0, 2]))
            print(response_json)
        with allure.step('check response error code is null and message is the send message'):
            assert response_json['data']['sendStreamchatMessage']['err'] is None
            assert response_json['data']['sendStreamchatMessage']['message']['content'] == message

    @allure.title('test_donate_1_lemon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_donate_1_lemon(self, get_config_data, viewer1_auth_header):
        """
        api: StreamDonate, sidebar_follow_user_list

        viewer1 donate 1 lemon to streamer: automation chat
        """
        with allure.step('Get viewer1 origin total lemon'):
            origin_lemon = common.get_account_lemon(get_config_data['url'], viewer1_auth_header)
            print('origin lemon is: ' + origin_lemon)
        with allure.step('Start to donate 1 lemon'):
            print('donate lemon is: ' + str(get_config_data['donate_value']))
            response_json = common.api_post(get_config_data['url'], viewer1_auth_header,
                                            Payload.donate_lemon(get_config_data['follow_streamer_permlink'],
                                                                 get_config_data['donate_value']))
            print(response_json)
            with allure.step('verify no error code in response and account is the as in config file'):
                assert response_json['data']['donate']['err'] is None
                assert response_json['data']['donate']['recentCount'] == get_config_data['donate_value']
        time.sleep(10)
        with allure.step('Check account reduction lemon is correct'):
            after_donate_lemon = common.get_account_lemon(get_config_data['url'], viewer1_auth_header)
            print('after donate lemon is: ' + after_donate_lemon)
            lemon = int(origin_lemon) - int(get_config_data['donate_value'])
            assert int(after_donate_lemon) == lemon

    @allure.title('test one viewer gift 5 sub and 5 user to claim')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_give_5_sub_in_channel(self, get_config_data):
        """
        api: AddGiftSub, AddGiftSubClaim

        one viewer gift 5 sub in channel, and 5 viewer to claim
        """
        header = common.get_auth_header(get_config_data['gift_sub_info']['give_sub_gift_user_auth'])
        with allure.step('viewer ' + str(get_config_data['gift_sub_info']['give_sub_gift_user'])
                         + ' gift 5 sub in ''channel ' + str(get_config_data['gift_sub_info']['streamer'])):
            gift_response_json = common.api_post(get_config_data['url'], header,
                                                 Payload.add_gift_sub(get_config_data['gift_sub_info']['streamer'], 5))
            print(gift_response_json)
            with allure.step('verify response error message is null'):
                assert gift_response_json['data']['giftSub']['err'] is None
        claim_list = get_config_data['gift_sub_info']['claim_user']
        for i in claim_list:
            viewer_header = common.get_auth_header(i['get_gift_sub_user_auth'])
            with allure.step('viewer' + str(i['get_gift_sub_user']) + ' start to claim gift'):
                claim_response_json = common.api_post(get_config_data['url'], viewer_header,
                                                      Payload.add_gift_sub_claim(get_config_data['gift_sub_info']['streamer']))
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
    pytest.main(['./test_liveroom.py', '--alluredir', './report/results-20230627'])
    os.system('allure generate ./report/results-20230627 -o ./report/report-20230627 --clean')
