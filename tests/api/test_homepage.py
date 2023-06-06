import os
import pytest
import requests
import json
import loadData.payloadData as Payload
import allure


@allure.feature('test_homepage')
class TestHomePage:
    @allure.title('test_homepage_carousels')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_carousels(self, get_config_data, api_headers): #轮播检查
        with allure.step('21312415'):
            response = requests.post(get_config_data['url'], headers=api_headers,
                                    json=Payload.homepage_carousels())
            assert response.status_code == 200
            response_json = json.loads(response.text)
            print(response_json)
            assert "data" in response.json()

    @allure.title('test_homepage_livestream')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_livestream(self, get_config_data, api_headers): #画廊直播间检查
        response = requests.post(get_config_data['url'], headers=api_headers,
                                json=Payload.homepage_livestream())
        response_json = json.loads(response.text)
        print(response_json)
        assert response.status_code == 200
        assert "data" in response.json()


    @allure.title('test_homepage_list_recommendation')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_list_recommendation(self, get_config_data, api_headers):# 推荐系统
        response = requests.post(get_config_data['url'], headers=api_headers,
                                json=Payload.homepage_list_recommendation())
        assert response.status_code == 200                       
        response_json = json.loads(response.text)
        print(response_json)
        data = response_json.get('data')
        home_page_list_recommendation = data.get('listRecommendation')
        print(home_page_list_recommendation)
        assert home_page_list_recommendation is not None


    @allure.title('test_homepage_global_information_recommend')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_global_information_recommend(self, get_config_data, api_headers):# 主页左边的推荐列表
        response = requests.post(get_config_data['url'], headers=api_headers,
                                json=Payload.homepage_global_information_recommend())
        response_json = json.loads(response.text)
        # 判断 recommendChannels 数组是否为空
        recommend_channels = response_json['data']['globalInfo']['recommendChannels']
        assert len(recommend_channels) > 0

        assert response.status_code == 200


    @allure.title('test_homepage_nav_search_result')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_nav_search_result(self, get_config_data, api_headers):
        response = requests.post(get_config_data['url'], headers=api_headers,
                                json=Payload.homepage_nav_search_result("automation"))
        assert response.status_code == 200
        # 解析返回结果
        data = json.loads(response.text)
        print(data)
        users = data['data']['search']['allUsers']['list']
        print(users)

        # 搜索"displayname": "automation"
        found_user = False
        for user in users:
            if user['creator']['displayname'] == 'automation':
                found_user = True
                break
        # 检查结果
        assert found_user == True


    @allure.title('test_homepage_nav_search_category')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_nav_search_category(self, get_config_data, api_headers):
        response = requests.post(get_config_data['url'], headers=api_headers,
                                json=Payload.homepage_nav_search_result("qatest"))
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

        # 检查是否存在"title": "qaTest"
        found_category = False
        for category in categories:
            if category.get("title") == "qaTest":
                found_category = True
                break

        # 检查结果
        assert found_category == True, "Category 'qaTest' not found"



    @allure.title('test_me_global')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_me_global(self, get_config_data, api_headers):
        response = requests.post(get_config_data['url'], headers=api_headers,
                                json=Payload.me_global())
        assert response.status_code == 200
        # 解析返回结果
        data = json.loads(response.text)
        print(data)
        # 检查用户ID是否正确
        assert data['data']['me']['id'] == 'user:automationviewer', "User ID is incorrect"

        # 检查用户名是否正确
        assert data['data']['me']['username'] == 'automationviewer', "Username is incorrect"

        # 检查用户余额是否为0
        assert data['data']['me']['wallet']['balance'] == '0', "User balance is not 0"

        # 检查用户头像URL是否正确
        assert data['data']['me']['avatar'] == 'https://image.dlivecdn.com/avatar/default17.png', "Avatar URL is incorrect"

        # 检查用户角色是否为None
        assert data['data']['me']['role'] == 'None', "User role is not None"

        # 检查用户邮箱是否已验证
        assert data['data']['me']['private']['emailVerified'] == True, "Email is not verified"

        # 检查用户语言设置是否为英文
        assert data['data']['me']['private']['language'] == 'en', "Language is not English"


    @allure.title('test_live_streams_languages')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_live_streams_languages(self, get_config_data, api_headers):
        response = requests.post(get_config_data['url'], headers=api_headers,
                                json=Payload.live_streams_languages())
        assert response.status_code == 200
        # 解析返回结果
        data = json.loads(response.text)

        # 检查返回的数据中的"languages"列表是否包含至少一个元素
        assert len(data["data"]["languages"]) > 0, "'languages' list is empty"

        #检查返回的数据中的每个语言对象是否包含"id"、"backendID"、"language"和"code"字段
        for language in data["data"]["languages"]:
            assert "id" in language, "Language object does not contain 'id' field"
            assert "backendID" in language, "Language object does not contain 'backendID' field"
            assert "language" in language, "Language object does not contain 'language' field"
            assert "code" in language, "Language object does not contain 'code' field"



