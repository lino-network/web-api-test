import json
import os
import pytest
import requests
import loadData.payloadData as Payload
from datetime import datetime, timedelta
import allure
import tests.common as common


@allure.feature('test_ios_homepage')
class TestIOSHomePage:
    @allure.title('test_ios_categories')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_categories(self, get_config_data, api_headers):
        """
        接口： categories
        首页检查 Categories 接口
        """
        with allure.step('检查 Categories 接口'):
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.AppHomepage.ios_categories())
            print(response_json)
            with allure.step('检查返回的 categories 不为空'):
                assert response_json['data']['categories']['list']  # 确认非空
            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

    @allure.title('test_ios_Livestreams')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_Livestreams(self, get_config_data, api_headers):
        """
        接口： Livestreams
        检查 Livestreams 接口
        """
        with allure.step('检查 Livestreams 接口'):
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.AppHomepage().ios_Livestreams())
            print(response_json)

            with allure.step('检查返回的 livestreams 不为空且没有错误'):
                assert response_json['data']['livestreams'] is not None
                assert response_json['data']['livestreams']['list']  # 确认 list 非空

            with allure.step('检查返回的每个 livestream 字段是否有效'):
                required_fields = ['permlink', 'title', 'thumbnailUrl', 'totalReward', 
                                   'watchingCount', 'createdAt', 'ageRestriction', 
                                   'earnRestriction', 'tags', 'category', 'creator']

                for livestream in response_json['data']['livestreams']['list']:
                    for field in required_fields:
                        assert field in livestream and livestream[field] is not None, f"{field} should not be None"

            with allure.step('检查 category 和 creator 是否存在'):
                for livestream in response_json['data']['livestreams']['list']:
                    assert 'category' in livestream and livestream['category'] is not None
                    assert 'creator' in livestream and livestream['creator'] is not None

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json



    @allure.title('test_ios_sendChat')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_sendChat(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口: sendChat

        用户viewer1发送信息和点赞的表情包给主播: automation
        """
        with allure.step('开始发送信息和点赞的表情包给主播'):
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H%M%S")
            print(currentTime)
            message = "AAA" + get_config_data['send_message'] + '_' + currentTime
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.AppChatroom().ios_sendChat(get_config_data['follow_streamer'], message,
                                                                            [0, 2]))
            print(response_json)
        with allure.step('检查返回值不报错'):
            assert response_json['data']['sendStreamchatMessage']['err'] is None
        with allure.step('检查返回的信息就是发送的信息'):
            assert response_json['data']['sendStreamchatMessage']['message']['content'] == message
'''
    @allure.title('test_current_user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_current_user(self, get_config_data, api_headers):
        """
        接口： CurrentUser
        检查当前用户接口
        """
        with allure.step('检查 CurrentUser 接口'):
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.AppHomepage().ios_Livestreams())
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 me 对象'):
                me = response_json['data']['me']
                assert me is not None

                required_user_fields = [
                    'username', 'avatar', 'displayname', 'partnerStatus', 
                    'location', 'role', 'hadLemonBack', 'bttReceiverAddress'
                ]
                for field in required_user_fields:
                    assert field in me and me[field] is not None, f"{field} should not be None"

                # 检查 Emoji 和 Emote 是否存在且不为 null
                assert 'emoji' in me and me['emoji'] is not None
                assert 'emote' in me and me['emote'] is not None

                # 检查 followers 和 following
                assert 'followers' in me and me['followers'] is not None
                assert 'following' in me and me['following'] is not None
                assert me['followers']['totalCount'] is not None
                assert me['following']['totalCount'] is not None

                # 检查 canSubscribe
                assert 'canSubscribe' in me

                # 检查 chat badges
                assert 'myChatBadges' in me
                assert 'myChatBadgesStr' in me
'''


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_ios_homepage.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')