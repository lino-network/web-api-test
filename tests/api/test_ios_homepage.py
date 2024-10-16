import json
import os
import time

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

    @allure.title('test_ios_AdvertisesInfo_carousel_mid')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_AdvertisesInfo_carousel_mid(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：AdvertisesInfo

        测试轮播的广告接口没报错

        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('测试轮播的广告接口没报错'):
            p = ["carousel_mid"]
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.IOS().ios_AdvertisesInfo(p))
            with allure.step('检查返回值不报错'):
                assert "err "not in response_json['data']['Advertises']

    @allure.title('test_ios_AdvertisesInfo_livestream')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_AdvertisesInfo_livestream(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：AdvertisesInfo

        测试直播流的广告接口没报错

        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('测试直播流的广告接口没报错'):
            p = ["livestream"]
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.IOS().ios_AdvertisesInfo(p))
            with allure.step('检查返回值不报错'):
                assert "err "not in response_json['data']['Advertises']

    @allure.title('test_ios_liveCarousel')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_liveCarousel(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： liveCarousel
        检查IOS 轮播接口是否有报错

        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('测试轮播接口没报错'):
            p = ["livestream"]
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.IOS().ios_liveCarousel())
            with allure.step('检查返回值不报错'):
                assert "err "not in response_json['data']['liveCarousel']

    @allure.title('test_ios_listRecommendation')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_listRecommendation(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：listRecommendation

        检查 channel you like 模块接口不报错

        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('检查 channel you like 模块接口不报错'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.IOS().ios_listRecommendation())
            with allure.step('检查返回值不报错'):
                assert "err " not in response_json['data']['listRecommendation']

    @allure.title('test_ios_checkUsersAccountLemon')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_checkUsersAccountLemon(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：fetchMyBalance

        检查用户的账户lemon 接口是否报错

        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('检查用户的账户lemon 接口是否报错'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.IOS().ios_fetchMyBalance())
            with allure.step('检查返回值不报错'):
                assert "err " not in response_json['data']['me']

    @allure.title('test_ios_myEmotes')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_myFavoritetorEmotes(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：myEmotes
        检查登录用户的 Emotes对不对
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('检查登录用户的 Emotes对不对'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.IOS().ios_myEmotes())
            with allure.step('检查返回值不报错'):
                assert "err " not in response_json['data']['me']
            with allure.step('检查最喜欢的表情在list里面'):
                list1 = response_json['data']['me']['emote']['mine']['list']
                is_exist = False
                for i in list1:
                    if i['name'] == '3a9f7388900813c_300300':
                        is_exist = True
                        assert 'dlive-degnujtptx' == i['username']
                        assert 'USER_LEVEL' == i['level']
                        assert 'EMOTE' == i['type']
                assert is_exist is True, '最喜欢的表情在list里面'

    @allure.title('test_ios_IsFirstLemonPurchase')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_IsFirstLemonPurchase(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： test_ios_IsFirstLemonPurchase
        检查用户是否购买过lemon，接口是否报错
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                        Payload.IOS().ios_IsFirstLemonPurchase(get_config_data['viewer1_username']))
        with allure.step('接口没报错'):
            assert response_json['data']['IsFirstLemonPurchase']['err'] is None
        with allure.step('检查用没有购买过lemon'):
            assert response_json['data']['IsFirstLemonPurchase']['isFirstLemonPurchase'] is True

    @allure.title('test_ios_isFirstThirdLogin')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_isFirstThirdLogin(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： isFirstThirdLogin
        检查用户是否第一次登录，接口是否报错
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                        Payload.IOS().ios_isFirstThirdLogin(get_config_data['viewer1_username']))
        with allure.step('检查用户是否第一次登录'):
            assert response_json['data']['isFirstThirdLogin']['isFirstThirdLogin'] is False

    @allure.title('test_ios_systemMessage')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_systemMessage(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： systemMessage
        检查系统消息接口是否报错
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                        Payload.IOS().ios_systemMessage())
        with allure.step('检查系统消息接口无报错'):
            assert 'err' not in response_json['data']['globalInfo']




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