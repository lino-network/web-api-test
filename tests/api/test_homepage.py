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
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.homepage_carousels())
            print(response_json)
            with allure.step('检查轮播的位置是否为5'):
                assert len(response_json['data']['carousels']) == 5
            with allure.step('检查轮播接口的返回值不包含err '):
                assert 'err' not in response_json

    @allure.title('test_homepage_livestream')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_livestream(self, get_config_data, api_headers): # 画廊直播间检查
        """
        接口： HomePageLivestream

        检查首页直播流接口
        """
        with allure.step('检查首页直播流接口'):
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.homepage_livestream())
            print(response_json)
            with allure.step('检查轮播接口的返回值不为空 '):
                assert len(response_json['data']['livestreams']['list']) is not None
            with allure.step('检查轮播接口的返回值不包含err '):
                assert 'err' not in response_json

    @allure.title('test_homepage_list_recommendation')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_list_recommendation(self, get_config_data, api_headers):  # 推荐系统
        """
        接口： HomePageListRecommendation

        检查主页推荐系统
        """
        with allure.step('检查主页推荐系统 '):
            response_json = common.api_post(get_config_data['url'], api_headers, Payload.homepage_list_recommendation())
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
                                            Payload.homepage_global_information_recommend())
            # 判断 recommendChannels 数组是否为空
            recommend_channels = response_json['data']['globalInfo']['recommendChannels']
            with allure.step('检查数据不为空'):
                assert len(recommend_channels) > 0
            with allure.step('检查数据无报错'):
                assert 'err' not in response_json['data']

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
                                   Payload.homepage_nav_search_result("automation"))
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

    @allure.title('test_me_global')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_me_global(self, get_config_data, api_headers):
        """
        接口: MeGlobal

        测试用户: 66@nqmo.com/password
        检查用户global信息
        """
        data = common.api_post(get_config_data['url'], common.get_auth_header(get_config_data['viewer1_auth']),
                               Payload.me_global())
        print(data)
        with allure.step('检查用户ID是否正确'):
            assert data['data']['me']['id'] == 'user:dlive-degnujtptx', "User ID is incorrect"

        with allure.step('检查用户名是否正确'):
            assert data['data']['me']['username'] == 'dlive-degnujtptx', "Username is incorrect"

        with allure.step('检查用户余额是否为0'):
            assert data['data']['me']['wallet']['balance'] != 0, "User balance is 0"

        with allure.step('检查用户头像URL是否正确'):
            assert data['data']['me']['avatar'] == 'https://image.dlivecdn.com/avatar/default22.png', \
                "Avatar URL is incorrect"

        with allure.step('检查用户角色是否为None'):
            assert data['data']['me']['role'] == 'None', "User role is not None"

        with allure.step('检查用户邮箱是否已验证'):
            assert data['data']['me']['private']['emailVerified'] == True, "Email is not verified"

        with allure.step('检查用户语言设置是否为英文'):
            assert data['data']['me']['private']['language'] == 'en', "Language is not English"
