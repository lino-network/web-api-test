import json
import os
import pytest
import requests
import loadData.payloadData as Payload
import allure
import tests.common as common


@allure.feature('test_homepage')
class TestHomePage:
    @allure.title('test_homepage_carousels')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_carousels(self, get_config_data, api_headers):  # 轮播检查
        """
        接口： HomePageCarousels

        检查轮播接口
        """
        with allure.step('检查轮播接口'):
            response_json = common.api_post(get_config_data['url'], api_headers,
                                            Payload.HomePageAPI().LiveCarousel())
            print(response_json)
            with allure.step('检查轮播的位置是否为5'):
                assert int(response_json['data']['liveCarousel']['totalCount']) == 5
            with allure.step('检查轮播接口的返回值不包含err '):
                assert 'err' not in response_json

    @allure.title('test_homepage_livestream')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_livestream(self, get_config_data, api_headers):  # 画廊直播间检查
        """
        接口： HomePageLivestream

        检查首页直播流接口
        """
        with allure.step('检查首页直播流接口'):
            response_json = common.api_post(get_config_data['url'], api_headers,
                                            Payload.HomePageAPI().homepage_livestream())
            print(response_json)
            with allure.step('检查轮播接口的返回值不为空 '):
                assert len(response_json['data']['livestreams']['list']) is not None
            with allure.step('检查轮播接口的返回值不包含err '):
                assert 'err' not in response_json

    @allure.title('test_homepage_categories')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_categories(self, get_config_data, api_headers):  # 检查cate分类列表
        """
        接口： homepage_categories

        """
        with allure.step('检查频道分类列表'):
            response_json = common.api_post(get_config_data['url'], api_headers,
                                            Payload.HomePageAPI().homepage_categories())

        categories_list = response_json['data']['categories']['list']

        # 确保 list 不为空
        assert categories_list, 'Categories list is empty'

        # 检查每一项是否有数据
        for category in categories_list:
            assert category['id'], 'Category ID is None'
            assert category['backendID'] is not None, 'Category backendID is None'
            assert category['title'], 'Category title is None'
            assert category['imgUrl'], 'Category imgUrl is None'
            assert category['watchingCount'] is not None, 'Category watchingCount is None'
            assert category['__typename'], 'Category __typename is None'



    @allure.title('test_homepage_list_recommendation')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_list_recommendation(self, get_config_data, api_headers):  # 推荐系统
        """
        接口： HomePageListRecommendation

        检查主页推荐系统
        """
        with allure.step('检查主页推荐系统 '):
            response_json = common.api_post(get_config_data['url'], api_headers,
                                            Payload.HomePageAPI().homepage_list_recommendation())
            print(response_json)
            data = response_json.get('data')
            home_page_list_recommendation = data.get('listRecommendation')
            print(home_page_list_recommendation)
            with allure.step('检查数据不为空'):
                assert home_page_list_recommendation is not None
            with allure.step('检查数据无报错'):
                assert 'err' not in data

    @allure.title('test_homepage_global_information_recommend')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_global_information_recommend(self, get_config_data, api_headers):  # 主页左边的推荐列表
        """
        接口：GlobalInformationRecommend

        主页左边的推荐列表
        """
        with allure.step("主页左边的推荐列表"):
            response_json = common.api_post(get_config_data['url'], api_headers,
                                            Payload.HomePageAPI().homepage_global_information_recommend())
            # 判断 recommendChannels 数组是否为空
            recommend_channels = response_json['data']['globalInfo']['recommendChannels']
            with allure.step('检查数据不为空'):
                assert len(recommend_channels) > 0
            with allure.step('检查数据无报错'):
                assert 'err' not in response_json['data']

    @allure.title('test_homepage_global_information_register_recommend')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_global_information_register_recommend(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：GlobalInformationRegisterRecommend

        """
        with allure.step("新注册用户推荐4个频道"):
            response_json = requests.post(get_config_data['url'], headers=get_follow_streamer_auth_header,
                                 json=Payload.HomePageAPI().homepage_global_information_register_recommend())
            
            response_data = response_json.json()
            recommend_channels = response_data['data']['globalInfo']['recommendChannels']

        # 确保推荐用户数量为 4
        assert len(recommend_channels) == 4, f"Expected 4 recommend channels, but got {len(recommend_channels)}"

        # 检查每个用户的内容
        for channel in recommend_channels:
            user = channel['user']
            assert user['id'], 'User ID is None'
            assert user['displayname'], 'User displayname is None'
            assert user['partnerStatus'], 'User partnerStatus is None'
            assert user['__typename'], 'User __typename is None'
            assert user['avatar'], 'User avatar is None'
            assert user['followers']['totalCount'] is not None, 'User followers totalCount is None'
            assert user['followers']['__typename'], 'User followers __typename is None'
            assert user['username'], 'User username is None'
            assert user['isFollowing'] is not None, 'User isFollowing is None'
            assert user['isMe'] is not None, 'User isMe is None'

    @allure.title('test_homepage_nav_search_result')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_nav_search_result(self, get_config_data, api_headers):
        """
        接口： NavSearchResult

        搜索关键字： automation
        检查首页搜索功能
        """
        with allure.step('检查首页搜索功能'):
            data = common.api_post(get_config_data['url'], api_headers,
                                   Payload.HomePageAPI().homepage_nav_search_result("automation"))
            # 解析返回结果
            print(data)
            users = data['data']['search']['allUsers']['list']
            print(users)

            with allure.step('检查搜索结果是否包含"automation"'):
                found_user = False
                for user in users:
                    if user['creator']['displayname'] == 'automation':
                        found_user = True
                        break
                assert found_user is True

    @allure.title('test_homepage_nav_search_category')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_nav_search_category(self, get_config_data, api_headers):
        """
        接口： NavSearchResult

        搜索关键字： automation
        检查首页搜索功能
        """
        response = requests.post(get_config_data['url'], headers=api_headers,
                                 json=Payload.HomePageAPI().homepage_nav_search_result("Web3 Games"))
        assert response.status_code == 200
        # 解析返回结果
        data = json.loads(response.text)

        # 检查返回的数据中的"search"字段是否为字典类型
        assert isinstance(data["data"]["search"], dict), "'search' field is not a dictionary"

        # 检查返回的数据中的"liveCategories"字段是否为字典类型
        assert isinstance(data["data"]["search"]["liveCategories"], dict), "'liveCategories' field is not a dictionary"

        # 检查返回的数据中的"liveCategories"字段中的"list"字段是否为列表类型
        assert isinstance(data["data"]["search"]["liveCategories"]["list"], list), "'list' field is not a list"

        # 获取分类列表
        categories = data["data"]["search"]["liveCategories"]["list"]
        print(categories)
        # 检查是否存在"title": "Web3 Games"
        found_category = False
        for category in categories:
            if category.get("title") == "Web3 Games":
                found_category = True
                break

        # 检查结果
        assert found_category == True, "Category 'Web3 Games' not found"

    @allure.title('test_me_global')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_me_global(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口: MeGlobal

        测试用户: 66@nqmo.com/password
        检查用户global信息
        """
        data = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                               Payload.me_global())
        print(data)
        with allure.step('检查用户ID是否正确'):
            assert data['data']['me']['id'] == 'user:dlive-degnujtptx', "User ID is incorrect"

        with allure.step('检查用户名是否正确'):
            assert data['data']['me']['displayname'] == 'automation_viewer1', "User displayname is incorrect"

        with allure.step('检查用户余额是否为0'):
            assert data['data']['me']['wallet']['balance'] != 0, "User balance is 0"

        with allure.step('检查用户头像URL是否正确'):
            assert data['data']['me'][
                       'avatar'] == 'https://images.stg.dlivecdn.com/avatar/c1e413da-aec2-11ee-acb9-4aed4c90c80a', \
                "Avatar URL is incorrect"

        with allure.step('检查用户角色是否为None'):
            assert data['data']['me']['role'] == 'None', "User role is not None"

    @allure.title('test_live_streams_languages')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_live_streams_languages(self, get_config_data, api_headers):
        """
        接口： LivestreamsLanguages

        """
        response = requests.post(get_config_data['url'], headers=api_headers,
                                 json=Payload.live_streams_languages())
        assert response.status_code == 200
        # 解析返回结果
        data = json.loads(response.text)
        print(data)

        # 检查返回的数据中的"languages"列表是否包含至少一个元素
        assert len(data["data"]["languages"]) > 0, "'languages' list is empty"

        # 检查返回的数据中的每个语言对象是否包含"id"、"backendID"、"language"和"code"字段
        for language in data["data"]["languages"]:
            assert "id" in language, "Language object does not contain 'id' field"
            assert "backendID" in language, "Language object does not contain 'backendID' field"
            assert "language" in language, "Language object does not contain 'language' field"
            assert "code" in language, "Language object does not contain 'code' field"

        # with allure.step('检查用户邮箱是否已验证'):
        #     assert data['data']['me']['private']['emailVerified'] == True, "Email is not verified"
        #
        # with allure.step('检查用户语言设置是否为英文'):
        #     assert data['data']['me']['private']['language'] == 'en', "Language is not English"

    @allure.title('test_me_balance')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_me_balance(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口: MeBalance

        用户: viewer1_username 
        """
        response = common.api_post(get_config_data['url'], get_viewer1_login_auth_header, Payload.test_me_balance())
        print(response)

        assert response["data"]["me"]["wallet"]["balance"] is not None
        assert response['data']['me']['id'] == 'user:dlive-degnujtptx', "Username is incorrect"

    @allure.title('test_me_rebillycards')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_me_rebillyCards(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口: MeRebillyCards

        用户:  automation
        """
        response = common.api_post(get_config_data['url'], get_viewer1_login_auth_header, Payload.MeRebillyCards())
        print(response)
        assert response["data"]["me"]["id"] == 'user:dlive-degnujtptx'
        assert response["data"]["me"]["private"]["userRebillyCards"] == []

    # @allure.title('test_activity_user_donation_rank')
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_activity_user_donation_rank(self, get_config_data, api_headers):
    #     """
    #     接口: ActivityUserDonationRank

    #     用户:  automation
    #     """
    #     response = requests.post(get_config_data['url'], headers=api_headers,
    #                      json=Payload.ActivityUserDonationRank(
    #                          get_config_data['follow_streamer'], 'THIS_WEEK'))
    #     assert response.status_code == 200

    #     data = response.json()
    #     print(data)  # 添加调试语句以查看获取的JSON数据

    #     assert data is not None  # 确保成功获取JSON数据

    #     assert data["data"]["userDonationRank"]["rank"] is not None
    #     assert data["data"]["userDonationRank"]["user"]["displayname"] == 'automation'
    @allure.title('test_browse_page_search_category')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_browse_page_search_category(self, get_config_data, api_headers):
        """
        接口: BrowsePageSearchCategory

        用户:  automation
        步骤:  category点击show all        
        """
        response = requests.post(get_config_data['url'], headers=api_headers,
                                 json=Payload.HomePageAPI().homepage_browse_page_search_category(""))
        # assert response.status_code == 200 
        data = json.loads(response.text)
        assert data["data"]["search"]["trendingCategories"]["list"] is not None

        response_search = requests.post(get_config_data['url'], headers=api_headers,
                                        json=Payload.HomePageAPI().homepage_browse_page_search_category("Web3"))
        assert response_search.status_code == 200
        data_search = json.loads(response_search.text)
        print(data_search)
        category_list = data_search["data"]["search"]["trendingCategories"]["list"]
        cate_exists = False
        for i in category_list:
            if i["title"] == "Web3 Games":
                cate_exists = True
                break
        assert cate_exists == True, '搜索的category不存在'

    @allure.title('test_live_streams_languages')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_live_streams_languages(self, get_config_data, api_headers):
        """
        接口: BrowsePageSearchCategory

        用户:  automation
        步骤:  category点击show all        
        """
        response = requests.post(get_config_data['url'], headers=api_headers,
                                 json=Payload.live_streams_languages())
        assert response.status_code == 200
        data = json.loads(response.text)
        print(data)
        assert data["data"]["languages"][0]["id"] is not None
        assert data["data"]["languages"][0]["language"] == "All"

    @allure.title('test_homepage_category_live_stream_page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_category_live_stream_pages(self, get_config_data, api_headers):
        """
        接口: CategoryLivestreamsPage

        步骤:  category点击games       
        """
        response = common.api_post(get_config_data['url'], api_headers,
                                   Payload.HomePageAPI().homepage_category_live_stream_page(
                                       get_config_data['streamer_category_id']))
        print(response)
        streamer_list = response["data"]["livestreams"]["list"]
        with allure.step("检查automation这个直播间是否在category: Web3 Games下面"):
            streamerExist = False
            for i in streamer_list:
                print(i['permlink'])
                if get_config_data['follow_streamer'] in i['permlink']:
                    print(streamerExist)
                    streamerExist = True
                    if streamerExist:
                        with allure.step("检查category是否显示正确"):
                            assert i['category']['id'] == "category:" + str(get_config_data['streamer_category_id'])
                            assert i['title'] == "Automation test"
                    break
            assert streamerExist == True, 'automation这个直播间不在category: Web3 Games下面'

    @allure.title('test_IsUserVerifyEmailButNoPwd')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_IsUserVerifyEmailButNoPwd(self, get_config_data, get_follow_streamer_auth_header):  # 检查用户邮箱验证
        """
        接口： IsUserVerifyEmailButNoPwd

        检查是否验证邮箱接口
        步骤： 登录
        """
        response = requests.post(get_config_data['url'], headers=get_follow_streamer_auth_header,
                                 json=Payload.LoginAPI().IsUserVerifyEmailButNoPwd(get_config_data['follow_streamer']))
        assert response.status_code == 200
        data = json.loads(response.text)
        is_user_verify_email_but_no_pwd = data["data"]["IsUserVerifyEmailButNoPwd"]["isUserVerifyEmailButNoPwd"]
        assert is_user_verify_email_but_no_pwd is False, "'isUserVerifyEmailButNoPwd' is not False."

    @allure.title('test_isFirstThirdLogin')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_isFirstThirdLogin(self, get_config_data, get_follow_streamer_auth_header):  # 检查是否第三方登录
        """
        接口： isFirstThirdLogin

        检查是否第三方登录
        步骤：登录
        """
        response = requests.post(get_config_data['url'], headers=get_follow_streamer_auth_header,
                                 json=Payload.LoginAPI().isFirstThirdLogin(get_config_data['follow_streamer']))
        assert response.status_code == 200
        data = json.loads(response.text)
        is_first_third_login = data["data"]["isFirstThirdLogin"]["isFirstThirdLogin"]
        assert is_first_third_login is False, "'isFirstThirdLogin' is not False."

    @allure.title('test_LiveCarousel')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_LiveCarousel(self, get_config_data, api_headers):  # 轮播检查
        """
        接口： LiveCarousel

        轮播检查
        """
        response = requests.post(get_config_data['url'], headers=api_headers,
                                 json=Payload.HomePageAPI().LiveCarousel())
        assert response.status_code == 200
        # 验证 totalCount 字段的值为 5
        data = json.loads(response.text)
        total_count = data["data"]["liveCarousel"]["totalCount"]
        assert total_count == 5, "'totalCount' is not 5."

        # 验证 list 字段不为空
        carousel_list = data["data"]["liveCarousel"]["list"]
        assert carousel_list, "'list' is empty."

        # 验证 list 中每一项不为空
        for item in carousel_list:
            assert item, "An item in 'list' is empty."


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_homepage.py', '--alluredir', './report/results-20230627-1'])
    os.system('allure generate ./report/results-20230627-1 -o ./report/report-20230627-1 --clean')
