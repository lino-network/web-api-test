import os
import allure
import pytest
import loadData.payloadData as Payload
from tests import common
from datetime import datetime


@allure.feature('test_streamerIncentive')
class TestStreamerIncentive:
    @allure.title('test_CheckPointRankWalletAndHistoryTabNotifyClosed')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_check_point_rank_wallet_and_history_tab_notify_closed(self, get_config_data, get_incentive_streamer_auth_header):  # 主播dashboard页面检查
        """
        接口： CheckPointRankWalletAndHistoryTabNotifyClosed

        检查红点
        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.StreamerIncentiveAPI().CheckPointRankWalletAndHistoryTabNotifyClosed("appletv"))
        print(response_json)
        with allure.step('Check Point Rank Wallet and History Tab notification is not closed for user appletv'):
            assert response_json['data']['checkPointRankWalletAndHistoryTabNotifyClosed']['isClosed'] == True


    @allure.title('test_ClosePointRankWalletAndHistoryTabNotify')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_close_point_rank_wallet_and_history_tab_notify(self, get_config_data, get_incentive_streamer_auth_header):
        """
        接口：ClosePointRankWalletAndHistoryTabNotify
        

        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.StreamerIncentiveAPI().ClosePointRankWalletAndHistoryTabNotify("appletv"))

        with allure.step('Error occurred while closing Point Rank Wallet and History Tab notification'):
            assert response_json['data']['closePointRankWalletAndHistoryTabNotify']['err'] is None

    @allure.title('test_EventGetPointTopUsers')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_event_get_point_top_user(self, get_config_data, get_incentive_streamer_auth_header):
        """
        接口：EventGetPointTopUsers
        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.StreamerIncentiveAPI().EventGetPointTopUsers("appletv"))

        assert response_json['data']['getPointEventTopUsers']['err'] is None
        users = response_json['data']['getPointEventTopUsers']['users']

        for user in users:
            with allure.step(f"Check user {user['username']}"):
                assert user['username'] is not None, f"Username is empty for user {user['username']}"
                assert user['points'] is not None, f"Points is empty for user {user['username']}"
                assert user['rank'] is not None, f"Rank is empty for user {user['username']}"
                assert user['ratio'] is not None, f"Ratio is empty for user {user['username']}"
                assert user['eventId'] is not None, f"Event ID is empty for user {user['username']}"
                assert response_json['data']['getPointEventTopUsers']['err'] is None, "Error occurred in getPointEventTopUsers response"
            
    @allure.title('test_GetPontEventRankRewardByUsernames')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_event_rank_reward_by_user(self, get_config_data, get_incentive_streamer_auth_header):
        """
        接口：GetPontEventRankRewardByUsername
        
        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.StreamerIncentiveAPI().GetPontEventRankRewardByUsername())

        metas = response_json['data']['GetPontEventRankRewardByUsername']['metas']

        for meta in metas:
            with allure.step(f"Check metadata with id {meta['id']}"):
                assert all(meta[key] is not None for key in meta if key != 'operator'), f"Field is empty for metadata with id {meta['id']}"

    @allure.title('test_get_event_rank_reward_by_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_event_rank_reward_by_user(self, get_config_data, get_incentive_streamer_auth_header):
        """
        接口：PointEventEarningsByUsername
        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.StreamerIncentiveAPI().PointEventEarningsByUsername())

        earnings = response_json['data']['PointEventEarningsByUsername']['earnings']

        for earning in earnings:
            with allure.step(f"Check earning for {earning['displayedSymbol']}"):
                assert earning['tokenId'] is not None, f"Token ID is empty for {earning['displayedSymbol']}"
                assert earning['displayedSymbol'] is not None, f"Displayed Symbol is empty for {earning['displayedSymbol']}"
                assert earning['logo'] is not None, f"Logo is empty for {earning['displayedSymbol']}"
                assert earning['total'] is not None, f"Total is empty for {earning['displayedSymbol']}"

    @allure.title('test_GetHtxUid')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_htx_uid(self, get_config_data, get_incentive_streamer_auth_header):
        """
        接口：GetHtxUid
        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.StreamerIncentiveAPI().GetHtxUid("appletv"))
        assert response_json['data']['getHtxUid']['err'] is None
        with allure.step('uid不为空'):
            assert response_json['data']['getHtxUid']['htxUid']is not None
        print("No errors and htxUid has a value.")

    @allure.title('test_get_set_htx_uid_deadline')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_set_htx_uid_deadline(self, get_config_data, get_incentive_streamer_auth_header):
        """
        接口：GetSetHtxUidDeadline
        
        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.StreamerIncentiveAPI().GetSetHtxUidDeadline())
        assert response_json['data']['getSetHtxUidDeadline']['err'] is None
        assert response_json['data']['getSetHtxUidDeadline']['onoff'] == False






if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_streamerIncentive.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')
