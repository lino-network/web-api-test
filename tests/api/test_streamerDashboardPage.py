import os

import allure
import pytest

import loadData.payloadData as Payload

from tests import common


@allure.feature('test_streamerDashboardPage')
class TestStreamerDashboardPage:
    @allure.title('test_dashboardLivePanelInfo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashboardLivePanelInfo(self, get_config_data):  # 主播dashboard页面检查
        """
        接口： MeDashboard

        检查主播:automation的Dashboard信息是否正确
        """
        response_json = common.api_post(get_config_data['url'],
                                        common.get_auth_header(get_config_data['follow_streamer_auth']),
                                        Payload.DaskboardAPI().MeDashboard(get_config_data['follow_streamer']))
        print(response_json)
        with allure.step('检查主播的title 是否是：Automation test'):
            assert response_json['data']['me']['private']['streamTemplate'][
                       'title'] == 'Automation test', 'streamer title is not Automation test'
        with allure.step('检查主播的所在的category 是否是：qaTest'):
            assert response_json['data']['me']['private']['streamTemplate']['category']['title'] == 'qaTest', \
                'streamer category is not qaTest'
        with allure.step('检查主播的所在的tag是否是：gogo'):
            assert response_json['data']['me']['private']['streamTemplate']['tags'][0] == 'gogo', \
                'streamer tag is not qaTest'
        with allure.step('检查主播的设置的语言是否是：English'):
            assert response_json['data']['me']['livestream']['language']['language'] == 'English', \
                'streamer language is not qaTest'
        with allure.step('检查主播的设置的rating tag是否是：Family Friendly'):
            if (response_json['data']['me']['private']['streamTemplate']['ageRestriction'] is False &
                    response_json['data']['me']['private']['streamTemplate']['earnRestriction'] is False):
                assert True, 'streamer rating tag is not Family Friendly'
        with allure.step('检查主播的设置的缩列图是否正确'):
            assert response_json['data']['me']['private']['streamTemplate']['thumbnailUrl'] == \
                   'https://images.stg.dlivecdn.com/thumbnail/37113e86-e28d-11ed-9838-e6f76b90cd4f', \
                'streamer language is： https://images.stg.dlivecdn.com/thumbnail/37113e86-e28d-11ed-9838-e6f76b90cd4f'

    @allure.title('test_dashBoardSearchTags')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashBoardSearchTags(self, get_config_data):
        """
        接口：DashBoardSearchTags

        主播的Dashboard -》Live 页面搜索tag
        """
        tag_name = get_config_data['dashboard_info']['search_tag']
        response_json = common.api_post(get_config_data['url'],
                                        common.get_auth_header(get_config_data['follow_streamer_auth']),
                                        Payload.DaskboardAPI().DashBoardSearchTags(tag_name))
        tag_exist = False
        for i in response_json['data']['tags']:
            print(i)
            if i == tag_name:
                tag_exist = True
                break
        with allure.step('检查在dashboard 能否search tag: ' + str(tag_name)):
            if tag_exist:
                assert True, 'search result not the expected: ' + tag_name
                assert 'err' not in response_json['data']
            else:
                assert False

    @allure.title('test_dashBoardSearchCategory')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashBoardSearchCategory(self, get_config_data):
        """
        接口：DashboardSearchCategories

        主播的Dashboard -》Live 页面搜索category
        """
        cate_name = get_config_data['dashboard_info']['search_category']
        response_json = common.api_post(get_config_data['url'],
                                        common.get_auth_header(get_config_data['follow_streamer_auth']),
                                        Payload.DaskboardAPI().DashboardSearchCategories(cate_name))
        category_exist = False
        print(response_json['data'])
        cate_list = response_json['data']['search']['categories']['list']
        for i in cate_list:
            print(i['title'])
            if i['title'] == cate_name:
                category_exist = True
                break
        with allure.step('检查在dashboard 能否search category: ' + str(cate_name)):
            if category_exist is True:
                assert True, 'search result not the expected: ' + cate_name
                assert 'err' not in response_json['data']
            else:
                assert False, 'expected category ' + cate_name + ' not exists'


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_streamerDashboardPage.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')
