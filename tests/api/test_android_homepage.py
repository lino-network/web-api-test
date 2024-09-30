import json
import os
import pytest
import requests
import loadData.payloadData as Payload
from datetime import datetime, timedelta
import allure
import tests.common as common


@allure.feature('test_android_homepage')
class TestAndroidHomePage:
    @allure.title('test_android_live_carousel')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_live_carousel(self, get_config_data, api_headers):
        """
        接口： LiveCarousel
        检查首页轮播接口
        """
        with allure.step('检查 LiveCarousel 接口'):
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.Android.android_LiveCarousel())
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 liveCarousel 对象'):
                live_carousel = response_json['data']['liveCarousel']
                assert live_carousel is not None

                with allure.step('检查 carousel list 不为空'):
                    assert live_carousel['list'] is not None and len(live_carousel['list']) > 0

                with allure.step('检查每个 carousel 的字段'):
                    for carousel in live_carousel['list']:
                        assert 'id' in carousel
                        assert 'position' in carousel
                        assert 'live' in carousel and carousel['live'] is not None

                        # 检查 live 对象内的字段
                        live = carousel['live']
                        required_fields = ['thumbnailUrl', 'title', 'watchingCount', 'totalReward', 'category', 'tags', 'creator']

                        for field in required_fields:
                            assert field in live and live[field] is not None, f"{field} should not be None"

                        # Check category and creator fields
                        category = live['category']
                        assert 'title' in category and category['title'] is not None
                        assert 'id' in category and category['id'] is not None

                        creator = live['creator']
                        assert 'username' in creator and creator['username'] is not None
                        assert 'displayname' in creator and creator['displayname'] is not None
                        assert 'avatar' in creator and creator['avatar'] is not None
                        assert 'partnerStatus' in creator and creator['partnerStatus'] is not None
                        assert 'role' in creator and creator['role'] is not None

    @allure.title('test_android_streams_query')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_streams_query(self, get_config_data, api_headers):
        """
        接口： StreamsQuery
        检查直播流接口
        """
        with allure.step('检查 StreamsQuery 接口'):
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.Android.android_StreamsQuery())
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 livestreams 对象'):
                livestreams = response_json['data']['livestreams']
                assert livestreams is not None

                # 检查 pageInfo 对象
                page_info = livestreams['pageInfo']
                assert 'endCursor' in page_info
                assert 'hasNextPage' in page_info

                with allure.step('检查返回的 list 不为空'):
                    assert livestreams['list'] is not None and len(livestreams['list']) > 0

                with allure.step('检查每个 livestream 是否有效'):
                    for livestream in livestreams['list']:
                        assert 'thumbnailUrl' in livestream and livestream['thumbnailUrl'] is not None
                        assert 'title' in livestream and livestream['title'] is not None
                        assert 'watchingCount' in livestream and livestream['watchingCount'] is not None
                        assert 'totalReward' in livestream and livestream['totalReward'] is not None
                        assert 'category' in livestream and livestream['category'] is not None
                        assert 'tags' in livestream  # tags 可以是空数组
                        assert 'creator' in livestream and livestream['creator'] is not None

                        # 检查 creator 字段的有效性
                        creator = livestream['creator']
                        assert 'username' in creator and creator['username'] is not None
                        assert 'displayname' in creator and creator['displayname'] is not None
                        assert 'avatar' in creator and creator['avatar'] is not None
                        assert 'partnerStatus' in creator and creator['partnerStatus'] is not None
                        assert 'role' in creator and creator['role'] is not None

    @allure.title('test_android_categories_query')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_categories_query(self, get_config_data, api_headers):
        """
        接口： CategoriesQuery
        检查分类接口
        """
        with allure.step('检查 CategoriesQuery 接口'):
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.Android.android_CategoriesQuery())
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 categories 对象'):
                categories = response_json['data']['categories']
                assert categories is not None

                # 检查 list 不为空
                category_list = categories['list']
                assert category_list is not None and len(category_list) > 0

                with allure.step('检查每个 category 的字段'):
                    required_fields = ['backendID', 'title', 'imgUrl', 'watchingCount']

                    for category in category_list:
                        for field in required_fields:
                            assert field in category and category[field] is not None, f"{field} should not be None"

                        # 对于 category 内的 parent 字段检查
                        if 'parent' in category:
                            parent = category['parent']
                            assert 'id' in parent and parent['id'] is not None


    @allure.title('test_user_post')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_user_post(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： UserPost
        检查用户信息接口
        """
        payload = Payload.Android.android_UserPost("automation") 

        with allure.step('检查 UserPost 接口'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_UserPost("automation"))
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 userByDisplayName 对象'):
                user = response_json['data']['userByDisplayName']
                assert user is not None

                required_fields = [
                    'username', 'displayname', 'avatar', 
                    'partnerStatus', 'role', 'myRoomRole', 
                    'bttReceiverAddress', 'followers'
                ]

                for field in required_fields:
                    assert field in user and user[field] is not None, f"{field} should not be None"

                # 检查 followers 的 totalCount 字段
                assert 'followers' in user and 'totalCount' in user['followers']
                assert user['followers']['totalCount'] is not None

                with allure.step('检查私有信息是否存在'):
                    assert 'private' in user
                    assert user['private'] is None  # 例如，这里验证 'private' 如果应该为 None

                # 检查直播字段
                livestream = user.get('livestream', None)
                if livestream:
                    assert 'permlink' in livestream and livestream['permlink'] is not None
                    assert 'thumbnailUrl' in livestream and livestream['thumbnailUrl'] is not None
                    assert 'title' in livestream and livestream['title'] is not None
                    assert 'watchingCount' in livestream and livestream['watchingCount'] is not None
                    assert 'totalReward' in livestream and livestream['totalReward'] is not None
                    assert 'language' in livestream and 'language' in livestream['language']
                    assert 'category' in livestream and 'title' in livestream['category']

    @allure.title('test_android_user_panel')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_user_panel(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： UserPanel
        检查用户面板信息接口
        """
        streamer_name = "automation"  # 使用的主播名称
        with allure.step('检查 UserPanel 接口'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                Payload.Android.android_UserPanel(streamer_name))
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 userByDisplayName 对象'):
                user = response_json['data']['userByDisplayName']
                assert user is not None

                panels = user['panels']
                assert panels is not None  # 检查面板列表的有效性

                #with allure.step('检查 panels 不为空'):
                    #assert len(panels) > 0
                
                with allure.step('检查每个 panel 的字段'):
                    required_fields = ['title', 'imageURL', 'imageLinkURL', 'body']

                    for panel in panels:
                        for field in required_fields:
                            assert field in panel and panel[field] is not None, f"{field} should not be None"


    @allure.title('test_channel_emote')
    @allure.severity(allure.severity_level.NORMAL)
    def test_channel_emote(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： ChannelEmote
        检查频道表情接口
        """
        with allure.step('检查 ChannelEmote 接口'):
            streamer_name = "automation"
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_ChannelEmote(streamer_name))
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 user 对象'):
                user = response_json['data']['user']
                assert user is not None

                emote = user['emote']
                assert emote is not None

                with allure.step('检查 emote 中的 vip 和 channel 是否都存在'):
                    assert 'vip' in emote
                    assert 'channel' in emote

                    # 检查 vip 的列表
                    vip_emotes = emote['vip']['list']
                    assert vip_emotes is not None
                    assert len(vip_emotes) > 0  # 确保不为空

                    # 检查 channel 的列表
                    channel_emotes = emote['channel']['list']
                    assert channel_emotes is not None
                    assert len(channel_emotes) > 0  # 确保不为空

                    # 验证 vip emote 的字段
                    for emote_item in vip_emotes:
                        assert 'name' in emote_item and emote_item['name'] is not None
                        assert 'level' in emote_item and emote_item['level'] is not None
                        assert 'type' in emote_item and emote_item['type'] is not None
                        assert 'username' in emote_item and emote_item['username'] == streamer_name
                        assert 'sourceURL' in emote_item and emote_item['sourceURL'] is not None

                    # 验证 channel emote 的字段
                    for emote_item in channel_emotes:
                        assert 'name' in emote_item and emote_item['name'] is not None
                        assert 'level' in emote_item and emote_item['level'] is not None
                        assert 'type' in emote_item and emote_item['type'] is not None
                        assert 'username' in emote_item and emote_item['username'] == streamer_name
                        assert 'sourceURL' in emote_item and emote_item['sourceURL'] is not None


    @allure.title('test_android_SCMessages')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_SCMessages(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： UserPost
        检查用户信息接口
        """
        with allure.step('检查 SCMessages 接口'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_SCMessages("automation"))
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 user 对象'):
                user = response_json['data']['user']
                assert user is not None

                # 检查 chats 的有效性
                chats = user['chats']
                assert chats is not None

                with allure.step('检查 chats 不为空'):
                    assert len(chats) > 0

                # 检查每条聊天信息的有效性
                for chat in chats:
                    #assert 'id' in chat
                    assert 'type' in chat

                    # 检查特定类型（ChatText)是否有必要字段
                    if chat['__typename'] == 'ChatText':
                        assert 'content' in chat and chat['content'] is not None
                        assert 'sender' in chat and chat['sender'] is not None

                        # 检查 sender 的字段
                        sender = chat['sender']
                        assert 'username' in sender and sender['username'] is not None
                        assert 'displayname' in sender and sender['displayname'] is not None
                        assert 'avatar' in sender and sender['avatar'] is not None

                    # 其他聊天类型（如 ChatGift、ChatFollow 等），可以在这里检查是否有特定逻辑需要进行验证

    @allure.title('test_android_total_contributor_query')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_total_contributor_query(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： TotalContributorQuery
        检查用户贡献者统计信息接口
        """
        with allure.step('检查 TotalContributorQuery 接口'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_TotalContributorQuery("automation"))
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 user 对象'):
                user = response_json['data']['user']
                assert user is not None

                top_contributions = user['topContributions']
                assert top_contributions is not None

                with allure.step('检查 topContributions 不为空'):
                    contribution_list = top_contributions['list']
                    assert contribution_list is not None and len(contribution_list) > 0

                # 检查每个 contribution 的字段
                with allure.step('检查每个贡献的字段'):
                    for contribution in contribution_list:
                        assert 'contributor' in contribution and contribution['contributor'] is not None
                        assert 'amount' in contribution and contribution['amount'] is not None
                        
                        contributor = contribution['contributor']
                        required_fields = ['username', 'displayname', 'avatar', 'partnerStatus', 'role']

                        for field in required_fields:
                            assert field in contributor and contributor[field] is not None, f"{field} should not be None"


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_android_homepage.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')