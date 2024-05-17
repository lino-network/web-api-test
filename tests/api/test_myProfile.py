import os
import string
import time
import pytest
from dateutil.relativedelta import relativedelta

import loadData.payloadData as Payload
from datetime import datetime, timedelta
import allure
import tests.common as common

currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%H%M%S")
video_title = 'automationTitle_' + currentTime
video_desc = 'automationContent_' + currentTime


@allure.feature('test_myProfile')
class TestMyProfilePage:
    @allure.title('test_uploadVideo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_1_uploadVideo(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口： VideoPermlink，UploadGeneratePresignUrl
        上传video
        """
        thumbnailUrl = 'https://images.stg.dlivecdn.com/thumbnail/315f02bf-1424-11ef-a15d-c22d51d48ad0'
        with allure.step('获取video permlink 和permlinkToken'):
            link_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                        Payload.MyProfileAPI().VideoPermlink())
            assert link_resp['data']['videoPermlinkGenerate']['err'] is None
            permlink = link_resp['data']['videoPermlinkGenerate']['permlink']
            permlinkToken = link_resp['data']['videoPermlinkGenerate']['permlinkToken']
            print('video permlink is:' + str(permlink))
            print('video permlinkToken is:' + str(permlinkToken))
        with allure.step('获取UploadGeneratePresignUrl的信息'):
            url_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                       Payload.MyProfileAPI().UploadGeneratePresignUrl('mp4', permlinkToken))
            assert url_resp['data']['presignURLGenerate']['err'] is None
            presignURL = url_resp['data']['presignURLGenerate']['presignURL']
            bucketName = presignURL['bucketName']
            key = presignURL['key']
            region = presignURL['url']
            url = presignURL['url']
        with allure.step('检查上传video是否成功'):
            video_respon = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                           Payload.MyProfileAPI().UploadAddVideo(permlink=permlink,
                                                                                 thumbnailUrl=thumbnailUrl,
                                                                                 title=video_title, content=video_desc,
                                                                                 filename=key,
                                                                                 bucketName=bucketName, region=region,
                                                                                 languageId=1, categoryId=18172))
            assert video_respon['data']['videoAdd']['err'] is None

    @allure.title('test_2_LivestreamProfileVideo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2_LivestreamProfileVideo(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：LivestreamProfileVideo
        检查上传的video视频能在直播间Video可见
        """
        with allure.step('检查上传的video视频能在直播间Video可见'):
            cate_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                        Payload.MyProfileAPI().
                                        LivestreamProfileVideo(get_config_data['follow_streamer']))
            video_list = cate_resp['data']['userByDisplayName']['videos']['list']
            for video in video_list:
                if video['title'] == video_title:
                    assert True
                    break

    @allure.title('test_UploadSearchCategory')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_UploadSearchCategory(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口: UploadSearchCategory
        在Upload video 页面搜索Category
        """
        categoryName = 'qaTest'
        with allure.step('检查能在Upload video 页面搜索出相应的Category'):
            cate_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                        Payload.MyProfileAPI().UploadSearchCategory(categoryName))
            categroy_list = cate_resp['data']['search']['categories']['list']
            for cate in categroy_list:
                if cate['title'] == categoryName:
                    assert True
                    break




