import os
import string
import time
import pytest
from dateutil.relativedelta import relativedelta

import loadData.payloadData as Payload
from datetime import datetime, timedelta
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
                                            Payload.LiveRoomAPI().send_chat(get_config_data['follow_streamer'], message,
                                                                            [0, 2]))
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
                                            Payload.LiveRoomAPI().donate_lemon(
                                                get_config_data['follow_streamer_permlink'],
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
                                                 Payload.LiveRoomAPI().add_gift_sub(
                                                     get_config_data['gift_sub_info']['streamer'], 5))
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
                                                      Payload.LiveRoomAPI().add_gift_sub_claim(
                                                          get_config_data['gift_sub_info']['streamer']))
                print('claim_response_json')
                with allure.step('检查用户 ' + str(i['get_gift_sub_user']) + ' 领取gift sub 的时候无报错'):
                    assert claim_response_json['data']['giftSubClaim']['err'] is None
        after_lemon = common.get_account_lemon(get_config_data['url'], header)
        print('after gift 5 sub account lemon is: ' + str(after_lemon))
        with allure.step('检查发送了5 gift sub 帐户的钱相应的减少1490'):
            assert int(after_lemon) + 1490 == int(origin_lemon), 'lemon减少不是1490, 而是 ' + str(
                int(origin_lemon) - int(after_lemon))

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
                                                                                                       '是' + \
                                                                                                       get_config_data[
                                                                                                           'chest_info'][
                                                                                                           'add_lemon'] + '而是' + str(
                int(origin_lemon) - int(after_lemon))
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
                                           viewer1_header, Payload.LiveRoomAPI().send_chat(
                    get_config_data['chest_info']['chest_streamer'],
                    get_config_data['chest_info']['msg'], []))
        with allure.step(str(get_config_data['chest_info']['donate_chest_user2'] + 'donate lemon')):
            donate_response = common.api_post(get_config_data['url'], viewer2_header,
                                              Payload.LiveRoomAPI().donate_lemon(
                                                  get_config_data['chest_info']['chest_streamer_permlimk']
                                                  , get_config_data['chest_info']['donate_lemon_value']))
        chest_streamer = get_config_data['chest_info']['chest_streamer']
        with allure.step('主播开始开启宝箱'):
            open_response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                            Payload.LiveRoomAPI().give_away_start())
            print(open_response)
            with allure.step('检查开启宝箱是否成功'):
                assert open_response['data']['giveawayStart']['err'] is None, '主播开启宝箱失败，信息为' + \
                                                                              str(open_response['data'][
                                                                                      'giveawayStart']['err'])
        viewer1_origin_lemon = common.get_account_lemon(get_config_data['url'], viewer1_header)
        viewer2_origin_lemon = common.get_account_lemon(get_config_data['url'], viewer2_header)
        claim_payload = Payload.LiveRoomAPI().give_away_claim(chest_streamer)
        print('claim_payload: ' + str(claim_payload))
        with allure.step('发信息观众开始参与宝箱抽奖'):
            viewer1_claim_re = common.api_post(get_config_data['url'], viewer1_header, claim_payload)
            with allure.step('检查是否成功参与宝箱'):
                assert viewer1_claim_re['data']['giveawayClaim']['err'] is None, '参与宝箱失败'
        with allure.step('donate观众开始参与宝箱抽奖'):
            viewer2_claim_re = common.api_post(get_config_data['url'], viewer2_header, claim_payload)
            with allure.step('检查是否成功参与宝箱'):
                assert viewer2_claim_re['data']['giveawayClaim']['err'] is None, '参与宝箱失败'
        with allure.step('无积分观众参与宝箱'):
            viewer3_claim_re = common.api_post(get_config_data['url'], viewer3_header,
                                               Payload.LiveRoomAPI().give_away_claim(chest_streamer))
            with allure.step('检查是否成功参与宝箱'):
                assert viewer3_claim_re['data']['giveawayClaim']['err'] is None, '参与宝箱失败'
        time.sleep(30)
        with allure.step('检查中奖名单'):
            winner_response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                              Payload.LiveRoomAPI().LivestreamTreasureChestWinners(chest_streamer))
            print('winner_response')
            print(winner_response)
            winner_list = winner_response['data']['userByDisplayName']['treasureChest']['lastGiveawayRewards']
            with allure.step('检查无积分的观众不在中奖名单'):
                assert get_config_data['chest_info']['chest_user_no_point_user'] not in winner_list
            message_user = False
            donate_user = False
            time.sleep(60)
            for i in winner_list:
                if i['user']['displayname'] in get_config_data['chest_info']['send_msg_chest_user1']:
                    viewer1_get_lemon = int(i['value']) / 100000
                    print('发信息的观众在中奖名单而且中奖金额是： ' + str(viewer1_get_lemon))
                    assert True
                    message_user = True
                    with allure.step('检查send message用户的宝箱中奖的lemon 是否加入用户帐号'):
                        viewer1_after_lemon = common.get_account_lemon(get_config_data['url'], viewer1_header)
                        assert int(viewer1_origin_lemon) + int(viewer1_get_lemon) <= int(viewer1_after_lemon) \
                               < int(viewer1_after_lemon) + 2
                if i['user']['displayname'] in get_config_data['chest_info']['donate_chest_user2']:
                    viewer2_get_lemon = int(i['value']) / 100000
                    print('donate的观众在中奖名单而且中奖金额是： ' + str(viewer2_get_lemon))
                    assert True
                    donate_user = True
                    with allure.step('检查打赏用户宝箱中奖的lemon 是否加入用户帐号'):
                        viewer2_after_lemon = common.get_account_lemon(get_config_data['url'], viewer2_header)
                        assert int(viewer2_origin_lemon) + int(viewer2_get_lemon) <= int(viewer2_after_lemon) \
                               < int(viewer2_after_lemon) + 2
            # if not message_user:
            #     with allure.step('发信息的观众不在中奖名单'):
            #         assert False
            if not donate_user:
                with allure.step('donate的观众不在中奖名单'):
                    assert False

    @allure.title('test_pwd_check')
    @allure.severity(allure.severity_level.NORMAL)
    def test_pwd_check(self, get_config_data, api_headers):
        """
        接口： PwdCheck

        直播间pwd接口检查
        """
        with allure.step("检查PwdCheck接口返回无报错"):
            resp = common.api_post(get_config_data['url'], api_headers,
                                   Payload.LiveRoomAPI().PwdCheck(get_config_data['follow_streamer']))
            assert resp['data']['pwdCheck']['err'] is None, '接口返回报错，错误信息是：' + \
                                                            str(resp['data']['pwdCheck']['err'])

    @allure.title('test_Live_stream_Page')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Live_stream_Page(self, get_config_data, api_headers):
        """
        接口： LivestreamPage

        直播页面接口检查
        直播间： automation
        """
        resp = common.api_post(get_config_data['url'], api_headers, Payload.LiveRoomAPI().
                               LivestreamPage(get_config_data['follow_streamer'], False, False))
        print(resp)
        with allure.step("检查LivestreamPage接口返回无报错"):
            assert 'err' not in resp['data'], '接口请求报错'
        with allure.step('检查直播间的offline图片网址对不对'):
            url = resp['data']['userByDisplayName']['offlineImage']
            assert url == 'https://images.stg.dlivecdn.com/thumbnail/2f067ebf-42ea-11ee-8c81-aedbe0993999', \
                'offline图片网址不对，实际的是： ' + str(url)
        with allure.step('检查直播间的category是否显示正确'):
            category = resp['data']['userByDisplayName']['livestream']['category']['title']
            assert category == 'Web3 Games', '主播的category显示不对，期望是Web3 Games，但是实际是：' + str(category)
        with allure.step('检查主播的displayname显示是否正确'):
            displayname = resp['data']['userByDisplayName']['livestream']['creator']['displayname']
            assert displayname == 'automation', '主播的名字显示不对，期望是automation，但是实际是：' + str(displayname)
        with allure.step('检查主播的title显示是否正确'):
            title = resp['data']['userByDisplayName']['livestream']['title']
            assert title == 'Automation test', '主播的title显示不对，期望是Automation test，但是实际是：' + str(title)
        tag_list = resp['data']['userByDisplayName']['livestream']['tags']
        with allure.step('检查主播的tag显示是否正确'):
            assert 'gogo' in tag_list, '主播的tag显示不对，期望是tag，但是实际是：' + str(tag_list)
        with allure.step('检查主播的语言显示是否正确'):
            assert 'English' in tag_list, '主播的语言显示不对，期望是English，但是实际是：' + str(tag_list)

    @allure.title('test_Live_room_top_contributors')
    @allure.severity(allure.severity_level.NORMAL)
    def test_Live_room_top_contributors(self, get_config_data, api_headers):
        """
        接口：TopContributors

        检查直播间最佳贡献者排名
        """
        with allure.step("检查this stream 最佳贡献者排名是否显示正常"):
            resp_stream = common.api_post(get_config_data['url'], api_headers, Payload.LiveRoomAPI().
                                          TopContributorsLivestream(get_config_data['follow_streamer']))
            print('00000000')
            print(resp_stream)
            amount_list = resp_stream['data']['userByDisplayName']['livestream']['topContributions']['list']
            l = len(amount_list)
            if l == 0:
                with allure.step('这个直播间暂时没有人做出贡献'):
                    print('这个直播间暂时没有人做出贡献')
            if l == 1:
                with allure.step('这个直播间只有一个人做出贡献而且贡献值是' + str(amount_list['amount'][:-5])):
                    print('这个直播间只有一个人做出贡献而且贡献值是' + str(amount_list['amount'][:-5]))
            if l > 1:
                with allure.step('这个直播间有多人做出贡献'):
                    a = 1
                    amount_new_list = []
                    for i in amount_list:
                        amount = str(i['amount'][:-5])
                        amount_new_list.append(amount)
                        with allure.step('THIS_STREAM第' + str(a) + '个人的贡献值是：' + amount):
                            print('THIS_STREAM第' + str(a) + '个人的贡献值是：' + amount)
                            a += 1
                    with allure.step('检查贡献者按照倒序排列'):
                        le = len(amount_new_list)
                        for j in range(l):
                            if j == le - 1:
                                break
                            else:
                                with allure.step('检查' + str(int(amount_new_list[j])) + '大于' +
                                                 str(int(amount_new_list[j + 1]))):
                                    assert int(amount_new_list[j]) >= int(amount_new_list[j + 1])

        with allure.step("检查THIS_MONTH最佳贡献者排名是否显示正常"):
            resp_month = common.api_post(get_config_data['url'], api_headers, Payload.LiveRoomAPI().TopContributors(
                get_config_data['follow_streamer'], 'THIS_MONTH'))
            amount_list1 = resp_month['data']['userByDisplayName']['topContributions']['list']
            l1 = len(amount_list1)
            if l1 == 0:
                with allure.step('这个月暂时没有人做出贡献'):
                    print('这个月暂时没有人做出贡献')
            if l1 == 1:
                with allure.step('这个月暂时只有一个人做出贡献， 而且贡献值是:' + str(amount_list1['amount'][:-5])):
                    print('这个月暂时只有一个人做出贡献， 而且贡献值是:' + str(amount_list1['amount'][:-5]))
            if l1 > 1:
                with allure.step('这个月有多人做出贡献'):
                    a = 1
                    amount_new_list1 = []
                    for i in amount_list1:
                        amount = str(i['amount'][:-5])
                        amount_new_list1.append(amount)
                        with allure.step('THIS_MONTH第' + str(a) + '个人的贡献值是：' + amount):
                            print('THIS_MONTH第' + str(a) + '个人的贡献值是：' + amount)
                            a += 1
                    with allure.step('检查贡献者按照倒序排列'):
                        le = len(amount_new_list1)
                        for j in range(l):
                            if j == le - 1:
                                break
                            else:
                                with allure.step('检查' + str(int(amount_new_list1[j])) + '大于' +
                                                 str(int(amount_new_list1[j + 1]))):
                                    assert int(amount_new_list1[j]) >= int(amount_new_list1[j + 1])

        with allure.step("检查ALL_TIME最佳贡献者排名是否显示正常"):
            resp_all = common.api_post(get_config_data['url'], api_headers, Payload.LiveRoomAPI().TopContributors(
                get_config_data['follow_streamer'], 'ALL_TIME'))
            amount_list2 = resp_all['data']['userByDisplayName']['topContributions']['list']
            l2 = len(amount_list2)
            if l2 == 0:
                with allure.step('开播到现在没人做出贡献值'):
                    print('开播到现在没人做出贡献值')
            if l2 == 1:
                with allure.step('开播到现在只有一个人做出贡献而且贡献值是' + str(amount_list2['amount'][:-5])):
                    print('开播到现在只有一个人做出贡献而且贡献值是' + str(amount_list2['amount'][:-5]))
            if l > 1:
                with allure.step('开播到现在有多人做出贡献而且贡献值是'):
                    a = 1
                    amount_new_list2 = []
                    for i in amount_list2:
                        amount = str(i['amount'][:-5])
                        amount_new_list2.append(amount)
                        with allure.step('ALL_TIME第' + str(a) + '个人的贡献值是：' + amount):
                            print('ALL_TIME第' + str(a) + '个人的贡献值是：' + amount)
                            a += 1
                    with allure.step('检查贡献者按照倒序排列'):
                        le = len(amount_new_list2)
                        for j in range(l):
                            if j == le - 1:
                                break
                            else:
                                with allure.step('检查' + str(int(amount_new_list2[j])) + '大于' +
                                                 str(int(amount_new_list2[j + 1]))):
                                    assert int(amount_new_list2[j]) >= int(amount_new_list2[j + 1])

    @allure.title('test_subscription_and_cancel_sub')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subscription_and_cancel_sub(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：AddSubscribe, MeSubscribing, UserUnsubscribe

        主播：automation去订阅并取消连续订阅
        """
        currentDateAndTime = datetime.now()
        currentTime = currentDateAndTime.strftime("%b %d, %Y")
        print("当前订阅时间：" + currentTime)
        next_month = currentDateAndTime + relativedelta(months=1)
        next_month_sub_date = next_month.strftime("%b %d, %Y")
        print("下次续费时间：" + next_month_sub_date)
        sub_streamer = get_config_data['subscription_streamer']
        print(sub_streamer)
        with allure.step("获取订阅前的lemon数量"):
            sub_before_lemon = common.get_account_lemon(get_config_data['url'], get_follow_streamer_auth_header)
            print("Before subscription lemon is: " + str(sub_before_lemon))
        with allure.step("用户：" + get_config_data['follow_streamer'] + "订阅主播间" + sub_streamer):
            sub_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                       Payload.LiveRoomAPI().AddSubscription(sub_streamer, 1))
            print(sub_resp)
        with allure.step("检查开始订阅的时间"):
            print("开始订阅的日期为：" + currentTime)
        with allure.step("检查返回error is Null, Cash back is Null"):
            assert sub_resp['data']['subscribeWithCashback']['err'] is None
            assert sub_resp['data']['subscribeWithCashback']['cashbacked'] is None
        time.sleep(60)
        with allure.step("获取订阅后的lemon数量"):
            sub_after_lemon = common.get_account_lemon(get_config_data['url'], get_follow_streamer_auth_header)
            print("Before subscription lemon is: " + str(sub_after_lemon))
        with allure.step("检查订阅后lemon是否只是扣了一个月298个lemon"):
            assert int(sub_after_lemon) + 298 == int(sub_before_lemon)
        with allure.step('检查订阅成功后，订阅时间续费时间是否正确'):
            next_month = currentDateAndTime + relativedelta(months=1)
            print('时间的下个月订阅的当天时间是：' + next_month.strftime("%b %d，%Y"))
            with allure.step('获取用户的订阅列表'):
                resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                       Payload.LiveRoomAPI().MeSubscribing())
                sub_list = resp['data']['me']['private']['subscribing']['list']
                for i in sub_list:
                    if i['streamer']['username'] == sub_streamer:
                        print('订阅主播成功')
                        assert True, '订阅主播不成功'
                        next_date = i['nextBillingAt']
                        date = (datetime.fromtimestamp(int(next_date) / 1000)).strftime("%b %d, %Y")
                        print('实际下一次扣费的时间是：' + date)
                        assert str(i['status']) == 'active', '订阅以后状态没更新，期望的是订阅以后状态变成active，' \
                                                             '而实际是： ' + str(i['status'])
                        assert str(next_month_sub_date) == str(date), '扣费时间不行，期望下次扣费时间是： ' + \
                                                                      str(next_month_sub_date) + '而实际是:' + str(date)
                        break
        with allure.step("检查是否能cancel订阅"):
            resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                   Payload.LiveRoomAPI().UserUnsubscribe(sub_streamer))
            time.sleep(60)
            cancel_sub = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                         Payload.LiveRoomAPI().MeSubscribing())
            sub_list1 = cancel_sub['data']['me']['private']['subscribing']['list']
            with allure.step('检查取消订阅成功与否'):
                assert resp['data']['unsubscribe']['err'] is None, '取消订阅不成功'
                for i in sub_list1:
                    if i['streamer']['username'] == sub_streamer:
                        assert str(i['status']) == 'p_cancel', '取消订阅以后状态没更新，期望的是取消订阅以后状态变成p_cancel' \
                                                               '而实际是： ' + str(i['status'])

    @allure.title('test_subscription_streamer_self')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subscription_streamer_self(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口：AddSubscribe
        主播：automation去订阅自己失败
        """
        sub_streamer = get_config_data['follow_streamer']
        with allure.step("用户：" + sub_streamer + "无法订阅自己"):
            sub_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                       Payload.LiveRoomAPI().AddSubscription(sub_streamer, 1))
            print(sub_resp)
            with allure.step('检查订阅自己时error code返回7004'):
                assert sub_resp['data']['subscribeWithCashback']['err']['code'] == 7004
            with allure.step('检查订阅自己时cashbacked返回None'):
                assert sub_resp['data']['subscribeWithCashback']['cashbacked'] is None

    @allure.title('test_ban_unban_chat_user')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ban_unban_chat_user(self, get_config_data, get_follow_streamer_auth_header,
                                 get_viewer1_login_auth_header):
        """
        接口：BanStreamChatUser, UnbanStreamChatUser, SendMessage
        测试主播：automation ban和unban 用户并发送信息
        """
        streamer = get_config_data['follow_streamer']
        user = get_config_data['viewer1_username']
        before_ban_user_message = ' before ban test ban user'
        ban_message = 'ban user test'
        after_unban_user_message = 'after ban test unban user'
        verify_message = 'message.AddMessage banned from stream chat'
        with allure.step('检查用户被ban 之前能发信息'):
            before_response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                   Payload.LiveRoomAPI().send_chat(streamer, before_ban_user_message,
                                                                                   [0, 2]))
            print(before_response_json)
            with allure.step('检查返回值不报错'):
                assert before_response_json['data']['sendStreamchatMessage']['err'] is None
            with allure.step('检查返回的信息就是发送的信息'):
                assert before_response_json['data']['sendStreamchatMessage']['message']['content'] == \
                       before_ban_user_message
        with allure.step("主播：" + streamer + "开始ban 用户" + user + '返回值无报错'):
            ban_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                       Payload.LiveRoomAPI().BanStreamChatUser(streamer, user))
            assert ban_resp['data']['streamchatUserBan']['err'] is None
        with allure.step('检查用户被ban 之后不能发信息'):
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.LiveRoomAPI().send_chat(streamer,
                                                                            ban_message, [0, 2]))
            print(response_json)
            assert response_json['data']['sendStreamchatMessage']['err']['code'] == 6001
            assert response_json['data']['sendStreamchatMessage']['err']['message'] == verify_message
        with allure.step('检查unban 用户之后能发信息'):
            unban_resp = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                         Payload.LiveRoomAPI().UnbanStreamChatUser(streamer, user))
            with allure.step("主播：" + streamer + "unban 用户" + user + '返回值无报错'):
                assert unban_resp['data']['streamchatUserUnban']['err'] is None
            after_response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                  Payload.LiveRoomAPI().send_chat(streamer,
                                                                                  after_unban_user_message, [0, 2]))
            print(after_response_json)
            with allure.step('检查返回的信息就是发送的信息'):
                assert after_response_json['data']['sendStreamchatMessage']['message']['content'] == \
                       after_unban_user_message

    @allure.title('test_setModerator')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Moderator1_add(self, get_config_data, get_follow_streamer_auth_header, get_viewer1_login_auth_header):
        """
        接口：AddModerator, DeleteChat
        测试主播：automation 设置 automation_viewer1 as moderator
        """
        streamer = get_config_data['follow_streamer']
        streamer_displayName = get_config_data['follow_displayName']
        user = get_config_data['viewer1_username']
        with allure.step('设置直播间Moderator'):
            response_json = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                            Payload.LiveRoomAPI().AddModerator(streamer, user))
            with allure.step('检查返回的信息无error'):
                assert response_json['data']['moderatorAdd']['err'] is None
            with allure.step('检查Moderator 用户在Moderator 列表'):
                response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                           Payload.LiveRoomAPI().StreamChatModerators(streamer_displayName))
                m_list = response['data']['userByDisplayName']['chatModerators']['list']
                for i in m_list:
                    if i['username'] == user:
                        assert True, 'The Moderator 不在Moderator列表'
                        break
        with allure.step('Moderator是否可以删除主播的信息'):
            message = 'add Moderator'
            response_json = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                            Payload.LiveRoomAPI().send_chat(streamer, message, [0, 2]))
            message_id = response_json['data']['sendStreamchatMessage']['message']['id']
            with allure.step('Moderator开始删除信息'):
                response_json1 = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                                 Payload.LiveRoomAPI().DeleteChat(streamer, message_id))
                assert response_json1['data']['chatDelete']['err'] is None, 'Moderator删除信息失败'

    @allure.title('test_RemoveModerator')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Moderator2_detele(self, get_config_data, get_follow_streamer_auth_header, get_viewer1_login_auth_header):
        """
        接口：RemoveModerator, DeleteChat
        测试主播：automation moderator： automation_viewer1
        """
        streamer = get_config_data['follow_streamer']
        streamer_displayName = get_config_data['follow_displayName']
        user = get_config_data['viewer1_username']
        moderator_exists = False
        with allure.step('检查删除之前Moderator在Moderator列中'):
            b_response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                         Payload.LiveRoomAPI().StreamChatModerators(streamer_displayName))
            b_list = b_response['data']['userByDisplayName']['chatModerators']['list']
            print(b_list)
            for i in b_list:
                if i['username'] == user:
                    moderator_exists = True
                    break
        if moderator_exists is False:
            print('要删除的Moderator不在Moderator列中')
            assert False
        else:
            with allure.step('删除Moderator'):
                response_json = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                                Payload.LiveRoomAPI().RemoveModerator(streamer, user))
                with allure.step('检查返回的信息无error'):
                    assert response_json['data']['moderatorRemove']['err'] is None
                with allure.step('检查删除的Moderator 用户不在Moderator 列表'):
                    response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                               Payload.LiveRoomAPI().StreamChatModerators(streamer_displayName))
                    m_list = response['data']['userByDisplayName']['chatModerators']['list']
                    assert not any(user == item for item in m_list), 'Moderator删除以后还在Moderator列表中'

    @allure.title('test_MeModLogs')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_MeModLogs(self, get_config_data, get_follow_streamer_auth_header):
        """
        接口： MeModLogs
        检查dashboard ->Moderator Log页面无报错
        """
        with allure.step('检查dashboard ->Moderator Log页面无报错'):
            response = common.api_post(get_config_data['url'], get_follow_streamer_auth_header,
                                       Payload.LiveRoomAPI().MeModLogs())
            print(response['data'])
            assert not any('err' == item for item in str(response['data'])), '接口返回值有报错'

    @allure.title('test_replay')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_replay(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：LivestreamProfileReplay
        检查replay数据返回没报错
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('检查replay数据返回没报错'):
            response = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                       Payload.LiveRoomAPI().LivestreamProfileReplay(
                                           get_config_data['replay_streamer']))
            assert response['data']['userByDisplayName']['pastBroadcastsV2']['list'] is not None
            assert not any('err' == item for item in str(response['data'])), '接口返回值有报错'

    @allure.title('test_replay_addWatch')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_replay_addWatch(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：AddWatch
        检查replay add watch接口数据返回没报错
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('检查replay add watch接口数据返回没报错'):
            response = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                       Payload.LiveRoomAPI().AddWatch(
                                           get_config_data['replay_streamer_permlink']))
            assert not any('err' == item for item in str(response['data'])), '接口返回值有报错'

    @allure.title('test_replay_PastBroadcastPage')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_replay_PastBroadcastPage(self, get_config_data, get_viewer1_login_auth_header):
        """
        接口：PastBroadcastPage
        检查replay PastBroadcastPage接口数据返回没报错
        :param get_config_data:
        :param get_viewer1_login_auth_header:
        :return:
        """
        with allure.step('检查replay PastBroadcastPage接口数据返回没报错'):
            response = common.api_post(get_config_data['url'], get_viewer1_login_auth_header,
                                       Payload.LiveRoomAPI().PastBroadcastPage(
                                           get_config_data['replay_streamer_permlink']))
            assert not any('err' == item for item in str(response['data'])), '接口返回值有报错'


if __name__ == '__main__':
    print('e2rwf')
    print(os.getcwd())
    pytest.main(['./test_liveroom.py', '--alluredir', './report/results-20230627'])
    os.system('allure generate ./report/results-20230627 -o ./report/report-20230627 --clean')
