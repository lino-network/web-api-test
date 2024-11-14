import os
import string
import time
import pytest
from dateutil.relativedelta import relativedelta

import loadData.payloadData as Payload
from datetime import datetime, timedelta
import allure
import tests.common as common


@allure.feature('test_personalHomepage')
class TestLivePage:
    @allure.title('test_ProfileVideos')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ProfileVideos(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：ProfileVideos
        检查个人主页的返回的 video 总数是否正常吗接口是否报错
        :param get_config_data:
        :param get_follow_streamer_auth_header:
        :return:
        """
        video_count = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                      Payload.MyProfileAPI().LivestreamProfileVideo(get_config_data['follow_displayName']))
        with allure.step('获取video 的总视频数'):
            v_count = len(video_count['data']['userByDisplayName']['videos']['list'])
            print('获取video 的总视频数是：' + str(v_count))
        replay_count = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                       Payload.LiveRoomAPI().LivestreamProfileReplay(get_config_data['follow_displayName']))
        with allure.step('获取replay的总视频数'):
            r_count = len(replay_count['data']['userByDisplayName']['pastBroadcastsV2']['list'])
            print('获取replay的总视频数是：' + str(r_count))
        response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.PersonlHomepage().ProfileVideos(get_config_data['follow_displayName']))
        with allure.step('检查接口无报错'):
            assert 'err' not in response['data']['userByDisplayName']
        with allure.step('检查个人主页返回的总的video'):
            personl_count = len(response['data']['userByDisplayName']['centerVideos']['list'])
        with allure.step('检查个人主页显示的video数目是replay+video的总数'):
            assert v_count + r_count == personl_count



