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
    def test_user_post(self, get_config_data, get_viewer1_login_auth_header):
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

if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_android_homepage.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')