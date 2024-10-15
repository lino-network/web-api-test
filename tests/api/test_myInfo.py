import os
import allure
import pytest
import loadData.payloadData as Payload
from tests import common
from datetime import datetime


@allure.feature('test_myInfo')
class TestMyInfo:
    @allure.title('test_MeSubscribing')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_my_subscribtion(self, get_config_data, get_auto_viewer_auth_header):
        """
        接口： MeSubscribing

        """
        response_json = common.api_post(get_config_data['url'], get_auto_viewer_auth_header, Payload.MyInfoAPI().MeSubscribing())

        me_data = response_json['data']['me']
        subscribing_list = me_data['private']['subscribing']['list']

        for sub in subscribing_list:
            if sub['streamer']['username'] == 'helenstreamer':
                assert sub['status'] == 'active'
            assert all(value is not None for value in sub.values())

    @allure.title('test_UserUnsubscribe')
    @allure.severity(allure.severity_level.NORMAL)
    def test_my_UserUnsubscribe(self, get_config_data, get_auto_viewer_auth_header):
        """
        接口： UserUnsubscribe
        测试取消一个不存在的订阅，会报错

        """
        response_json = common.api_post(get_config_data['url'], get_auto_viewer_auth_header, Payload.MyInfoAPI().UserUnsubscribe("errorstreamer"))
        
        metadata = response_json['data']['unsubscribe']
        assert metadata['err']['code'] == 7001
        assert metadata['err']['__typename'] == 'Error'
        assert metadata['__typename'] == 'UnsubscribeResponse'

    @allure.title('test_ClosePointRankWalletAndHistoryTabNotify')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_wallet_address_by_owner(self, get_config_data, get_incentive_streamer_auth_header):
        """
        接口：getWalletAddressByOwner
        检查appletv钱包里的内容不为空
        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.MyInfoAPI().getWalletAddressByOwner("vptest"))
        wallets = response_json["data"]["getWalletAddressByOwner"]["wallets"]
        for wallet in wallets:
            assert "name" in wallet
            assert "address" in wallet
            assert wallet["name"] != ""
            assert wallet["address"] != ""


    @allure.title('test_List_Withdraw_Txes_By_Streamer')
    @allure.severity(allure.severity_level.NORMAL)
    def test_List_Withdraw_Txes_By_Streamer(self, get_config_data, get_incentive_streamer_auth_header):
        """
        接口：ListWithdrawTxesByStreamer
        """
        response_json = common.api_post(get_config_data['url'], get_incentive_streamer_auth_header,
                                        Payload.MyInfoAPI().ListWithdrawTxesByStreamer("helenstreamer"))
        withdraw_txes = response_json["data"]["ListWithdrawTxesByStreamer"]

        for tx in withdraw_txes:
            for key, value in tx.items():
                assert value is not None, f"Field {key} is null in transaction: {tx}"






if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_myInfo.py', '--alluredir', './report/results'])
    os.system('allure generate ./report/results -o ./report/report --clean')
