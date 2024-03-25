import os
import string
import time
import pytest
from dateutil.relativedelta import relativedelta

import loadData.payloadData as Payload
from datetime import datetime, timedelta
import allure
import tests.common as common


@allure.feature('test_categoryAndMatureTag')
class TestCategoryAndMatureTagPage:
    @allure.title('test_userHadClick18+')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_userHadClick18Popup(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：CheckMaturePopupClosedByUsername
        检查已经点击过18+ 的用户进入Mature 的直播间没有18+ 的弹框
        """
        with allure.step("检查已经点击过18+ 的用户进入Mature 的直播间没有18+ 的弹框"):
            resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.MatureRelatedAPI().CheckMaturePopupClosedByUsername(
                                       get_config_data['follow_streamer']))
            data = resp['data']['checkMaturePopupClosedByUsername']
            assert data['isClosed'] is True, '检查已经点击过18+ 的用户进入Mature 的直播间还是有18+ 的弹框'
            assert data['err'] is None, '点击过18+ 的用户，报错信息是： ' + data['err']

    @allure.title('test_userNeverClick18Popup+')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_userNeverClick18Popup(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：CheckMaturePopupClosedByUsername
        检查没有点击过18+ 的用户进入Mature 的直播间有18+ 的弹框
        """
        with allure.step("检查没有点击过18+ 的用户进入Mature 的直播间有18+ 的弹框"):
            resp = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                   Payload.MatureRelatedAPI().CheckMaturePopupClosedByUsername(
                                       get_config_data['viewer1_username']))
            data = resp['data']['checkMaturePopupClosedByUsername']
            assert data['isClosed'] is False, '没有点击过18+ 的用户，进入Mature 的直播间没有18+ 的弹框'
            assert data['err'] is None, '没有点击过18+ 的用户，报错信息是： ' + data['err']

    @allure.title('test_StreamerTagIsMatureInMatureCategory+')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_StreamerTagIsMatureInMatureCategory(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口: CategoryLivestreamsPage
        检查Tag是content tag的主播在Mature category下面
        """
        with allure.step("检查Tag是mature content tag的主播在Mature category下面"):
            resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.HomePageAPI().homepage_category_live_stream_page('-1'))
            streamer_list = resp['data']['livestreams']['list']
            for i in streamer_list:
                if i['creator']['username'] == get_config_data['follow_streamer']:
                    assert True, 'mature content tag的主播不在Mature category下面'
                    break

    @allure.title('test_streamerInWeb3GamesAlsoInGamesAndCryptoCategory+')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_streamerInWeb3GamesAlsoInGamesAndCryptoCategory(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口: CategoryLivestreamsPage
        检查属于web3 Games的主播同样属于Games和Crypto
        """
        with allure.step("检查automation这个直播间是否在Web3 Games 这个category下面"):
            resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.HomePageAPI().homepage_category_live_stream_page('-4'))
            streamer_list = resp['data']['livestreams']['list']
            is_InWeb3 = False
            for i in streamer_list:
                if i['creator']['username'] == get_config_data['follow_streamer']:
                    is_InWeb3 = True
                    assert True, 'mature content tag的主播不在Mature category下面'
                    with allure.step("检查automation这个直播间是否在Games这个category下面"):
                        resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                               Payload.HomePageAPI().homepage_category_live_stream_page('-3'))
                        streamer_list1 = resp['data']['livestreams']['list']
                        is_game = False
                        for j in streamer_list1:
                            if j['creator']['username'] == get_config_data['follow_streamer']:
                                assert True, 'mature content tag的主播不在Mature category下面'
                                is_game = True
                                break
                    with allure.step("检查automation这个直播间是否在Crypto这个category下面"):
                        resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                               Payload.HomePageAPI().homepage_category_live_stream_page('-5'))
                        streamer_list2 = resp['data']['livestreams']['list']
                        is_crypto = False
                        for a in streamer_list2:
                            if a['creator']['username'] == get_config_data['follow_streamer']:
                                assert True, 'mature content tag的主播不在Crypto category下面'
                                is_crypto = True
                                break
                    break
            if not is_InWeb3:
                assert False, '检查automation这个直播间不在Web3 Games 这个category下面'
            if not is_game:
                assert False, '检查automation这个直播间不在Games这个category下面'
            if not is_crypto:
                assert False, '检查automation这个直播间不在Crypto这个category下面'




