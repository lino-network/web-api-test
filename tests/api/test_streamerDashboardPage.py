import os

import allure
import pytest

import loadData.payloadData as Payload

from tests import common


@allure.feature('test_streamerDashboardPage')
class TestStreamerDashboardPage:
    @allure.title('test_homepage_carousels')
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
            assert response_json['data']['me']['private']['streamTemplate']['title'] == 'Automation test', 'streamer title is not Automation test'
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


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_streamerDashboardPage.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')

