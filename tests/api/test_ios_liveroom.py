import json
import os
import time

import pytest
import requests
import loadData.payloadData as Payload
from datetime import datetime, timedelta
import allure
import tests.common as common


@allure.feature('test_ios_liveroom')
class TestIOSLivingPage:
    @allure.title('test_ios_CheckIfCanFreeSub')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_CheckIfCanFreeSub(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： freeSubOffer
        检查用户:viewer1_username具备首次免费订阅的资格
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                        Payload.IOS().ios_freeSubOffer(get_config_data['viewer1_username']))
        with allure.step('检查未订阅过的用户:viewer1_username具备首次免费订阅的资格'):
            assert response_json['data']['freeSubOffer']['err'] is None
            assert response_json['data']['freeSubOffer']['canFree'] is True
        response_json1 = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                         Payload.IOS().ios_freeSubOffer(get_config_data['follow_streamer']))
        with allure.step('检查已经订阅过的用户:automation不具备首次免费订阅的资格'):
            assert response_json1['data']['freeSubOffer']['err'] is None
            assert response_json1['data']['freeSubOffer']['canFree'] is False

    @allure.title('test_ios_FollowStreamer')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_1_FollowStreamer(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： follow
        检查用户viewer1_username: follow主播: automation功能是否正常
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                        Payload.IOS().ios_follow(get_config_data['follow_streamer']))
        with allure.step('检查follow 的接口没报错'):
            assert response_json['data']['follow']['err'] is None
        time.sleep(10)
        with allure.step('检查follow主播以后，主播在用户的following list的接口没报错'):
            following_resp = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                             Payload.IOS().ios_FollowingList(get_config_data['viewer1_username']))
            following_list = following_resp['data']['user']['following']['list']
            print('following_list: ' + str(following_list))
            is_exists = False
            for i in following_list:
                if i['username'] == get_config_data['follow_streamer']:
                    is_exists = True
                    assert i['isFollowing'] is True
            assert is_exists is True, 'Following 的主播：automation不在关注列表'

    @allure.title('test_ios_UnFollowStreamer')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_2_UnFollowStreamer(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： unfollow
        检查用户unfollow主播功能是否正常
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                        Payload.IOS().ios_unfollow(get_config_data['follow_streamer']))
        with allure.step('检查unfollow 的接口没报错'):
            assert response_json['data']['unfollow']['err'] is None
        with allure.step('检查unfollow主播以后，主播不在用户的following list的接口没报错'):
            following_resp = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                             Payload.IOS().ios_FollowingList(get_config_data['viewer1_username']))
            following_list = following_resp['data']['user']['following']['list']
            print('following_list: ' + str(following_list))
            is_exists = True
            if get_config_data['follow_streamer'] not in following_list:
                is_exists = False
            assert is_exists is False, 'Unfollowing 的主播：automation以后，主播还在关注列表'

    @allure.title('test_ios_followerList')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_followerList(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：FollowersList
        检查用户viewer1_username的粉丝列表

        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        followers_resp = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                         Payload.IOS().ios_FollowersList(get_config_data['viewer1_username']))
        with allure.step('检查粉丝接口没报错'):
            assert 'err' not in followers_resp['data']
        with allure.step('检查关注用户viewer1_username在粉丝列表'):
            followers_list = followers_resp['data']['user']['followers']['list']
            is_exists = False
            for i in followers_list:
                if i['username'] == 'new411':
                    is_exists = True
            assert is_exists is True, '关注主播的用户new411不在主播viewer1_username的粉丝列表'

    @allure.title('test_ios_DonateLemon')
    @allure.severity(allure.severity_level.NORMAL)
    def test_ios_DonateLemon(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： addDonation， fetchMyBalance
        用户viewer1_username给主播automation 打赏， 检查能否正常打赏，打赏后viewer1_username账户的lemon显示正常
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                        Payload.IOS().ios_fetchMyBalance())
        before_balance = response_json['data']['me']['wallet']['balance'][:-5]
        with allure.step('检查打赏前用户的账户lemon是： ' + str(before_balance)):
            print('检查打赏前用户的账户lemon是： ' + str(before_balance))
        donate_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                          Payload.IOS().ios_addDonation(count=1,
                                                        permlink=get_config_data['follow_streamer_permlink']))
        print(donate_json)
        with allure.step('检查给主播automation 打赏1 个lemon接口无报错'):
            assert donate_json['data']['donate']['recentCount'] is 1
            assert donate_json['data']['donate']['expireDuration'] is 0
            assert donate_json['data']['donate']['err'] is None

        response_json1 = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                        Payload.IOS().ios_fetchMyBalance())
        after_balance = response_json1['data']['me']['wallet']['balance'][:-5]
        with allure.step('检查打赏后用户的账户lemon是： ' + str(after_balance)):
            print('检查打赏后用户的账户lemon是： ' + str(after_balance))

        with allure.step('检查打赏后账户剩余的lemon数值正确'):
            assert after_balance + 1 == before_balance


