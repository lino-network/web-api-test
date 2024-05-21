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
Video_thumbnailUrl = 'https://images.stg.dlivecdn.com/thumbnail/315f02bf-1424-11ef-a15d-c22d51d48ad0'
video_cateID = 18172  # categoryName: qaTest
video_lan = 1  # language: English
video_comment = 'automationComment' + currentTime


@allure.feature('test_myProfile')
class TestVideoFunction:
    @allure.title('test_uploadVideo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_uploadVideo(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口： VideoPermlink，UploadGeneratePresignUrl
        上传video
        """
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
                                       Payload.MyProfileAPI().UploadGeneratePresignUrl(fileName="mp4", hash=permlinkToken))
            print(url_resp)
            assert url_resp['data']['presignURLGenerate']['err'] is None
            presignURL = url_resp['data']['presignURLGenerate']['presignURL']
            bucketName = presignURL['bucketName']
            key = presignURL['key']
            region = presignURL['url']
        with allure.step('检查上传video是否成功'):
            video_respon = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                           Payload.MyProfileAPI().UploadAddVideo(permlink=permlink,
                                                                                 thumbnailUrl=Video_thumbnailUrl,
                                                                                 title=video_title, content=video_desc,
                                                                                 filename=key,
                                                                                 bucketName=bucketName, region=region,
                                                                                 languageId=video_lan,
                                                                                 categoryId=video_cateID))
            assert video_respon['data']['videoAdd']['err'] is None

    @allure.title('test_LivestreamProfileVideo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_LivestreamProfileVideo(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：LivestreamProfileVideo
        检查上传的video视频能在直播间Video可见
        """
        with allure.step('检查上传的video视频能在直播间Video可见'):
            video_resp = common.get_video_permlink(get_config_data['url'], get_follow_streamer_auth_header,
                                                   Payload.MyProfileAPI().
                                                   LivestreamProfileVideo(get_config_data['follow_streamer']),
                                                   video_title)
            print("上传的video 视频permlink是：" + video_resp)
            assert video_resp is not None

    @allure.title('test_VideoPage')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_VideoPage(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：VideoPage
        检查上传的video 视频信息是否正确
        """
        with allure.step('获取要观看的permlink name'):
            permlink = common.get_video_permlink(get_config_data['url'], get_follow_streamer_auth_header,
                                                 Payload.MyProfileAPI().LivestreamProfileVideo(
                                                     get_config_data['follow_streamer']), video_title)
        if permlink is None:
            assert False, '找不到相应的permlink'
        else:
            with allure.step('进入相应的permlink video 视频页面'):
                resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                       Payload.MyProfileAPI.VideoPage(permlink))
                with allure.step('检查thumbnailUrl是否正确'):
                    assert resp['data']['video']['thumbnailUrl'] == Video_thumbnailUrl, '期望是：' + Video_thumbnailUrl +\
                                                                                     '但是实际是：' + resp['data']['video']['thumbnailUrl']
                with allure.step('检查content是否正确'):
                    assert resp['data']['video']['content'] == video_desc, '期望是：' + video_desc + \
                                                                                        '但是实际是：' + \
                                                                           resp['data']['video']['content']
                with allure.step('检查title是否正确'):
                    assert resp['data']['video']['title'] == video_title, '期望是：' + video_title + \
                                                                                       '但是实际是：' + \
                                                                                       resp['data']['video']['title']
                with allure.step('检查category是否正确'):
                    autul_cate = resp['data']['video']['category']['backendID']
                    assert autul_cate == video_cateID, '期望是：' + autul_cate + '但是实际是：' + resp['data']['video'][
                                                                                           'content']
                with allure.step('检查language是否正确'):
                    autul_lan = resp['data']['video']['language']['id']
                    expect_lan = 'language:' + str(video_lan)
                    assert autul_lan == expect_lan, '期望是：' + expect_lan + '但是实际是：' + autul_lan

    @allure.title('test_AddWatch')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_AddWatch(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：AddWatch
        检查video 视频AddWatch接口不报错
        """
        with allure.step('获取要观看的permlink name'):
            permlink = common.get_video_permlink(get_config_data['url'], get_follow_streamer_auth_header,
                                                 Payload.MyProfileAPI().LivestreamProfileVideo(
                                                     get_config_data['follow_streamer']), video_title)
        if permlink is None:
            assert False, '找不到相应的permlink'
        else:
            with allure.step('检查video 视频AddWatch接口不报错'):
                add_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                           Payload.MyProfileAPI.AddWatch(permlink))
                assert add_resp['data']['watch']['err'] is None

    @allure.title('test_AddVideoComment')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_AddVideoComment(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：AddComment
        在video 视频下面添加comment
        """
        with allure.step('获取要评论的permlink name'):
            permlink = common.get_video_permlink(get_config_data['url'], get_follow_streamer_auth_header,
                                                 Payload.MyProfileAPI().LivestreamProfileVideo(
                                                     get_config_data['follow_streamer']), video_title)
        if permlink is None:
            assert False, '找不到相应的permlink'
        else:
            with allure.step('在video 视频下面添加comment'):
                add_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                           Payload.MyProfileAPI.AddComment(permlink, video_comment))
                with allure.step('检查接口不报错'):
                    assert add_resp['data']['comment']['err'] is None
                with allure.step('检查添加的comment正确'):
                    assert add_resp['data']['comment']['comment']['content'] == video_comment
                with allure.step('检查返回的comment permlink不为空'):
                    assert add_resp['data']['comment']['comment']['permlink'] is not None

    @allure.title('test_AddCommentVote')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_AddCommentVote(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：AddCommentVote
        检查vote评论是是否正确
        """
        with allure.step('获取要评论的permlink name'):
            permlink = common.get_video_permlink(get_config_data['url'], get_follow_streamer_auth_header,
                                                 Payload.MyProfileAPI().LivestreamProfileVideo(
                                                     get_config_data['follow_streamer']), video_title)
        if permlink is None:
            assert False, '找不到相应的permlink'
        else:
            with allure.step('获取要vote的评论的permlink'):
                comment_list_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                                    Payload.MyProfileAPI.VideoPage(permlink))
                comment_list = comment_list_resp['data']['video']['comments']['list']
                is_comment_exist = False
                for i in comment_list:
                    if i['content'] == video_comment:
                        comment_permlink = i['permlink']
                        is_comment_exist = True
                        break
                if is_comment_exist:
                    with allure.step('Down vote的评论'):
                        resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                               Payload.MyProfileAPI().AddCommentVote(comment_permlink, 'Down'))
                        assert resp['data']['commentVote']['err'] is None
                    with allure.step('Up vote的评论'):
                        resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                               Payload.MyProfileAPI().AddCommentVote(comment_permlink, 'Up'))
                        assert resp['data']['commentVote']['err'] is None

    @allure.title('test_DeleteVideoComment')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_DeleteVideoComment(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：DeleteVideoComment
        在video 视频下面删除comment
        """
        with allure.step('获取要评论的permlink name'):
            permlink = common.get_video_permlink(get_config_data['url'], get_follow_streamer_auth_header,
                                                 Payload.MyProfileAPI().LivestreamProfileVideo(
                                                     get_config_data['follow_streamer']), video_title)
        if permlink is None:
            assert False, '找不到相应的permlink'
        else:
            with allure.step('获取要删除的评论的permlink'):
                comment_list_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                                    Payload.MyProfileAPI.VideoPage(permlink))
                comment_list = comment_list_resp['data']['video']['comments']['list']
                is_comment_exist = False
                for i in comment_list:
                    if i['content'] == video_comment:
                        comment_permlink = i['permlink']
                        is_comment_exist = True
                        break
                if is_comment_exist:
                    delete_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                                  Payload.MyProfileAPI.DeleteVideoComment(comment_permlink, permlink))
                    with allure.step('检查是否成功删除评论'):
                        assert delete_resp['data']['deleteVideoComment']['err'] is None
                else:
                    assert False, '找不到该评论'

    @allure.title('test_DeleteVideo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_DeleteVideo(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：DeleteVideo
        删除Video
        """
        with allure.step('获取要删除的permlink name'):
            resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header, Payload.MyProfileAPI().
                                   LivestreamProfileVideo(get_config_data['follow_streamer']))
            permlink_list = resp['data']['userByDisplayName']['videos']['list']
            is_link = False
            for link in permlink_list:
                if link['title'] == video_title:
                    permlink_name = link['permlink']
                    is_link = True
                    assert True
                    break
            if is_link is False:
                assert False, '找不到相应的video 视频'
        with allure.step('检查能否成功删除Video'):
            delete_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                          Payload.MyProfileAPI().DeleteVideo(permlink_name))
            assert delete_resp['data']['videoDelete']['err'] is None
            time.sleep(30)
        with allure.step('检查删除Video以后直播间不显示改video视频'):
            after_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header, Payload.MyProfileAPI().
                                         LivestreamProfileVideo(get_config_data['follow_streamer']))
            video_list = after_resp['data']['userByDisplayName']['videos']['list']
            for video in video_list:
                print(str(video['permlink']))
                if video['permlink'] == permlink_name:
                    print('删除后该video视频还存在')
                    assert False

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





