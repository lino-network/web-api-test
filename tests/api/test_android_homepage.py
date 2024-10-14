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

    @allure.title('test_channel_emote')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_channel_emote(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： ChannelEmote
        检查频道表情接口
        """
        with allure.step('检查 ChannelEmote 接口'):
            streamer_name = "automation"
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_ChannelEmote(streamer_name))

        with allure.step("检查接口返回是否没有错误"):
            assert 'err' not in response_json

        with allure.step("检查返回的 user 对象"):
            user = response_json['data']['user']
            assert user is not None

            emoji = user['emote']
            assert emoji is not None

            with allure.step("检查 emoji 的结构"):
                assert 'vip' in emoji
                assert 'channel' in emoji

                # 检查 VIP 表情列表
                vip_emotes = emoji['vip']['list']
                assert vip_emotes is not None

                if len(vip_emotes) > 0:  # 如果有 VIP 表情，检查每个表情
                    for emote in vip_emotes:
                        assert 'name' in emote and emote['name'] is not None
                        assert 'level' in emote and emote['level'] is not None
                        assert 'type' in emote and emote['type'] is not None
                        assert 'username' in emote and emote['username'] == streamer_name
                        assert 'sourceURL' in emote and emote['sourceURL'] is not None

                # 检查频道表情列表
                channel_emotes = emoji['channel']['list']
                assert channel_emotes is not None

                if len(channel_emotes) > 0:  # 如果有频道表情，检查每个表情
                    for emote in channel_emotes:
                        assert 'name' in emote and emote['name'] is not None
                        assert 'level' in emote and emote['level'] is not None
                        assert 'type' in emote and emote['type'] is not None
                        assert 'username' in emote and emote['username'] == streamer_name
                        assert 'sourceURL' in emote and emote['sourceURL'] is not None


    @allure.title('test_android_Myinfo')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_Myinfo(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： MyInfo
        检查用户信息接口，获取自己的信息，首页每次打开只要缓存自己是登陆状态就会请求，刷新自己的缓存信息
        """
        with allure.step('检查 MyInfo 接口'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_MyInfo())
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 me 对象'):
                me = response_json['data']['me']
                assert me is not None

                required_fields = [
                    'username', 'displayname', 'avatar',
                    'partnerStatus', 'role', 'myChatBadges',
                    'myChatBadgesStr', 'private', 'subCashbacked'
                ]

                for field in required_fields:
                    assert field in me and me[field] is not None, f"{field} should not be None"

                # 检查私有信息字段
                private_info = me['private']
                assert private_info is not None

                private_required_fields = [
                    'accessToken', 'email', 'emailVerified', 'hasSubscribed'
                ]

                for field in private_required_fields:
                    assert field in private_info and private_info[field] is not None, f"{field} should not be None"



    @allure.title('test_android_list_badge_resource')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_list_badge_resource(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： ListBadgeResource
        检查徽章资源列表接口
        """

        with allure.step('检查 ListBadgeResource 接口'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_ListBadgeResource())
            print(response_json)

            with allure.step('检查是否没有错误'):
                assert 'err' not in response_json

            with allure.step('检查返回的 listBadgeResource 对象'):
                badge_resources = response_json['data']['listBadgeResource']
                assert badge_resources is not None  # 确保徽章资源列表不为 None

                with allure.step('检查徽章资源不为空'):
                    assert len(badge_resources) > 0  # 确保徽章资源列表有内容

                with allure.step('检查每个徽章资源的字段'):
                    required_fields = ['description', 'url', 'name']

                    for badge in badge_resources:
                        for field in required_fields:
                            assert field in badge and badge[field] is not None, f"{field} should not be None"

    @allure.title('test_android_my_emoji')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_my_emoji(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： MyEmoji
        检查用户表情接口
        """

        with allure.step("请求 MyEmoji 接口"):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_MyEmoji())
            print(response_json)

        with allure.step('检查是否没有错误'):
            assert 'err' not in response_json

        with allure.step("检查返回的 me 对象"):
            me = response_json['data']['me']
            assert me is not None

            emoji = me['emoji']
            assert emoji is not None

            with allure.step("检查 emoji 的结构"):
                assert 'global' in emoji
                assert 'vip' in emoji

                global_emojis = emoji['global']['list']
                assert global_emojis is not None and len(global_emojis) > 0

                for emote in global_emojis:
                    assert 'name' in emote and emote['name'] is not None

                vip_emojis = emoji['vip']['list']
                assert vip_emojis is not None  # VIP 可以为空列表

    @allure.title('test_android_channel_emoji')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_channel_emoji(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： ChannelEmoji
        检查频道表情接口
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_ChannelEmoji("automation"))
        print(response_json)

        with allure.step('检查是否没有错误'):
            assert 'err' not in response_json

        with allure.step("检查返回的 user 对象"):
            user = response_json['data']['user']
            assert user is not None
            assert user['displayname'] == "automation"
            assert 'isSubscribing' in user

            emoji = user['emoji']
            assert emoji is not None
            assert emoji['vip']['list'] is not None  # 验证 VIP 表情列表存在
            assert len(emoji['vip']['list']) == 3  # 检查 VIP 表情数量是否为 0

    @allure.title('test_android_stream_contributor_query')
    @allure.severity(allure.severity_level.NORMAL)
    def test_android_stream_contributor_query(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： StreamContributorQuery
        检查直播贡献者统计信息接口
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_StreamContributorQuery("automation"))           

        with allure.step('检查接口返回是否没有错误'):
            assert 'err' not in response_json

        with allure.step('检查返回的 user 对象'):
            user = response_json['data']['user']
            assert user is not None

            top_contributions = user['topContributions']
            assert top_contributions is not None

            with allure.step('检查 topContributions 不为空'):
                contributions_list = top_contributions['list']
                assert contributions_list is not None

                # 检查返回的列表长度合法，最多不会超过10个
                assert len(contributions_list) <= 10, f"Expected at most 10 contributions, but got {len(contributions_list)}"

            with allure.step('检查每个贡献的字段'):
                for contribution in contributions_list:
                    assert 'contributor' in contribution and contribution['contributor'] is not None
                    assert 'amount' in contribution and contribution['amount'] is not None

                    contributor = contribution['contributor']
                    required_fields = ['username', 'displayname', 'avatar', 'partnerStatus', 'role']

                    for field in required_fields:
                        assert field in contributor and contributor[field] is not None, f"{field} should not be None"


    @allure.title('test_send_chat_message_with_emoji')
    @allure.severity(allure.severity_level.NORMAL)
    def test_send_chat_message_with_emoji(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： SendSCMsg
        检查发送带表情的聊天消息
        """
        payload = Payload.Android.android_SendSCMsg("automation", "CRY ", ["0", "2"], "Member", False, "")  # 生成 Payload
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_SendSCMsg("automation", "CRY ", [0, 2], "Member", False, ""))  

        with allure.step("检查接口返回是否没有错误"):
            assert 'err' not in response_json

        with allure.step("检查返回的 message 对象"):
            message = response_json['data']['sendStreamchatMessage']['message']
            assert message is not None
            assert message['__typename'] == "ChatText"

            assert message['content'] == "CRY "
            assert message['emojis'] == [0, 2]  # 验证发送的表情有效性


    @allure.title('test_send_chat_message_without_emoji')
    @allure.severity(allure.severity_level.NORMAL)
    def test_send_chat_message_without_emoji(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口： SendSCMsg
        检查发送普通聊天消息
        """
        response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.Android.android_SendSCMsg("automation", "test message", [], "Member", False, "") )  

        with allure.step("检查接口返回是否没有错误"):
            assert 'err' not in response_json

        with allure.step("检查返回的 message 对象"):
            message = response_json['data']['sendStreamchatMessage']['message']
            assert message is not None
            assert message['__typename'] == "ChatText"

            assert message['content'] == "test message"
            assert message['emojis'] == []  # 验证表情为空


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_android_homepage.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')