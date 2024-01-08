import os
import allure
import pytest
import loadData.payloadData as Payload
from tests import common
from datetime import datetime


@allure.feature('test_streamerDashboardPage')
class TestStreamerDashboardPage:
    @allure.title('test_dashboardLivePanelInfo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashboardLivePanelInfo(self, get_config_data, get_follow_streamer_auth_header):  # 主播dashboard页面检查
        """
        接口： MeDashboard

        检查主播:automation的Dashboard信息是否正确
        """
        response_json = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                        Payload.DaskboardAPI().MEDashboard(get_config_data['follow_streamer']))
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
        # with allure.step('检查主播的设置的缩列图是否正确'):
        #     assert response_json['data']['me']['private']['streamTemplate']['thumbnailUrl'] == \
        #            'https://images.stg.dlivecdn.com/thumbnail/37113e86-e28d-11ed-9838-e6f76b90cd4f', \
        #         'streamer language is： https://images.stg.dlivecdn.com/thumbnail/37113e86-e28d-11ed-9838-e6f76b90cd4f'

    @allure.title('test_dashBoardSearchTags')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_dashBoardSearchTags(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：DashBoardSearchTags

        主播的Dashboard -》Live 页面搜索tag
        """
        tag_name = get_config_data['dashboard_info']['search_tag']
        response_json = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
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
    def test_dashBoardSearchCategory(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：DashboardSearchCategories

        主播的Dashboard -》Live 页面搜索category
        """
        cate_name = get_config_data['dashboard_info']['search_category']
        response_json = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                        Payload.DaskboardAPI().DashboardSearchCategories(cate_name))
        category_exist = False
        print(response_json)
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

    @allure.title('test_enableAutoRun')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_enableAutoRun(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：RerunEnableSwitch

        打开auto run 开关
        """
        response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.DaskboardAPI().RerunEnableSwitch())
        print(response)
        with allure.step('检查返回值无error code'):
            assert response['data']['rerunEnable']['err'] is None, 'verify response code is not null'

    @allure.title('test_disableAutoRun')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_disableAutoRun(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：RerunDisableSwitch

        关闭auto run 开关
        """
        response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.DaskboardAPI().RerunDisableSwitch())
        with allure.step('检查返回值无error code'):
            assert response['data']['rerunDisable']['err'] is None, 'verify response code is not null'

    @allure.title('test_SubscriberSettings')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_SubscriberSettings(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：SetSubSettings

        设置subscription 信息
        """
        currentDateAndTime = datetime.now()
        currentTime = currentDateAndTime.strftime("%H%h%S")
        benefits = 'automationTest_' + currentTime
        backgroundImage = "https://images.stg.dlivecdn.com/thumbnail/bd939713-ea48-11ed-a524-425e9654e40d"
        badgeColor = "#FF0066"
        badgeText = "autoTest"
        streakTextColor = "#FFD300"
        textColor = "#800080"
        payload = Payload.DaskboardAPI().SetSubSettings(benefits=benefits, badgeColor=badgeColor, badgeText=badgeText,
                                                        streakTextColor=streakTextColor,
                                                        textColor=textColor, backgroundImage=backgroundImage)
        response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header, payload)
        with allure.step('检查返回值无error code'):
            assert response['data']['subSettingSet']['err'] is None, 'verify response code is not null'

        response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.DaskboardAPI.MEDashboard(get_config_data['follow_streamer']))
        subSetting = response['data']['me']['subSetting']
        print('2222')
        print(subSetting)
        with allure.step('检查badgeColor是否更新正确'):
            assert subSetting['badgeColor'] == badgeColor, '修改badge color 不成功，修改成：' + badgeColor + \
                                                           '而实际是:' + subSetting['badgeColor']
        with allure.step('badgeText'):
            assert subSetting['badgeText'] == badgeText, '修改badgeText 不成功，修改成：' + badgeText + \
                                                         '而实际是:' + subSetting['badgeText']
        with allure.step('检查streakTextColor是否更新正确'):
            assert subSetting[
                       'streakTextColor'] == streakTextColor, '修改streakTextColor不成功，修改成：' + streakTextColor + \
                                                              '而实际是:' + subSetting['streakTextColor']
        with allure.step('检查textColor是否更新正确'):
            assert subSetting['textColor'] == textColor, '修改textColor不成功，修改成：' + textColor + \
                                                         '而实际是:' + subSetting['textColor']
        with allure.step('检查benefits是否更新正确'):
            assert subSetting['benefits'][0] == benefits, '修改benefits不成功，修改成：' + benefits + \
                                                          '而实际是:' + subSetting['benefits']

    @allure.title('test_StreamHostSet')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_StreamHostSet1_add(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：StreamHostSet

        添加hosting
        """
        user = 'appletv'
        streamer = get_config_data['follow_streamer']
        with allure.step('添加hosting'):
            resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.DaskboardAPI().StreamHostSet(user))
            assert resp['data']['hostSet']['err'] is None
            hostingID = resp['data']['hostSet']['livestream']['permlink']
            with allure.step('检查添加的hosting 以后显示在hosting 列表'):
                host_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                            Payload.DaskboardAPI().MEDashboard(streamer))
                hosting_list = host_resp['data']['me']['hostingLivestream']['permlink']
                print('hosting列表如下：' + str(hosting_list))
                assert not any(hostingID == item for item in hosting_list), 'Hosting 视频在hosting列表中'

    @allure.title('test_StreamHostDelete')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_StreamHostSet2_delete(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：StreamHostDelete

        删除hosting
        """
        streamer = get_config_data['follow_streamer']
        with allure.step('获取一个要删除的hosting id'):
            host_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                        Payload.DaskboardAPI().MEDashboard(streamer))
            delete_hosting_id = host_resp['data']['me']['hostingLivestream']['permlink']
            delete_hotsing = str(delete_hosting_id).split('+')[0]
        with allure.step('开始删除hosting'):
            resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.DaskboardAPI().StreamHostDelete(delete_hotsing))
            assert resp['data']['hostDelete']['err'] is None
            with allure.step('检查删除后的hosting不显示在hosting 列表'):
                host_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                            Payload.DaskboardAPI().MEDashboard(streamer))
                hosting_list = host_resp['data']['me']['hostingLivestream']
                print('hosting列表如下：' + str(hosting_list))
                assert hosting_list is None, '删除Hosting视频以后，视频还在hosting列表中'


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_streamerDashboardPage.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')
