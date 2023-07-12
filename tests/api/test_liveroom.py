import os
import time
import pytest
import loadData.payloadData as Payload
from datetime import datetime
import allure
import tests.common as common


@allure.feature('test_liveroom_page')
class TestLivePage:
    @allure.title('test_follow_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_follow_user(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口: FollowUser, MeSidebar

        用户: viewer1_username follow 主播: automation
        """
        with allure.step('检查用户follow主播之前，主播不在sidebar列表'):
            before_side_response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                        Payload.sidebar_follow_user_list())
            before_side_follow_list = before_side_response_json['data']['me']['private']['followeeFeed']['list']
            print(before_side_follow_list)
            for i in before_side_follow_list:
                if i['displayname'] == get_config_data['follow_streamer']:
                    print('未follow主播之前，主播已经在左边的sidebar列表')
                    assert False

        with allure.step('开始follow主播'):
            follow_response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                   Payload.follow_user(get_config_data['follow_streamer']))
            assert follow_response_json['data']['follow']['err'] is None
        time.sleep(15)
        with allure.step('检查follow主播之后，主播是否在左边的sidebar列表'):
            after_side_response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                       Payload.sidebar_follow_user_list())
            after_side_follow_list = after_side_response_json['data']['me']['private']['followeeFeed']['list']
            user_follow_list = False
            for i in after_side_follow_list:
                print(i['displayname'])
                if i['displayname'] == get_config_data['follow_streamer']:
                    print('主播在左边follow 列表')
                    user_follow_list = True
                    break
            assert user_follow_list is True

    @allure.title('test_unfollow_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_unfollow_user(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口: sidebar_follow_user_list, UnfollowUser

        用户: viewer1_username unfollow 主播: automation
        """
        with allure.step('开始unfollow主播'):
            follow_response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                   Payload.unfollow_user(get_config_data['follow_streamer']))
            assert follow_response_json['data']['unfollow']['err'] is None
        time.sleep(10)
        with allure.step('检查unfollow主播之后，主播是否在左边的sidebar列表'):
            after_side_response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                       Payload.sidebar_follow_user_list())
            after_side_follow_list = after_side_response_json['data']['me']['private']['followeeFeed']['list']
            print(after_side_follow_list)
            for i in after_side_follow_list:
                if i['displayname'] == get_config_data['follow_streamer']:
                    print('主播不在左边follow 列表')
                    assert False

    @allure.title('test_send_message_and_emo')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_send_message_and_emo(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口: SendStreamChatMessage

        用户viewer1发送信息和点赞的表情包给主播: automation
        """
        with allure.step('开始发送信息和点赞的表情包给主播'):
            currentDateAndTime = datetime.now()
            currentTime = currentDateAndTime.strftime("%H%M%S")
            print(currentTime)
            message = "AAA " + get_config_data['send_message'] + '_' + currentTime
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.send_chat(get_config_data['follow_streamer'], message, [0, 2]))
            print(response_json)
        with allure.step('检查返回值不报错'):
            assert response_json['data']['sendStreamchatMessage']['err'] is None
        with allure.step('检查返回的信息就是发送的信息'):
            assert response_json['data']['sendStreamchatMessage']['message']['content'] == message

    @allure.title('test_donate_1_lemon')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_donate_1_lemon(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口: StreamDonate, sidebar_follow_user_list

        用户viewer1 打赏 1 lemon 给直播: automation
        """
        with allure.step('获取打赏前用户的总lemon'):
            origin_lemon = common.get_account_lemon(get_config_data['url'], get_viewer1_login_auth_header)
            print('origin lemon is: ' + origin_lemon)
        with allure.step('开始打赏 1 lemon'):
            print('donate lemon is: ' + str(get_config_data['donate_value']))
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.donate_lemon(get_config_data['follow_streamer_permlink'],
                                                                 get_config_data['donate_value']))
            print(response_json)
            with allure.step('检查放回值无报错'):
                assert response_json['data']['donate']['err'] is None
            with allure.step('检查打赏的金额是 1 lemon'):
                assert response_json['data']['donate']['recentCount'] == get_config_data['donate_value']
        time.sleep(5)
        with allure.step('检查打赏后用户的总lemon相应的减少'):
            after_donate_lemon = common.get_account_lemon(get_config_data['url'], get_viewer1_login_auth_header)
            print('after donate lemon is: ' + after_donate_lemon)
            lemon = int(origin_lemon) - int(get_config_data['donate_value'])
            assert int(after_donate_lemon) == lemon

    @allure.title('test one viewer gift 5 sub and 5 user to claim')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_give_5_sub_in_channel(self, get_config_data):
        """
        接口: AddGiftSub, AddGiftSubClaim

        用户viewer在直播间：automation发送5 个gift, 5 个用户领取
        """
        header = common.get_login_auth_header(get_config_data['url'],
                                              get_config_data['gift_sub_info']['give_sub_gift_user'],
                                              get_config_data['gift_sub_info']['give_sub_gift_user_pwd'])
        origin_lemon = common.get_account_lemon(get_config_data['url'], header)
        print('origin account lemon is: ' + str(origin_lemon))
        with allure.step('用户 ' + str(get_config_data['gift_sub_info']['give_sub_gift_user'])
                         + ' 发送5 个gift在直播间：' + str(get_config_data['gift_sub_info']['streamer'])):
            gift_response_json = common.api_post(get_config_data['url'], header,
                                                 Payload.add_gift_sub(get_config_data['gift_sub_info']['streamer'], 5))
            print(gift_response_json)
            with allure.step('检查返回值无报错'):
                assert gift_response_json['data']['giftSub']['err'] is None
        claim_list = get_config_data['gift_sub_info']['claim_user']
        for i in claim_list:
            viewer_header = common.get_login_auth_header(get_config_data['url'],
                                                         i['get_gift_sub_user'],
                                                         i['get_gift_sub_user_pwd'])
            with allure.step('用户' + str(i['get_gift_sub_user']) + ' 领取gift sub'):
                claim_response_json = common.api_post(get_config_data['url'], viewer_header,
                                                      Payload.add_gift_sub_claim(get_config_data['gift_sub_info']['streamer']))
                print('claim_response_json')
                with allure.step('检查用户 ' + str(i['get_gift_sub_user']) + ' 领取gift sub 的时候无报错'):
                    assert claim_response_json['data']['giftSubClaim']['err'] is None
        after_lemon = common.get_account_lemon(get_config_data['url'], header)
        print('after gift 5 sub account lemon is: ' + str(after_lemon))
        with allure.step('检查发送了5 gift sub 帐户的钱相应的减少1490'):
            assert int(after_lemon) + 1490 == int(origin_lemon), 'lemon减少不是1490, 而是 ' + str(int(origin_lemon)-int(after_lemon))

    @allure.title('test_streamer_open_chest')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_streamer_open_chest(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口: LivestreamTreasureChestAddCheck, GiveawayStart

        1. streamer add 20 lemon to chest
        2. user1: test_streamer_add_lemon_to_chest send message to chat and open chest
        3. user2: chest_donate_user2_auth donate lemon and open chest
        4. user3: chest_user_no_point_auth no point to open chest
        """
        with allure.step("在加lemon进宝箱之前检查帐户总的lemon"):
            origin_lemon = common.get_account_lemon(get_config_data['url'], get_follow_streamer_auth_header)
            print("Before add to chest total lemon is: " + str(origin_lemon))
        with allure.step('streamer: automation add 20 lemon to chest'):
            add_chest_payload = Payload.LiveRoomAPI().ChestUserTransfer(str(get_config_data['chest_info']['add_lemon']))
            add_chest = common.api_post(get_config_data['url'], get_follow_streamer_auth_header, add_chest_payload)
            with allure.step('检查加lemon进宝箱是否成功'):
                assert add_chest['data']['treasureChestUserTransfer']['err'] is None, '加lemon进宝箱失败'
        with allure.step("在加lemon进宝箱之后检查帐户总的lemon"):
            after_lemon = common.get_account_lemon(get_config_data['url'], get_follow_streamer_auth_header)
            print("After add to chest total lemon is: " + str(after_lemon))
        with allure.step('检查加钱进宝箱以后，总帐户减少对应的数目'):
            assert int(after_lemon) + get_config_data['chest_info']['add_lemon'] == int(origin_lemon), '帐户lemon的减少不' \
                                        '是' + get_config_data['chest_info']['add_lemon'] + '而是' + str(int(origin_lemon)-int(after_lemon))
        viewer1_header = common.get_login_auth_header(get_config_data['url'],
                                                      get_config_data['chest_info']['send_msg_chest_user1'],
                                                      get_config_data['chest_info']['send_msg_chest_user1_pwd'])
        viewer2_header = common.get_login_auth_header(get_config_data['url'],
                                                      get_config_data['chest_info']['donate_chest_user2'],
                                                      get_config_data['chest_info']['chest_donate_user2_pwd'])
        viewer3_header = common.get_login_auth_header(get_config_data['url'],
                                                      get_config_data['chest_info']['chest_user_no_point_user'],
                                                      get_config_data['chest_info']['chest_user_no_point_pwd'])
        with allure.step(str(get_config_data['chest_info']['send_msg_chest_user1']) + 'send message to chat'):
            msg_response = common.api_post(get_config_data['url'],
                                           viewer1_header, Payload.send_chat(get_config_data['chest_info']['chest_streamer'],
                                                                             get_config_data['chest_info']['msg'], []))
        with allure.step(str(get_config_data['chest_info']['donate_chest_user2'] + 'donate lemon')):
            donate_response = common.api_post(get_config_data['url'], viewer2_header,
                                              Payload.donate_lemon(
                                                  get_config_data['chest_info']['chest_streamer_permlimk']
                                              , get_config_data['chest_info']['donate_lemon_value']))
        with allure.step('主播开始开启宝箱'):
            open_response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                            Payload.LiveRoomAPI().give_away_start())
            print('0000')
            print(open_response)
            with allure.step('检查开启宝箱是否成功'):
                assert open_response['data']['giveawayStart']['err'] is None, '主播开启宝箱失败，信息为' + \
                                                                        str(open_response['data']['giveawayStart']['err'])
        viewer1_origin_lemon = common.get_account_lemon(get_config_data['url'], viewer1_header)
        viewer2_origin_lemon = common.get_account_lemon(get_config_data['url'], viewer2_header)
        with allure.step('发信息观众开始参与宝箱抽奖'):
            viewer1_claim_re = common.api_post(get_config_data['url'], viewer1_header,
                                               Payload.LiveRoomAPI().give_away_claim(get_config_data['chest_info']['chest_streamer']))
            with allure.step('检查是否成功参与宝箱'):
                assert viewer1_claim_re['data']['giveawayClaim']['err'] is None, '参与宝箱失败'
        with allure.step('donate观众开始参与宝箱抽奖'):
            viewer2_claim_re = common.api_post(get_config_data['url'], viewer2_header,
                                               Payload.LiveRoomAPI().give_away_claim(
                                                   get_config_data['chest_info']['chest_streamer']))
            with allure.step('检查是否成功参与宝箱'):
                assert viewer2_claim_re['data']['giveawayClaim']['err'] is None, '参与宝箱失败'
        with allure.step('无积分观众参与宝箱'):
            viewer3_claim_re = common.api_post(get_config_data['url'], viewer3_header,
                                               Payload.LiveRoomAPI().give_away_claim(
                                                   get_config_data['chest_info']['chest_streamer']))
            with allure.step('检查是否成功参与宝箱'):
                assert viewer3_claim_re['data']['giveawayClaim']['err'] is None, '参与宝箱失败'
        with allure.step('检查中奖名单'):
            winner_response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                              Payload.LiveRoomAPI().LivestreamTreasureChestWinners())
            winner_list = winner_response['data']['userByDisplayName']['treasureChest']['lastGiveawayRewards']
            viewer1_get_lemon = 0
            viewer2_get_lemon = 0
            with allure.step('检查无积分的观众不在中奖名单'):
                assert get_config_data['chest_info']['chest_user_no_point_user'] not in winner_list
            for i in winner_list:
                if i['user']['displayname'] in get_config_data['chest_info']['send_msg_chest_user1']:
                    viewer1_get_lemon = str(int(i['value']/10000))
                    print('发现信息的观众在中奖名单而且中奖金额是： ' + str(int(i['value']/10000)))
                    assert True, '发送信息的观众不在中奖名单'
                if i['user']['displayname'] in get_config_data['chest_info']['donate_chest_user2']:
                    viewer2_get_lemon = str(int(i['value']/10000))
                    print('donate的观众在中奖名单而且中奖金额是： ' + str(int(i['value']/10000)))
                    assert True, '发送信息的观众不在中奖名单'

    @allure.title('test_streamer_open_chest')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_clip(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：MeClipsOfMe, MeClipsByMe

        主播clip 自己和观众clip 主播
        """
        currentDateAndTime = datetime.now()
        currentTime = currentDateAndTime.strftime("%H%M%S")
        streamer_clip_message = 'streamer_clip_self'+ currentTime
        with allure.step("主播clip自己"):
            stream_clip_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                               Payload.me_clips_by_me())









if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_liveroom.py', '--alluredir', './report/results-20230627'])
    os.system('allure generate ./report/results-20230627 -o ./report/report-20230627 --clean')
