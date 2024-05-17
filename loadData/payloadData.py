def normal_header():
    headers = {
        'Content-Type': 'application/json'
    }
    return headers


def normal_header():
    headers = {
        'Content-Type': 'application/json'
    }
    return headers


def login(email, password):
    payload = {
        "operationName": "EmailLogin",
        "variables": {
            "email": email,
            "password": password,
            "recaptchaToken": 'fewvqv',
        },
        "query": "mutation EmailLogin($email: String!, $password: String!, $recaptchaToken: String, $deviceType: "
                 "DeviceType) {\n  loginWithEmail(email: $email, password: $password, recaptchaToken: $recaptchaToken,"
                 " deviceType: $deviceType) {\n    me {\n      id\n      private {\n        accessToken\n        "
                 "__typename\n      }\n      __typename\n    }\n    twofactorToken\n    err {\n      code\n      "
                 "message\n      __typename\n    }\n    __typename\n  }\n}\n"
    }
    return payload


def follow_user(user_id):
    payload = {
        "operationName": "FollowUser",
        "variables": {
            "streamer": user_id
        },
        "query": "mutation FollowUser($streamer: String!) {follow(streamer: $streamer) {err {code message}}}"
    }
    return payload


def sidebar_follow_user_list():  # 获取sidebar following list
    payload = {
        "operationName": "MeSidebar",
        "variables": {
            "folowingFirst": 500,
            "after": "MeSidebar"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "14cff202984215984934df214bacf048befd9d8dc21791b0391ce65bd2981484"
            }
        }
    }

    return payload


def unfollow_user(user_id):
    payload = {
        "operationName": "UnfollowUser",
        "query": "mutation UnfollowUser($streamer: String!) {\n  unfollow(streamer: $streamer) {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n",

        "variables": {
            "streamer": user_id
        }
    }
    return payload


def me_clips_of_me():
    payload = {
        "operationName": "MeClipsOfMe",
        "variables": {
            "first": 20,
            "order": "Upvotes",
            "showUnpicked": True
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "18dd1600a3edf816e14823421c8b5bce5c1549bb7a6e5d0435464e12d23252f4"
            }
        }
    }
    return payload


def me_clips_by_me():
    payload = {
        "operationName": "MeClipsByMe",
        "variables": {
            "first": 20,
            "order": "Upvotes",
            "showUnpicked": True
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "ed003aaf2752edee54bf2ae51c074ba65fdb6eaa603db9ba3d17d0bb288bb761"
            }
        }
    }
    return payload


def get_today_token_limit():  # 获取体现额度
    payload = {
        "operationName": "GetTodayTokenLimit",
        "variables": {},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "30f628ded36de5fdc2d3be5a8b1c45287333c7a2f940e6bbfe23f8310ce2d76f"
            }
        }
    }
    return payload


def MeBalance():
    payload = {
        "operationName": "MeBalance",
        "variables": {},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "6e6794dcd570ff8ed544d45483971969db2c8e968a3a082645ae92efa124f3ec"
            }
        }
    }
    return payload


def MeRebillyCards():
    payload = {
        "operationName": "MeRebillyCards",
        "variables": {},
        "query": "query MeRebillyCards {\n  me {\n    ...MeRebillyCardsFrag\n    __typename\n  }\n}\n\nfragment MeRebillyCardsFrag on User {\n  id\n  private {\n    userRebillyCards {\n      brand\n      last4\n      id\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
    }
    return payload


def ActivityUserDonationRank(username, rankingType):
    payload = {
          "operationName": "ActivityUserDonationRank",
          "variables": {
            "username": username,
            "rankingType": rankingType,
            "isStreamer": True
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "5ff007e457c354fc042cd9ef637babac993c1c92c917650b152bbf4cd5fd1a20"
            }
          },
          "query": "query ActivityUserDonationRank($username: String!, $rankingType: RankingType!, $isStreamer: Boolean!) {\n  userDonationRank(username: $username, rankingType: $rankingType, isStreamer: $isStreamer) {\n    __typename\n    rank\n    user {\n      displayname\n      __typename\n    }\n    amount\n  }\n}\n"
        }
    return payload


def live_streams_languages():
    payload = {
        "operationName": "LivestreamsLanguages",
        "variables": {},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "5a2ac0ba175c8e440b5eb1441a75c3cdececd213a33712ad14a12bd67ab1b9df"
            }
        },
        "query": "query LivestreamsLanguages($categoryID: Int) {\n  languages(categoryID: $categoryID) {\n    ...LanguageFrag\n    __typename\n  }\n}\n\nfragment LanguageFrag on Language {\n  id\n  backendID\n  language\n  code\n  __typename\n}\n"
    }
    return payload


def advertises():
    payload = {
        "operationName": "advertises",
        "variables": {
            "info": {
                "positions": [
                    "carousel_left",
                    "carousel_right",
                    "livestream"]
            }
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "e191582dab63048caae40cc6ee7d0a43fa14f6f3666a4dfa0fa47dc1b1981546"
            }
        }
    }
    return payload


def me_global():  # 个人的一些信息
    payload = {
        "operationName": "MeGlobal",
        "variables": {},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "34f843ef6ae287e477e08dc0a6a21f8fd7cb96f7fce9806492ddde45db6ab8e1"
            }
        }
    }
    return payload


def test_me_balance():
    payload = {

        "operationName": "MeBalance",
        "variables": {},
        "query": "query MeBalance {me {id wallet {balance}}}"
    }
    return payload


def global_information():
    payload = {
        "operationName": "GlobalInformation",
        "variables": {
            "limit": 10,
            "languageCode": ""
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "8492b145b14af44ec710eba6c57071cff98d9508f10b59bfaec1ea9b3384f3c7"
            }
        }
    }
    return payload


def me_livestream():
    payload = {
        "operationName": "MeLivestream",
        "variables": {
            "isLoggedIn": True
        },
        "query": "query MeLivestream($isLoggedIn: Boolean!) {me {...MeLivestreamFrag __typename}}fragment MeLivestreamFrag on User "
                 "{id ...MeLivestreamChatroomFrag __typename}fragment MeLivestreamChatroomFrag on User {id username role "
                 "myChatBadges ...EmojiFrag ...MeEmoteFrag ...MeStreamChatModeSettingFrag __typename}fragment MeEmoteFrag on User {"
                 "id role @include(if: $isLoggedIn)emote {...EmoteMineFrag ...EmoteChannelFrag ...EmoteGlobalFrag ...EmoteVipFrag __typename }__typename}"
                 "fragment EmoteMineFrag on AllEmotes {mine {list {name username sourceURL mimeType level type __typename}__typename}__typename}"
                 "fragment EmoteChannelFrag on AllEmotes {channel {list {name username sourceURL mimeType level type __typename}__typename}__typename}"
                 "fragment EmoteGlobalFrag on AllEmotes {global {list {name username sourceURL mimeType level type __typename}__typename}__typename}"
                 "fragment EmoteVipFrag on AllEmotes {vip {list {name username sourceURL mimeType level type__typename}__typename}__typename}"
                 "fragment MeStreamChatModeSettingFrag on User {id private {displaySetting {lemon icecream diamond ninjaghini "
                 "ninjet follow subscription hosting moderation chat stickers __typename}__typename}__typename}"
                 "fragment EmojiFrag on User {id emoji {...EmojiGlobalFrag ...EmojiVipFrag __typename}__typename}"
                 "fragment EmojiGlobalFrag on AllEmojis {global {totalCount list { name username sourceURL mimeType level type "
                 "__typename}__typename}__typename}"
                 "fragment EmojiVipFrag on AllEmojis {vip {totalCount list {name username sourceURL mimeType level type __typename}__typename}__typename}"
    }
    return payload


def browser_register_notification(token):
    payload = {
        "operationName": "BrowserRegisterNotification",
        "variables": {
            "token": token
        },
        "query": "mutation BrowserDeregisterNotification($token: String!) {browserDeregisterNotification(token: $token) {err {message code __typename}__typename}}"
    }
    return payload


class DaskboardAPI:
    @staticmethod
    def StreamHostDelete(username):
        payload = {
            "operationName": "StreamHostDelete",
            "variables": {
                "username": username
            },
            "query": "mutation StreamHostDelete($username: String!) {hostDelete(username: $username) {err {code __typename}__typename}}"
        }
        return payload

    @staticmethod
    def StreamHostSet(username):
        payload = {
          "operationName": "StreamHostSet",
          "variables": {
            "username": username
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "c4c11c7881c2516b8aeae032be6280fbb944a38af2b66ae32dba9d07da788260"
            }
          },
          "query": "mutation StreamHostSet($username: String!) {\n  hostSet(username: $username) {\n    livestream {\n      id\n      permlink\n      creator {\n        id\n        username\n        ...VDliveAvatarFrag\n        ...VDliveNameFrag\n        __typename\n      }\n      ...VVideoPlayerFrag\n      __typename\n    }\n    err {\n      code\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment VVideoPlayerFrag on Livestream {\n  permlink\n  disableAlert\n  encryptedStream\n  ageRestriction\n  category {\n    id\n    title\n    __typename\n  }\n  tags\n  language {\n    id\n    language\n    __typename\n  }\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def MEDashboard(username):
        payload = {
          "operationName": "MeDashboard",
          "variables": {
            "isLoggedIn": True,
            "input": {
              "operator": username,
              "operation": "",
              "first": 10,
              "after": ""
            }
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "78e83028a2c6203c4ac6e2cdccd1cb162f061d7fcf7e64ce7f851b618116af1c"
            }
          },
          "query": "query MeDashboard($isLoggedIn: Boolean!) {\n  me {\n    ...MeDashboardFrag\n    __typename\n  }\n}\n\nfragment MeDashboardFrag on User {\n  id\n  canSubscribe\n  private {\n    emailVerified\n    __typename\n  }\n  ...DashboardStreamSettingsFrag\n  ...DashboardHostSettingFrag\n  ...DashboardStreamChatroomFrag\n  ...DashboardActivityFeedFrag\n  ...DashboardOfflineImageSettingFrag\n  ...DashboardRerunSettingsFrag\n  ...DashboardSubscriptionSettingFrag\n  __typename\n}\n\nfragment DashboardStreamSettingsFrag on User {\n  livestream {\n    id\n    permlink\n    ...VVideoPlayerFrag\n    __typename\n  }\n  hostingLivestream {\n    id\n    permlink\n    creator {\n      id\n      username\n      ...VDliveAvatarFrag\n      ...VDliveNameFrag\n      __typename\n    }\n    ...VVideoPlayerFrag\n    __typename\n  }\n  private {\n    streamTemplate {\n      title\n      ageRestriction\n      earnRestriction\n      thumbnailUrl\n      disableAlert\n      category {\n        id\n        backendID\n        title\n        __typename\n      }\n      language {\n        id\n        backendID\n        code\n        language\n        __typename\n      }\n      tags\n      saveReplay\n      __typename\n    }\n    filterWords\n    __typename\n  }\n  __typename\n}\n\nfragment VVideoPlayerFrag on Livestream {\n  permlink\n  disableAlert\n  encryptedStream\n  ageRestriction\n  category {\n    id\n    title\n    __typename\n  }\n  tags\n  language {\n    id\n    language\n    __typename\n  }\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment DashboardHostSettingFrag on User {\n  id\n  hostingLivestream {\n    creator {\n      id\n      username\n      ...VDliveAvatarFrag\n      ...VDliveNameFrag\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DashboardStreamChatroomFrag on User {\n  ...MeLivestreamChatroomFrag\n  __typename\n}\n\nfragment MeLivestreamChatroomFrag on User {\n  id\n  username\n  role\n  myChatBadges\n  ...EmojiFrag\n  ...MeEmoteFrag\n  ...MeStreamChatModeSettingFrag\n  __typename\n}\n\nfragment MeEmoteFrag on User {\n  id\n  role @include(if: $isLoggedIn)\n  emote {\n    ...EmoteMineFrag\n    ...EmoteChannelFrag\n    ...EmoteGlobalFrag\n    ...EmoteVipFrag\n    __typename\n  }\n  __typename\n}\n\nfragment EmoteMineFrag on AllEmotes {\n  mine {\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmoteChannelFrag on AllEmotes {\n  channel {\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmoteGlobalFrag on AllEmotes {\n  global {\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmoteVipFrag on AllEmotes {\n  vip {\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment MeStreamChatModeSettingFrag on User {\n  id\n  private {\n    displaySetting {\n      lemon\n      icecream\n      diamond\n      ninjaghini\n      ninjet\n      follow\n      subscription\n      hosting\n      moderation\n      chat\n      stickers\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiFrag on User {\n  id\n  emoji {\n    ...EmojiGlobalFrag\n    ...EmojiVipFrag\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiGlobalFrag on AllEmojis {\n  global {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiVipFrag on AllEmojis {\n  vip {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DashboardActivityFeedFrag on User {\n  id\n  ...ActivityFeedFrag\n  __typename\n}\n\nfragment ActivityFeedFrag on User {\n  id\n  username\n  displayname\n  ...VStreamChatRowStreamerFrag\n  ...ActivityFeedSettingsFrag\n  chats(count: 50) {\n    type\n    ... on ChatGift {\n      id\n      gift\n      amount\n      message\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    ... on ChatHost {\n      id\n      viewer\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    ... on ChatSubscription {\n      id\n      month\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    ... on ChatExtendSub {\n      id\n      month\n      length\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatGiftSub {\n      id\n      ...VStreamChatSenderInfoFrag\n      count\n      receiver\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatGiftSubReceive {\n      id\n      ...VStreamChatSenderInfoFrag\n      gifter\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatFollow {\n      id\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VStreamChatRowStreamerFrag on User {\n  displayname\n  isMe @include(if: $isLoggedIn)\n  ...VStreamChatRowSenderInfoStreamerFrag\n  ...VStreamChatProfileCardStreamerFrag\n  ...StreamChatTextRowStreamerFrag\n  __typename\n}\n\nfragment VStreamChatRowSenderInfoStreamerFrag on User {\n  id\n  subSetting {\n    badgeText\n    badgeColor\n    textColor\n    streakTextColor\n    __typename\n  }\n  __typename\n}\n\nfragment VStreamChatProfileCardStreamerFrag on User {\n  id\n  username\n  myRoomRole @include(if: $isLoggedIn)\n  role\n  __typename\n}\n\nfragment StreamChatTextRowStreamerFrag on User {\n  id\n  username\n  myRoomRole @include(if: $isLoggedIn)\n  mySubscription @include(if: $isLoggedIn) {\n    isSubscribing\n    __typename\n  }\n  chatBannedEmoji\n  emote @include(if: $isLoggedIn) {\n    channel {\n      list {\n        name\n        username\n        sourceURL\n        mimeType\n        level\n        type\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  subSetting {\n    streakTextColor\n    __typename\n  }\n  __typename\n}\n\nfragment ActivityFeedSettingsFrag on User {\n  id\n  private {\n    activitySetting {\n      lemon\n      icecream\n      diamond\n      ninjaghini\n      ninjet\n      follow\n      subscription\n      hosting\n      moderation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VStreamChatSenderInfoFrag on SenderInfo {\n  subscribing\n  role\n  roomRole\n  sender {\n    id\n    username\n    displayname\n    avatar\n    partnerStatus\n    badges\n    effect\n    __typename\n  }\n  __typename\n}\n\nfragment DashboardOfflineImageSettingFrag on User {\n  id\n  partnerStatus\n  offlineImage\n  __typename\n}\n\nfragment DashboardRerunSettingsFrag on User {\n  id\n  private {\n    rerunSetting {\n      enabled\n      presets {\n        pastbroadcast {\n          permlink\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment DashboardSubscriptionSettingFrag on User {\n  id\n  private {\n    showSubSettingTab\n    __typename\n  }\n  ...SettingsSubscribeFrag\n  __typename\n}\n\nfragment SettingsSubscribeFrag on User {\n  id\n  subSetting {\n    badgeColor\n    badgeText\n    textColor\n    streakTextColor\n    benefits\n    backgroundImage\n    __typename\n  }\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def DashBoardSearchTags(searchText):
        payload = {
              "operationName": "DashBoardSearchTags",
              "variables": {
                "text": searchText
              },
              "extensions": {
                "persistedQuery": {
                  "version": 1,
                  "sha256Hash": "6941f74b248c6b1a2045742c053865a91576fd8e03e71ce9982dfa0a781c2d3f"
                }
              },
              "query": "query DashBoardSearchTags($text: String!) {\n  tags(text: $text)\n}\n"
            }
        return payload

    @staticmethod
    def DashboardSearchCategories(searchText):
        payload = {
            "operationName": "DashboardSearchCategories",
            "variables": {
                "text": searchText
            },
            "query": "query DashboardSearchCategories($text: String!, $first: Int, $after: String) {search(text: $text) {categories(first: $first, after: $after) {pageInfo {endCursor hasNextPage __typename}list {id backendID title __typename}__typename}__typename}}"
        }
        return payload

    @staticmethod
    def RerunEnableSwitch():
        payload = {
            "operationName": "RerunEnableSwitch",
            "variables": {},
            "query": "mutation RerunEnableSwitch {rerunEnable {err {code message __typename}__typename}}"
        }
        return payload

    @staticmethod
    def RerunDisableSwitch():
        payload = {
            "operationName": "RerunDisableSwitch",
            "variables": {},
            "query": "mutation RerunDisableSwitch {rerunDisable {err {code message __typename}__typename}}"
        }
        return payload

    @staticmethod
    def SetStreamTemplate(title, ageRestriction, earnRestriction, categoryID, languageID, thumbnailUrl, disableAlert,
                          saveReplay, tags: []):
        payload = {
            "operationName": "SetStreamTemplate",
            "variables": {
                "template": {
                    "title": title,
                    "ageRestriction": ageRestriction,
                    "earnRestriction": earnRestriction,
                    "categoryID": categoryID,
                    "languageID": languageID,
                    "thumbnailUrl": thumbnailUrl,
                    "disableAlert": disableAlert,
                    "saveReplay": saveReplay,
                    "tags": tags
                }
            },
            "query": "mutation SetStreamTemplate($template: SetStreamTemplateInput!) {\n  streamTemplateSet(template: $template) {\n    err {\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        return payload

    @staticmethod
    def SetSubSettings(benefits, badgeColor, badgeText, textColor, streakTextColor, backgroundImage):
        payload = {
            "operationName": "SetSubSettings",
            "variables": {
                "badgeColor": badgeColor,
                "badgeText": badgeText,
                "textColor": textColor,
                "streakTextColor": streakTextColor,
                "benefits": [benefits],
                "backgroundImage": backgroundImage
            },
            "query": "mutation SetSubSettings($badgeText: String!, $badgeColor: String!, $textColor: String!, $backgroundImage: String, $streakTextColor: String, $benefits: [String!]) {\n  subSettingSet(subSetting: {badgeColor: $badgeColor, badgeText: $badgeText, textColor: $textColor, streakTextColor: $streakTextColor, benefits: $benefits, backgroundImage: $backgroundImage}) {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        return payload


class LiveRoomAPI:
    @staticmethod
    def Live_stream_profile_following(streamer_display_name):  # 主播关注的直播间
        payload = {
              "operationName": "LivestreamProfileFollowing",
              "variables": {
                "displayname": streamer_display_name,
                "sortedBy": "AZ",
                "first": 20,
                "isLoggedIn": True
              },
              "query": "query LivestreamProfileFollowing($displayname: String!, $sortedBy: RelationSortOrder, $first: Int, $after: String, $isLoggedIn: Boolean!) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    displayname\n    following(sortedBy: $sortedBy, first: $first, after: $after) {\n      pageInfo {\n        endCursor\n        hasNextPage\n        __typename\n      }\n      list {\n        ...VDliveAvatarFrag\n        ...VDliveNameFrag\n        ...VFollowFrag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment VFollowFrag on User {\n  id\n  username\n  displayname\n  isFollowing @include(if: $isLoggedIn)\n  isMe @include(if: $isLoggedIn)\n  followers {\n    totalCount\n    __typename\n  }\n  __typename\n}\n"
            }

        return payload

    @staticmethod
    def Live_stream_profile_followers(streamer_display_name):  # 其他关注主播的主播
        payload = {
              "operationName": "LivestreamProfileFollowers",
              "variables": {
                "displayname": streamer_display_name,
                "sortedBy": "AZ",
                "first": 20,
                "isLoggedIn": True
              },
              "query": "query LivestreamProfileFollowers($displayname: String!, $sortedBy: RelationSortOrder, $first: Int, $after: String, $isLoggedIn: Boolean!) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    displayname\n    followers(sortedBy: $sortedBy, first: $first, after: $after) {\n      pageInfo {\n        endCursor\n        hasNextPage\n        __typename\n      }\n      list {\n        ...VDliveAvatarFrag\n        ...VDliveNameFrag\n        ...VFollowFrag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment VFollowFrag on User {\n  id\n  username\n  displayname\n  isFollowing @include(if: $isLoggedIn)\n  isMe @include(if: $isLoggedIn)\n  followers {\n    totalCount\n    __typename\n  }\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def donate_lemon(streamer_permlink, account):  # 打赏lemon
        payload = {
            "operationName": "StreamDonate",
            "variables": {
                "input": {
                    "permlink": streamer_permlink,
                    "type": "LEMON",
                    "count": int(account),
                    "message": ""
                }
            },
            "query": "mutation StreamDonate($input: DonateInput!) {donate(input: $input) {id recentCount expireDuration "
                     "err {code message}}}"
        }
        return payload

    @staticmethod
    def add_gift_sub(streamer_name, count):  # 分发gift sub
        payload = {
            "operationName": "AddGiftSub",
            # "query": 'mutation AddGiftSub($streamer: String!, $toUser: String, $count: Int) {giftSub(streamer: $streamer, toUser: $toUser, count: $count) '
            #          '{ err { code message __typename} __typename}}',
            "variables": {
                "streamer": streamer_name,
                "count": int(count)
            },
            'query': 'mutation AddGiftSub($streamer: String!, $toUser: String, $count: Int) {giftSub(streamer: $streamer, toUser: $toUser, count: $count) {err {code message}}}'
        }
        return payload

    @staticmethod
    def add_gift_sub_claim(streamer_name):  # 领取gift sub
        payload = {
            "operationName": "AddGiftSubClaim",
            "variables": {
                "streamer": streamer_name
            },
            'query': 'mutation AddGiftSubClaim($streamer: String!) {giftSubClaim(streamer: $streamer) {err {code message}}}'
        }
        return payload

    @staticmethod
    def send_chat(stream_name, message, emoList: []):  # 直播间发信息
        payload = {
              "operationName": "SendStreamChatMessage",
              "variables": {
                "input": {
                  "streamer": stream_name,
                  "message": message,
                  "roomRole": "Owner",
                  "subscribing": True,
                  "emojis": emoList
                }
              },
              "query": "mutation SendStreamChatMessage($input: SendStreamchatMessageInput!) {\n  sendStreamchatMessage(input: $input) {\n    err {\n      message\n      code\n      __typename\n    }\n    message {\n      type\n      ... on ChatText {\n        id\n        emojis\n        content\n        createdAt\n        subLength\n        ...VStreamChatSenderInfoFrag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VStreamChatSenderInfoFrag on SenderInfo {\n  subscribing\n  role\n  roomRole\n  sender {\n    id\n    username\n    displayname\n    avatar\n    partnerStatus\n    badges\n    effect\n    __typename\n  }\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def LivestreamTreasureChestAddPoints(streamerDisplayName):
        payload = {
            "operationName": "LivestreamTreasureChestAddPoints",
            "variables": {
                "displayname": streamerDisplayName
            },
            "query": "query LivestreamTreasureChestAddPoints($displayname: String!) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    ...TreasureChestAddPointsFrag\n    __typename\n  }\n}\n\nfragment TreasureChestAddPointsFrag on User {\n  id\n  treasureChest {\n    userTransferSetting {\n      weeklyTransferTotalQuota\n      weeklyTransferQuotaLeft\n      __typename\n    }\n    __typename\n  }\n  wallet {\n    balance\n    __typename\n  }\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def LivestreamTreasureChestAddCheck(streamerDisplayName, amount):  # 加lemon 进宝箱
        payload = {
            "operationName": "LivestreamTreasureChestAddCheck",
            "variables": {
                "displayname": streamerDisplayName,
                "amount": amount
            },
            "query": "query LivestreamTreasureChestAddCheck($displayname: String!, $amount: String!) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    ...TreasureChestValidTransferFrag\n    __typename\n  }\n}\n\nfragment TreasureChestValidTransferFrag on User {\n  id\n  treasureChest {\n    validUserTransfer(amount: $amount)\n    __typename\n  }\n  wallet {\n    balance\n    __typename\n  }\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def ChestUserTransfer(amount):
        payload = {
            "operationName": "ChestUserTransfer",
            "variables": {
                "amount": amount
            },
            "query": "mutation ChestUserTransfer($amount: String!) {\n  treasureChestUserTransfer(amount: $amount) {\n    err {\n      message\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        return payload

    @staticmethod
    def give_away_start():  # 主播开启宝箱
        payload = {
            "operationName": "GiveawayStart",
            "variables": {},
            "query": "mutation GiveawayStart {\n  giveawayStart {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        return payload

    @staticmethod
    def give_away_claim(streamer_name):  # 用户抢宝箱
        payload = {
            "operationName": "GiveawayClaim",
            "variables": {
                "streamer": streamer_name
            },
            "query": "mutation GiveawayClaim($streamer: String!) {\n  giveawayClaim(streamer: $streamer) {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        return payload

    @staticmethod
    def LivestreamTreasureChestWinners(streamer_name):  # 宝箱中奖名单
        payload = {
            "operationName": "LivestreamTreasureChestWinners",
            "variables": {
                "displayname": streamer_name,
                "isLoggedIn": True
            },
            "query": "query LivestreamTreasureChestWinners($displayname: String!, $isLoggedIn: Boolean!) {"
                     "userByDisplayName(displayname: $displayname) {id"
                     "...TreasureChestWinnersFrag __typename}}"
                     "fragment TreasureChestWinnersFrag on User {id username isMe @include(if: $isLoggedIn)"
                     "treasureChest {myLastGiveawayReward @include(if: $isLoggedIn) {"
                     "... on GiveawayHappyHourTicketReward {type value __typename}"
                     "... on GiveawayMoneyReward {type value __typename} __typename} lastGiveawayRewards {"
                     "... on GiveawayHappyHourTicketReward {type value user {"
                     "...VDliveAvatarFrag displayname __typename} __typename}"
                     "... on GiveawayMoneyReward {type value user {"
                     "...VDliveAvatarFrag displayname __typename }__typename}__typename}__typename}__typename}"
                     "fragment VDliveAvatarFrag on User {id avatar effect __typename}"
        }
        return payload

    @staticmethod
    def ClipAdd(streamerPermlink, streamerName, clipUrl, desc, thumbnailUrl, sendChat=True, startTime=0, endTime=60):
        payload = {
            "operationName": "ClipAdd",
            "variables": {
                "permlink": streamerPermlink,
                "url": clipUrl,
                "streamer": streamerName,
                "description": desc,
                "thumbnailUrl": thumbnailUrl,
                "sendChat": sendChat,
                "startTime": startTime,
                "endTime": endTime,
                "recaptchaToken": "03AAYGu2S8w6F90RZCmWzdnRLuFbiVPyuHk4PhyELecbm8kVPVk2LeZH0wULPtlFdVMu3d50GBgAyFmjMjR9F7zMnv2jAfo_HPqgmWE4MlaTKa5nY6cBBd2a3-t-0HV6Rg_339ujmZTtR-xzCVLKn0WGzfRfnToy-Ex7CRZRjAb2Qp9ffVy0nYhNMuxi9X-ODN4I7v1l5VmpDGISDTVd8-1fxJChj3YJyYbk1et_LPnvvCi69fByLnSKQBwxLR7aRQjX2vWBeTbi3dfCXySSZI2ssrPSE8mbkGnDmDSvFyuBWnOVQQe0isNsVFlBF4fdJ7U11A-SYg_og-gCdmaRSwkd48zI16TsDQxUODVLj2COX_aIWUbn23LxIFbIrJAEAdrL1SdgDLEW9LDOsi3VLHLoTETltoiDNyTK45pAfZxbiBIT8LRP49bKUxCz_yoBIRPYg0on7uLXn77hhMSYsoYoy8j1bLhDso6Gq0R9B6jc_JXKMrnD7eMfAd8mzijmlK5AwUwjLu6GAW9rg2Qmw_2-q4ZkILkczbBkvrXiQMAJZr6N5CC5TSUzI"
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "6a4ce76f11d29a750c535bd5558afb71d862241b592189a9799da70fce4a986c"
                }
            }
        }
        return payload

    @staticmethod
    def ClipViewAdd(id):
        payload = {
            "operationName": "ClipViewAdd",
            "variables": {
                "id": id
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "afb2d85295db3fe9426254c342514d00093952d6a19f669ac56c3435007f2695"
                }
            }
        }
        return payload

    @staticmethod
    def MeLivestream(isLoginIn=True):
        payload = {
            "operationName": "MeLivestream",
            "variables": {
                "isLoggedIn": isLoginIn
            },
            "query": "query MeLivestream($isLoggedIn: Boolean!) {\n  me {\n    ...MeLivestreamFrag\n    __typename\n  }\n}\n\nfragment MeLivestreamFrag on User {\n  id\n  ...MeLivestreamChatroomFrag\n  __typename\n}\n\nfragment MeLivestreamChatroomFrag on User {\n  id\n  username\n  role\n  myChatBadges\n  ...EmojiFrag\n  ...MeEmoteFrag\n  ...MeStreamChatModeSettingFrag\n  __typename\n}\n\nfragment MeEmoteFrag on User {\n  id\n  role @include(if: $isLoggedIn)\n  emote {\n    ...EmoteMineFrag\n    ...EmoteChannelFrag\n    ...EmoteGlobalFrag\n    ...EmoteVipFrag\n    __typename\n  }\n  __typename\n}\n\nfragment EmoteMineFrag on AllEmotes {\n  mine {\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmoteChannelFrag on AllEmotes {\n  channel {\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmoteGlobalFrag on AllEmotes {\n  global {\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmoteVipFrag on AllEmotes {\n  vip {\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment MeStreamChatModeSettingFrag on User {\n  id\n  private {\n    displaySetting {\n      lemon\n      icecream\n      diamond\n      ninjaghini\n      ninjet\n      follow\n      subscription\n      hosting\n      moderation\n      chat\n      stickers\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiFrag on User {\n  id\n  emoji {\n    ...EmojiGlobalFrag\n    ...EmojiVipFrag\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiGlobalFrag on AllEmojis {\n  global {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiVipFrag on AllEmojis {\n  vip {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def LivestreamPage(streamerDisplayName, isLoggedIn, isMe):
        payload = {
            "operationName": "LivestreamPage",
            "variables": {
                "displayname": streamerDisplayName,
                "add": False,
                "isLoggedIn": isLoggedIn,
                "isMe": isMe,
                "showUnpicked": False,
                "order": "PickTime"
            },
            "query": "query LivestreamPage($displayname: String!, $add: Boolean!, $isLoggedIn: Boolean!, $isMe: Boolean!, $order: ClipSortOrder!, $showUnpicked: Boolean!) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    ...VDliveAvatarFrag\n    ...VDliveNameFrag\n    ...LivestreamChannelHeaderFrag\n    offlineImage\n    banStatus\n    deactivated\n    avatar\n    chatBannedEmoji @include(if: $isLoggedIn)\n    bttReceiverAddress\n    myRoomRole @include(if: $isLoggedIn)\n    isMe @include(if: $isLoggedIn)\n    isSubscribing @include(if: $isLoggedIn)\n    ...LivestreamInfoFrag\n    lastStreamedAt\n    donateDisabled\n    subscribeDisabled\n    clientLivestream {\n      magnetUri\n      online\n      __typename\n    }\n    livestream {\n      id\n      permlink\n      createdAt\n      ageRestriction\n      earnRestriction\n      encryptedStream\n      watchTime(add: $add)\n      ...VVideoPlayerFrag\n      __typename\n    }\n    hostingLivestream {\n      id\n      creator {\n        id\n        ...VDliveAvatarFrag\n        ...VDliveNameFrag\n        username\n        __typename\n      }\n      ...VVideoPlayerFrag\n      __typename\n    }\n    rerun {\n      entries {\n        pastbroadcast {\n          ...RerunReplayFrag\n          __typename\n        }\n        __typename\n      }\n      startSecond\n      __typename\n    }\n    ...LivestreamProfileFrag\n    beta {\n      starfruitEnabled\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment LivestreamInfoFrag on User {\n  id\n  livestream {\n    id\n    category {\n      title\n      imgUrl\n      id\n      backendID\n      __typename\n    }\n    language {\n      id\n      language\n      __typename\n    }\n    title\n    watchingCount\n    totalReward\n    lemonReward\n    ...VDonationGiftFrag\n    __typename\n  }\n  clientLivestream {\n    magnetUri\n    online\n    __typename\n  }\n  hostingLivestream {\n    id\n    __typename\n  }\n  rerun {\n    startSecond\n    watchingCount\n    __typename\n  }\n  ...TreasureChestFrag\n  __typename\n}\n\nfragment VDonationGiftFrag on Post {\n  permlink\n  category {\n    id\n    title\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  creator {\n    id\n    username\n    __typename\n  }\n  __typename\n}\n\nfragment TreasureChestFrag on User {\n  id\n  username\n  isMe @include(if: $isLoggedIn)\n  treasureChest {\n    value\n    state\n    ongoingGiveaway {\n      closeAt\n      pricePool\n      claimed @include(if: $isLoggedIn)\n      __typename\n    }\n    __typename\n  }\n  ...TreasureChestPopupFrag\n  __typename\n}\n\nfragment TreasureChestPopupFrag on User {\n  id\n  username\n  isMe @include(if: $isLoggedIn)\n  isFollowing @include(if: $isLoggedIn)\n  treasureChest {\n    value\n    state\n    expireAt\n    buffs {\n      type\n      boost\n      __typename\n    }\n    ongoingGiveaway {\n      pricePool\n      closeAt\n      claimed @include(if: $isLoggedIn)\n      durationInSeconds\n      __typename\n    }\n    startGiveawayValueThreshold\n    nextGiveawayThresholdAt @include(if: $isMe)\n    __typename\n  }\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment LivestreamProfileFrag on User {\n  isMe @include(if: $isLoggedIn)\n  canSubscribe\n  private @include(if: $isLoggedIn) {\n    subscribers {\n      totalCount\n      __typename\n    }\n    __typename\n  }\n  videos {\n    totalCount\n    __typename\n  }\n  pastBroadcasts {\n    totalCount\n    __typename\n  }\n  clips(order: $order, showUnpicked: $showUnpicked) {\n    totalCount\n    __typename\n  }\n  followers {\n    totalCount\n    __typename\n  }\n  following {\n    totalCount\n    __typename\n  }\n  ...LivestreamAboutFrag\n  __typename\n}\n\nfragment LivestreamAboutFrag on User {\n  id\n  panels {\n    id\n    title\n    imageURL\n    imageLinkURL\n    body\n    __typename\n  }\n  __typename\n}\n\nfragment VVideoPlayerFrag on Livestream {\n  permlink\n  disableAlert\n  encryptedStream\n  category {\n    id\n    title\n    __typename\n  }\n  tags\n  language {\n    id\n    language\n    __typename\n  }\n  __typename\n}\n\nfragment VFollowFrag on User {\n  id\n  username\n  displayname\n  isFollowing @include(if: $isLoggedIn)\n  isMe @include(if: $isLoggedIn)\n  followers {\n    totalCount\n    __typename\n  }\n  __typename\n}\n\nfragment LivestreamChannelHeaderFrag on User {\n  ...VDliveAvatarFrag\n  ...VDliveNameFrag\n  ...VFollowFrag\n  ...VSubscriptionFrag\n  followers {\n    totalCount\n    __typename\n  }\n  livestream {\n    id\n    totalReward\n    createdAt\n    watchingCount\n    ageRestriction\n    ...VPostInfoShareFrag\n    __typename\n  }\n  hostingLivestream {\n    id\n    __typename\n  }\n  rerun {\n    watchingCount\n    __typename\n  }\n  __typename\n}\n\nfragment VSubscriptionFrag on User {\n  id\n  username\n  displayname\n  lastStreamedAt\n  mySubscription @include(if: $isLoggedIn) {\n    isSubscribing\n    nextBillingAt\n    lemonSub\n    subType\n    subscribedAt\n    subStreak\n    lastBilledDate\n    status\n    month\n    subStreakStartedAt\n    __typename\n  }\n  isSubscribing @include(if: $isLoggedIn)\n  ...EmojiFrag\n  canSubscribe\n  isMe @include(if: $isLoggedIn)\n  subSetting {\n    badgeColor\n    badgeText\n    textColor\n    streakTextColor\n    benefits\n    backgroundImage\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiFrag on User {\n  id\n  emoji {\n    ...EmojiGlobalFrag\n    ...EmojiVipFrag\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiGlobalFrag on AllEmojis {\n  global {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiVipFrag on AllEmojis {\n  vip {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VPostInfoShareFrag on Post {\n  permlink\n  title\n  content\n  category {\n    id\n    backendID\n    title\n    __typename\n  }\n  creator {\n    id\n    username\n    displayname\n    __typename\n  }\n  __typename\n}\n\nfragment RerunReplayFrag on PastBroadcast {\n  id\n  permlink\n  playbackUrl\n  category {\n    title\n    imgUrl\n    id\n    backendID\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  title\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def LivestreamChatroomInfo(streamerDisplayName, isLoggedIn=True):
        payload = {
            "operationName": "LivestreamChatroomInfo",
            "variables": {
                "displayname": streamerDisplayName,
                "isLoggedIn": isLoggedIn,
                "limit": 20,
                "count": 40
            },
            "query": "query LivestreamChatroomInfo($displayname: String!, $isLoggedIn: Boolean!, $limit: Int!, $count: Int!) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    ...VLivestreamChatroomFrag\n    __typename\n  }\n  listBadgeResource {\n    name\n    url\n    description\n    __typename\n  }\n}\n\nfragment VLivestreamChatroomFrag on User {\n  id\n  isFollowing @include(if: $isLoggedIn)\n  role @include(if: $isLoggedIn)\n  myRoomRole @include(if: $isLoggedIn)\n  isSubscribing @include(if: $isLoggedIn)\n  ...VStreamChatroomHeaderFrag\n  ...VStreamChatroomListFrag\n  ...StreamChatroomInputFrag\n  chats(count: $count) {\n    type\n    ... on ChatGift {\n      id\n      gift\n      amount\n      message\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    ... on ChatHost {\n      id\n      viewer\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    ... on ChatSubscription {\n      id\n      month\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    ... on ChatExtendSub {\n      id\n      month\n      length\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatText {\n      id\n      content\n      subLength\n      emojis\n      createdAt\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    ... on ChatSubStreak {\n      id\n      length\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatClip {\n      id\n      url\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatModerator {\n      id\n      add\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatTCValueAdd {\n      id\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      amount\n      totalAmount\n      __typename\n    }\n    ... on ChatFollow {\n      id\n      ...VStreamChatSenderInfoFrag\n      __typename\n    }\n    ... on ChatEmoteAdd {\n      id\n      emote\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatGiftSub {\n      id\n      count\n      receiver\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    ... on ChatGiftSubReceive {\n      id\n      gifter\n      ...VStreamChatSenderInfoFrag\n      subscribing\n      role\n      roomRole\n      sender {\n        id\n        username\n        displayname\n        avatar\n        partnerStatus\n        badges\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VStreamChatroomHeaderFrag on User {\n  id\n  username\n  displayname\n  donateDisabled\n  subscribeDisabled\n  ...EmojiFrag\n  livestream {\n    id\n    permlink\n    __typename\n  }\n  ...VTopContributorsFrag\n  __typename\n}\n\nfragment VTopContributorsFrag on User {\n  id\n  displayname\n  livestream {\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiFrag on User {\n  id\n  emoji {\n    ...EmojiGlobalFrag\n    ...EmojiVipFrag\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiGlobalFrag on AllEmojis {\n  global {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiVipFrag on AllEmojis {\n  vip {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VStreamChatroomListFrag on User {\n  ...VStreamChatRowStreamerFrag\n  ...PinnedGiftsFrag\n  ...PinnedSubFrag\n  ...ChatDisabledFrag\n  ...PinnedStreakFrag\n  __typename\n}\n\nfragment VStreamChatRowStreamerFrag on User {\n  displayname\n  isMe @include(if: $isLoggedIn)\n  ...VStreamChatRowSenderInfoStreamerFrag\n  ...VStreamChatProfileCardStreamerFrag\n  ...StreamChatTextRowStreamerFrag\n  __typename\n}\n\nfragment VStreamChatRowSenderInfoStreamerFrag on User {\n  id\n  subSetting {\n    badgeText\n    badgeColor\n    textColor\n    streakTextColor\n    __typename\n  }\n  __typename\n}\n\nfragment VStreamChatProfileCardStreamerFrag on User {\n  id\n  username\n  myRoomRole @include(if: $isLoggedIn)\n  role\n  __typename\n}\n\nfragment StreamChatTextRowStreamerFrag on User {\n  id\n  username\n  myRoomRole @include(if: $isLoggedIn)\n  mySubscription @include(if: $isLoggedIn) {\n    isSubscribing\n    __typename\n  }\n  chatBannedEmoji\n  emote @include(if: $isLoggedIn) {\n    channel {\n      list {\n        name\n        username\n        sourceURL\n        mimeType\n        level\n        type\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  subSetting {\n    streakTextColor\n    __typename\n  }\n  __typename\n}\n\nfragment PinnedGiftsFrag on User {\n  id\n  username\n  recentDonations(limit: $limit) {\n    user {\n      ...VDliveAvatarFrag\n      ...VDliveNameFrag\n      __typename\n    }\n    ...PinnedGiftItemFrag\n    __typename\n  }\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment PinnedGiftItemFrag on DonationBlock {\n  user {\n    id\n    username\n    displayname\n    ...VDliveAvatarFrag\n    ...VDliveNameFrag\n    __typename\n  }\n  count\n  type\n  updatedAt\n  expiresAt\n  expirationTime\n  __typename\n}\n\nfragment PinnedSubFrag on User {\n  id\n  username\n  ...VDliveAvatarFrag\n  ...VDliveNameFrag\n  subSetting {\n    badgeText\n    badgeColor\n    textColor\n    benefits\n    __typename\n  }\n  ...VFollowFrag\n  ...PinnedSubOnGoingFrag\n  __typename\n}\n\nfragment VFollowFrag on User {\n  id\n  username\n  displayname\n  isFollowing @include(if: $isLoggedIn)\n  isMe @include(if: $isLoggedIn)\n  followers {\n    totalCount\n    __typename\n  }\n  __typename\n}\n\nfragment PinnedSubOnGoingFrag on User {\n  id\n  username\n  ongoingGiftSub {\n    gifter {\n      ...VDliveAvatarFrag\n      ...VDliveNameFrag\n      __typename\n    }\n    count\n    __typename\n  }\n  __typename\n}\n\nfragment ChatDisabledFrag on User {\n  id\n  chatDisabled\n  __typename\n}\n\nfragment PinnedStreakFrag on User {\n  id\n  username\n  mySubscription @include(if: $isLoggedIn) {\n    isSubscribing\n    canCheerStreak\n    subStreak\n    __typename\n  }\n  __typename\n}\n\nfragment StreamChatroomInputFrag on User {\n  id\n  username\n  displayname\n  chatMode\n  chatInterval\n  myRoomRole @include(if: $isLoggedIn)\n  livestream {\n    id\n    creator {\n      id\n      username\n      displayname\n      __typename\n    }\n    permlink\n    __typename\n  }\n  ...StreamChatMemberManageTabFrag\n  ...StreamChatModeSettingsFrag\n  ...EmoteBoardStreamerFrag\n  __typename\n}\n\nfragment StreamChatMemberManageTabFrag on User {\n  id\n  username\n  displayname\n  myRoomRole @include(if: $isLoggedIn)\n  __typename\n}\n\nfragment StreamChatModeSettingsFrag on User {\n  id\n  chatMode\n  emoteMode {\n    NoMineEmote\n    NoGlobalEmote\n    NoAllEmote\n    __typename\n  }\n  chatVerifiedOnly\n  chatLinkDisabled\n  chatInterval\n  followChatDelay\n  __typename\n}\n\nfragment EmoteBoardStreamerFrag on User {\n  id\n  username\n  partnerStatus\n  ...EmojiFrag\n  chatBannedEmoji\n  myRoomRole @include(if: $isLoggedIn)\n  mySubscription @include(if: $isLoggedIn) {\n    isSubscribing\n    __typename\n  }\n  emoteMode {\n    NoMineEmote\n    NoGlobalEmote\n    NoAllEmote\n    __typename\n  }\n  emote @include(if: $isLoggedIn) {\n    channel {\n      list {\n        name\n        username\n        sourceURL\n        mimeType\n        level\n        type\n        __typename\n      }\n      __typename\n    }\n    vip {\n      list {\n        name\n        username\n        sourceURL\n        mimeType\n        level\n        type\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VStreamChatSenderInfoFrag on SenderInfo {\n  subscribing\n  role\n  roomRole\n  sender {\n    id\n    username\n    displayname\n    avatar\n    partnerStatus\n    badges\n    effect\n    __typename\n  }\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def PwdCheck(streamerDisplayName):
        payload = {
            "operationName": "PwdCheck",
            "variables": {
                "displayName": streamerDisplayName
            },
            "query": "query PwdCheck($pwd: String, $displayName: String!) {\n  pwdCheck(pwd: $pwd, displayName: $displayName) {\n    err {\n      code\n      message\n      __typename\n    }\n    valid\n    __typename\n  }\n}\n"
        }
        return payload

    @staticmethod
    def LivestreamPageRefetch(streamerDisplayName, isLoggedIn=True):
        payload = {
            "operationName": "LivestreamPageRefetch",
            "variables": {
                "displayname": streamerDisplayName,
                "add": False,
                "isLoggedIn": isLoggedIn
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "a7cf60e7fdc27ebd47acf5e647c1c2dfe58281a0a50f2bb29759355e1f1ece13"
                }
            }
        }
        return payload

    @staticmethod
    def TopContributorsLivestream(streamDisplayName):
        payload = {
              "operationName": "TopContributorsLivestream",
              "variables": {
                "displayname": streamDisplayName,
                "first": 10,
                "rule": "THIS_STREAM",
                "queryStream": True
              },
              "query": "query TopContributorsLivestream($displayname: String!, $first: Int, $after: String) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    livestream {\n      ...TopContributorsOfLivestreamFrag\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment TopContributorsOfLivestreamFrag on Livestream {\n  id\n  permlink\n  topContributions(first: $first, after: $after) {\n    pageInfo {\n      endCursor\n      hasNextPage\n      __typename\n    }\n    list {\n      amount\n      contributor {\n        id\n        ...VDliveNameFrag\n        ...VDliveAvatarFrag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def TopContributors(streamDisplayName, rule):
        payload = {
              "operationName": 'TopContributors',
              "variables": {
                "displayname": streamDisplayName,
                "first": 10,
                "rule": rule,
                "queryStream": False
              },
              "extensions": {
                "persistedQuery": {
                  "version": 1,
                  "sha256Hash": "e167a0e968a58dc723f0471b68fe65b0015ac63fdf1724187b68055b1361970f"
                }
              },
             "query": "query TopContributors($displayname: String!, $rule: ContributionSummaryRule!, $first: Int, $after: String) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    ...TopContributorsOfStreamerFrag\n    __typename\n  }\n}\n\nfragment TopContributorsOfStreamerFrag on User {\n  id\n  topContributions(rule: $rule, first: $first, after: $after) {\n    pageInfo {\n      endCursor\n      hasNextPage\n      __typename\n    }\n    list {\n      amount\n      contributor {\n        id\n        ...VDliveNameFrag\n        ...VDliveAvatarFrag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def AddSubscription(streamerName, month):
        payload = {
            "operationName": "AddSubscribe",
            "variables": {
                "streamer": streamerName,
                "month": month
            },
            "query": "mutation AddSubscribe($streamer: String!, $month: Int) {\n  subscribeWithCashback(streamer: "
                     "$streamer, month: $month) {\n    err {\n      code\n      __typename\n    }\n    "
                     "cashbacked\n    __typename\n  }\n}\n"
        }
        return payload

    @staticmethod
    def MeSubscribing():
        payload = {
              "operationName": "MeSubscribing",
              "variables": {
                "first": 50
              },
              "query": "query MeSubscribing($first: Int!, $after: String) {\n  me {\n    ...MeSubscribingFrag\n    __typename\n  }\n}\n\nfragment MeSubscribingFrag on User {\n  id\n  private {\n    subscribing(first: $first, after: $after) {\n      totalCount\n      pageInfo {\n        startCursor\n        endCursor\n        hasNextPage\n        hasPreviousPage\n        __typename\n      }\n      list {\n        streamer {\n          username\n          displayname\n          avatar\n          partnerStatus\n          __typename\n        }\n        tier\n        status\n        lastBilledDate\n        subscribedAt\n        nextBillingAt\n        month\n        subType\n        platform\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def UserUnsubscribe(streamer_name):
        payload = {
              "operationName": "UserUnsubscribe",
              "variables": {
                "streamer": streamer_name
              },
              "query": "mutation UserUnsubscribe($streamer: String!) {\n  unsubscribe(streamer: $streamer) {\n    err {\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
            }
        return payload

    @staticmethod
    def BanStreamChatUser(streamer, banUser):
        payload = {
          "operationName": "BanStreamChatUser",
          "variables": {
            "streamer": streamer,
            "username": banUser
          },
          "query": "mutation BanStreamChatUser($streamer: String!, $username: String!) {\n  streamchatUserBan(streamer: $streamer, username: $username) {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        return payload

    @staticmethod
    def UnbanStreamChatUser(streamer, banUser):
        payload = {
              "operationName": "UnbanStreamChatUser",
              "variables": {
                "streamer": streamer,
                "username": banUser
              },
              "extensions": {
                "persistedQuery": {
                  "version": 1,
                  "sha256Hash": "574e9a8db47ff719844359964d6108320e4d35f0378d7f983651d87b315d4008"
                }
              },
              "query": "mutation UnbanStreamChatUser($streamer: String!, $username: String!) {\n  streamchatUserUnban(streamer: $streamer, username: $username) {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
            }
        return payload

    @staticmethod
    def StreamChatBannedUsers(streamer_display):
        payload = {
            "operationName": "StreamChatBannedUsers",
            "variables": {
                "displayname": streamer_display,
                "first": 20,
                "search": ""
            },
            "query": "query StreamChatBannedUsers($displayname: String!, $first: Int, $after: String, $search: String) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    chatBannedUsers(first: $first, after: $after, search: $search) {\n      pageInfo {\n        endCursor\n        hasNextPage\n        __typename\n      }\n      list {\n        username\n        ...VDliveAvatarFrag\n        ...VDliveNameFrag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def AddModerator(streamer, user):
        payload = {
            "operationName": "AddModerator",
            "variables": {
                "username": user,
                "streamer": streamer
            },
            "query": "mutation AddModerator($username: String!, $streamer: String) {\n  moderatorAdd(username: $username, streamer: $streamer) {\n    err {\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
        }
        return payload

    @staticmethod
    def RemoveModerator(streamer, user):
        payload = {
              "operationName": "RemoveModerator",
              "variables": {
                "username": user,
                "streamer": streamer
              },
              "query": "mutation RemoveModerator($username: String!, $streamer: String) {\n  moderatorRemove(username: $username, streamer: $streamer) {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
            }
        return payload

    @staticmethod
    def StreamChatModerators(displayname):
        payload = {
            "operationName": "StreamChatModerators",
            "variables": {
                "displayname": displayname,
                "first": 20,
                "search": ""
            },
            "query": "query StreamChatModerators($displayname: String!, $first: Int, $after: String, $search: String) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    chatModerators(first: $first, after: $after, search: $search) {\n      pageInfo {\n        endCursor\n        hasNextPage\n        __typename\n      }\n      list {\n        username\n        ...VDliveAvatarFrag\n        ...VDliveNameFrag\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
        }

        return payload

    @staticmethod
    def DeleteChat(streamer, messageID):
        payload = {
              "operationName": "DeleteChat",
              "variables": {
                "streamer": streamer,
                "id": messageID
              },
              "extensions": {
                "persistedQuery": {
                  "version": 1,
                  "sha256Hash": "7ae6f96161b89d9831dcf217f11f67c1edf5bb311d8819101345ed8eb38f6ed9"
                }
              },
              "query": "mutation DeleteChat($streamer: String!, $id: String!) {\n  chatDelete(streamer: $streamer, id: $id) {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
            }
        return payload

    @staticmethod
    def MeModLogs():
        payload = {
            "operationName": "MeModLogs",
            "variables": {
                "input": {
                    "operator": "",
                    "operation": "",
                    "start": None,
                    "end": None,
                    "first": 20,
                    "after": ""
                }
            },
            "query": "query MeModLogs($input: ListModLogsInput!) {\n  me {\n    ...DashboardModeratorFrag\n    __typename\n  }\n}\n\nfragment DashboardModeratorFrag on User {\n  id\n  modLogs(input: $input) {\n    pageInfo {\n      endCursor\n      hasNextPage\n      __typename\n    }\n    list {\n      streamer {\n        id\n        avatar\n        displayname\n        __typename\n      }\n      operator {\n        id\n        avatar\n        displayname\n        __typename\n      }\n      operation\n      user {\n        id\n        avatar\n        displayname\n        __typename\n      }\n      emote\n      log\n      createdAt\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
        }

        return payload

    @staticmethod
    def LivestreamProfileReplay(displayname):
        payload = {
              "operationName": "LivestreamProfileReplay",
              "variables": {
                "displayname": displayname,
                "first": 20
              },
              "query": "query LivestreamProfileReplay($displayname: String!, $first: Int, $after: String) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    pastBroadcastsV2(first: $first, after: $after) {\n      pageInfo {\n        endCursor\n        hasNextPage\n        __typename\n      }\n      list {\n        ...ProfileReplaySnapFrag\n        __typename\n      }\n      __typename\n    }\n    username\n    __typename\n  }\n}\n\nfragment ProfileReplaySnapFrag on PastBroadcast {\n  permlink\n  thumbnailUrl\n  title\n  length\n  totalReward\n  createdAt\n  viewCount\n  playbackUrl\n  creator {\n    id\n    displayname\n    __typename\n  }\n  resolution {\n    resolution\n    url\n    __typename\n  }\n  category {\n    id\n    title\n    imgUrl\n    __typename\n  }\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def LivestreamProfileSubscriber(displayname):
        payload = {
              "operationName": "LivestreamProfileSubscriber",
              "variables": {
                "displayname": displayname,
                "first": 20
              },
              "query": "query LivestreamProfileSubscriber($displayname: String!, $first: Int, $after: String) {\n  userByDisplayName(displayname: $displayname) {\n    id\n    private {\n      subscribers(first: $first, after: $after) {\n        pageInfo {\n          endCursor\n          hasNextPage\n          __typename\n        }\n        list {\n          subscriber {\n            username\n            ...VDliveAvatarFrag\n            ...VDliveNameFrag\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def AddWatch(permlink):
        payload = {
              "operationName": "AddWatch",
              "variables": {
                "permlink": permlink
              },
              "query": "mutation AddWatch($permlink: String!) {\n  watch(permlink: $permlink) {\n    err {\n      code\n      __typename\n    }\n    __typename\n  }\n}\n"
            }
        return payload

    @staticmethod
    def PastBroadcastPage(permlink):
        payload = {
              "operationName": "PastBroadcastPage",
              "variables": {
                "permlink": permlink,
                "commentsFirst": 20,
                "topContributionsFirst": 10,
                "isLoggedIn": True
              },
              "query": "query PastBroadcastPage($permlink: String!, $commentsFirst: Int, $topContributionsFirst: Int, $commentsAfter: String, $topContributionsAfter: String, $isLoggedIn: Boolean!) {\n  pastBroadcastV2(permlink: $permlink) {\n    creator {\n      id\n      displayname\n      donateDisabled\n      subscribeDisabled\n      __typename\n    }\n    length\n    content\n    createdAt\n    playbackUrl\n    thumbnailUrl\n    upNext {\n      list {\n        ...VVideoPBUpNextItemFrag\n        __typename\n      }\n      __typename\n    }\n    comments(first: $commentsFirst, after: $commentsAfter) {\n      ...VVideoPBCommentFrag\n      __typename\n    }\n    topContributions(first: $topContributionsFirst, after: $topContributionsAfter) {\n      ...VVideoPBUpNextTopContributorFrag\n      __typename\n    }\n    ...VideoPBHeaderFrag\n    ...VVideoPBInfoFrag\n    __typename\n  }\n}\n\nfragment VVideoPBInfoFrag on VideoPB {\n  category {\n    title\n    imgUrl\n    id\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  content\n  permlink\n  title\n  createdAt\n  creator {\n    id\n    displayname\n    __typename\n  }\n  ...VDonationGiftFrag\n  __typename\n}\n\nfragment VDonationGiftFrag on Post {\n  permlink\n  category {\n    id\n    title\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  creator {\n    id\n    username\n    __typename\n  }\n  __typename\n}\n\nfragment VideoPBHeaderFrag on VideoPB {\n  totalReward\n  viewCount\n  creator {\n    id\n    username\n    displayname\n    about\n    followers {\n      totalCount\n      __typename\n    }\n    ...VDliveAvatarFrag\n    ...VDliveNameFrag\n    ...VFollowFrag\n    ...VSubscriptionFrag\n    __typename\n  }\n  ...VPostInfoShareFrag\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment VFollowFrag on User {\n  id\n  username\n  displayname\n  isFollowing @include(if: $isLoggedIn)\n  isMe @include(if: $isLoggedIn)\n  followers {\n    totalCount\n    __typename\n  }\n  __typename\n}\n\nfragment VSubscriptionFrag on User {\n  id\n  username\n  displayname\n  lastStreamedAt\n  mySubscription @include(if: $isLoggedIn) {\n    isSubscribing\n    nextBillingAt\n    lemonSub\n    subType\n    subscribedAt\n    subStreak\n    lastBilledDate\n    status\n    month\n    subStreakStartedAt\n    __typename\n  }\n  isSubscribing @include(if: $isLoggedIn)\n  ...EmojiFrag\n  canSubscribe\n  isMe @include(if: $isLoggedIn)\n  subSetting {\n    badgeColor\n    badgeText\n    textColor\n    streakTextColor\n    benefits\n    backgroundImage\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiFrag on User {\n  id\n  emoji {\n    ...EmojiGlobalFrag\n    ...EmojiVipFrag\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiGlobalFrag on AllEmojis {\n  global {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment EmojiVipFrag on AllEmojis {\n  vip {\n    totalCount\n    list {\n      name\n      username\n      sourceURL\n      mimeType\n      level\n      type\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VPostInfoShareFrag on Post {\n  permlink\n  title\n  content\n  category {\n    id\n    backendID\n    title\n    __typename\n  }\n  creator {\n    id\n    username\n    displayname\n    __typename\n  }\n  __typename\n}\n\nfragment VVideoPBUpNextItemFrag on VideoPB {\n  creator {\n    id\n    displayname\n    __typename\n  }\n  permlink\n  title\n  totalReward\n  thumbnailUrl\n  length\n  createdAt\n  category {\n    id\n    title\n    __typename\n  }\n  viewCount\n  __typename\n}\n\nfragment VVideoPBCommentFrag on CommentConnection {\n  totalCount\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  list {\n    ...VVideoPBCommentItemFrag\n    __typename\n  }\n  __typename\n}\n\nfragment VVideoPBCommentItemFrag on Comment {\n  upvotes\n  downvotes\n  author {\n    displayname\n    avatar\n    __typename\n  }\n  content\n  createdAt\n  myVote\n  commentCount\n  permlink\n  __typename\n}\n\nfragment VVideoPBUpNextTopContributorFrag on ContributionConnection {\n  list {\n    amount\n    contributor {\n      ...VDliveAvatarFrag\n      ...VDliveNameFrag\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
            }
        return payload


class LoginAPI:
    @staticmethod
    def IsUserVerifyEmailButNoPwd(streamerDisplayName):
        payload = {
            "operationName": "IsUserVerifyEmailButNoPwd",
            "variables": {
                "username": streamerDisplayName
            },
            "query": "query IsUserVerifyEmailButNoPwd($username: String!) {IsUserVerifyEmailButNoPwd(username: $username) {isUserVerifyEmailButNoPwd __typename}}"
        }
        return payload

    @staticmethod
    def isFirstThirdLogin(streamerDisplayName, isLoggedIn=True):
        payload = {
            "operationName": "isFirstThirdLogin",
            "variables": {
                "username": "automation"
            },
            "query": "query isFirstThirdLogin($username: String!) {isFirstThirdLogin(username: $username) {isFirstThirdLogin __typename}}"
        }
        return payload


class HomePageAPI:
    @staticmethod
    def LiveCarousel():
        payload = {
              "operationName": "LiveCarousel",
              "variables": {
                "input": {
                  "first": 5,
                  "showNSFW": True,
                  "showMatureContent": True,
                  "languageID": 1
                }
              },
              "extensions": {
                "persistedQuery": {
                  "version": 1,
                  "sha256Hash": "421104d17f58f9e240983bebe1c8811cb534560b049e444d32bf3350067e4eb9"
                }
              },
              "query": "query LiveCarousel($input: LivestreamsOption) {\n  liveCarousel(input: $input) {\n    totalCount\n    list {\n      id\n      position\n      live {\n        ... on Livestream {\n          id\n          permlink\n          ...VLivestreamSnapFrag\n          language {\n            id\n            backendID\n            language\n            __typename\n          }\n          category {\n            id\n            backendID\n            title\n            imgUrl\n            __typename\n          }\n          title\n          creator {\n            beta {\n              starfruitEnabled\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VLivestreamSnapFrag on Livestream {\n  id\n  creator {\n    id\n    username\n    displayname\n    myChatBadges\n    ...VDliveAvatarFrag\n    ...VDliveNameFrag\n    __typename\n  }\n  permlink\n  title\n  totalReward\n  watchingCount\n  earnRestriction\n  ageRestriction\n  thumbnailUrl\n  lastUpdatedAt\n  category {\n    id\n    title\n    parent {\n      id\n      title\n      __typename\n    }\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  tags\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def homepage_carousels():
        payload = {
            "operationName": "HomePageCarousels",
            "variables": {
                "count": 5,
                "userLanguageCode": "en"
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "1668c6da479e8bf5cbffdff4006228499d14ead02f29cdb53a7a31404e191067"
                }
            },
            "query": "query HomePageCarousels($count: Int, $userLanguageCode: String, $watching: Int) {\n  carousels(count: $count, userLanguageCode: $userLanguageCode, watching: $watching) {\n    type\n    item {\n      ... on Livestream {\n        id\n        permlink\n        ...VLivestreamSnapFrag\n        language {\n          id\n          backendID\n          language\n          __typename\n        }\n        category {\n          id\n          backendID\n          title\n          imgUrl\n          __typename\n        }\n        title\n        creator {\n          beta {\n            starfruitEnabled\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      ... on Poster {\n        thumbnailURL\n        redirectLink\n        mobileThumbnailURL\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VLivestreamSnapFrag on Livestream {\n  id\n  creator {\n    id\n    username\n    displayname\n    myChatBadges\n    ...VDliveAvatarFrag\n    ...VDliveNameFrag\n    __typename\n  }\n  permlink\n  title\n  totalReward\n  watchingCount\n  earnRestriction\n  ageRestriction\n  thumbnailUrl\n  lastUpdatedAt\n  category {\n    id\n    title\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  tags\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def homepage_livestream():
        payload = {
            "operationName": "HomePageLivestream",
            "variables": {
                "first": 20,
                # "showNSFW": true,
                "order": "TRENDING",
                "userLanguageCode": "en",
                # "showMatureContent": true
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "02887b79493a97ee84d3119a377208f843e8a35ed25f2dfe0deb1b55c1a5adcd"
                }
            },
            "query": "query HomePageLivestream($first: Int, $after: String, $languageID: Int, $categoryID: Int, $showNSFW: Boolean, $order: LivestreamSortOrder, $userLanguageCode: String, $showMatureContent: Boolean) {\n  livestreams(input: {first: $first, after: $after, languageID: $languageID, categoryID: $categoryID, showNSFW: $showNSFW, order: $order, userLanguageCode: $userLanguageCode, showMatureContent: $showMatureContent}) {\n    ...VCategoryLivestreamFrag\n    __typename\n  }\n}\n\nfragment VCategoryLivestreamFrag on LivestreamConnection {\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  list {\n    permlink\n    ageRestriction\n    earnRestriction\n    ...VLivestreamSnapFrag\n    __typename\n  }\n  __typename\n}\n\nfragment VLivestreamSnapFrag on Livestream {\n  id\n  creator {\n    id\n    username\n    displayname\n    myChatBadges\n    ...VDliveAvatarFrag\n    ...VDliveNameFrag\n    __typename\n  }\n  permlink\n  title\n  totalReward\n  watchingCount\n  earnRestriction\n  ageRestriction\n  thumbnailUrl\n  lastUpdatedAt\n  category {\n    id\n    title\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  tags\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def homepage_categories():
        payload = {
              "operationName": "HomePageCategories",
              "variables": {
                "first": 15,
                "languageID": None,
                "showMatureContent": True,
                "showNSFW": True
              },
              "extensions": {
                "persistedQuery": {
                  "version": 1,
                  "sha256Hash": "859cd2be7b573e3070733a7ac8ec9c398aa8476026987afb516ee9bdcd4aef57"
                }
              },
              "query": "query HomePageCategories($first: Int, $after: String, $languageID: Int, $showMatureContent: Boolean, $showNSFW: Boolean) {\n  categories(input: {first: $first, after: $after, languageID: $languageID, showMatureContent: $showMatureContent, showNSFW: $showNSFW}) {\n    ...HomeCategoriesFrag\n    __typename\n  }\n}\n\nfragment HomeCategoriesFrag on CategoryConnection {\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  list {\n    ...VCategoryCardFrag\n    __typename\n  }\n  __typename\n}\n\nfragment VCategoryCardFrag on Category {\n  id\n  backendID\n  title\n  imgUrl\n  watchingCount\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def homepage_list_recommendation():  # 推荐系统
        payload = {
              "operationName": "HomePageListRecommendation",
              "variables": {
                "first": 40,
                "after": "0",
                "languageID": None,
                "categoryID": None,
                "showNSFW": None,
                "userLanguageCode": "en",
                "showMatureContent": True
              },
              "extensions": {
                "persistedQuery": {
                  "version": 1,
                  "sha256Hash": "51069c2a7814a46fdc4e3bbc6920f18351ded9a1491e57617cbdb6a4cab633c2"
                }
              },
              "query": "query HomePageListRecommendation($first: Int, $after: String, $languageID: Int, $categoryID: Int, $showNSFW: Boolean, $userLanguageCode: String, $showMatureContent: Boolean) {\n  listRecommendation(input: {first: $first, after: $after, languageID: $languageID, categoryID: $categoryID, showNSFW: $showNSFW, userLanguageCode: $userLanguageCode, showMatureContent: $showMatureContent}) {\n    ...VCategoryLivestreamFrag\n    __typename\n  }\n}\n\nfragment VCategoryLivestreamFrag on LivestreamConnection {\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  list {\n    permlink\n    ageRestriction\n    earnRestriction\n    ...VLivestreamSnapFrag\n    __typename\n  }\n  __typename\n}\n\nfragment VLivestreamSnapFrag on Livestream {\n  id\n  creator {\n    id\n    username\n    displayname\n    myChatBadges\n    ...VDliveAvatarFrag\n    ...VDliveNameFrag\n    __typename\n  }\n  permlink\n  title\n  totalReward\n  watchingCount\n  earnRestriction\n  ageRestriction\n  thumbnailUrl\n  lastUpdatedAt\n  category {\n    id\n    title\n    parent {\n      id\n      title\n      __typename\n    }\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  tags\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def homepage_global_information_recommend():  # 主页左边的推荐列表
        payload = {
              "operationName": "GlobalInformationRecommend",
              "variables": {
                "limit": 50
              },
              "query": "query GlobalInformationRecommend($limit: Int!, $category: String) {\n  globalInfo {\n    ...SidebarRecommendation\n    __typename\n  }\n}\n\nfragment SidebarRecommendation on GlobalInfo {\n  recommendChannels(limit: $limit, category: $category) {\n    user {\n      ...VDliveNameFrag\n      ...VDliveAvatarFrag\n      livestream {\n        id\n        watchingCount\n        permlink\n        earnRestriction\n        ageRestriction\n        category {\n          id\n          title\n          __typename\n        }\n        __typename\n      }\n      followers {\n        totalCount\n        __typename\n      }\n      banStatus\n      hostingLivestream {\n        id\n        permlink\n        earnRestriction\n        ageRestriction\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n"
            }
        return payload

    @staticmethod
    def homepage_nav_search_result(search_text):
        payload = {
            "operationName": "NavSearchResult",
            "variables": {
                "text": search_text,
                "userFirst": 8,
                "categoryFirst": 3
            },
            "query": "query NavSearchResult($text: String!, $userFirst: Int, $categoryFirst: Int) {\n  search(text: $text) {\n    allUsers(first: $userFirst) {\n      list {\n        ... on Livestream {\n          id\n          category {\n            id\n            title\n            __typename\n          }\n          creator {\n            id\n            ...VDliveAvatarFrag\n            ...VDliveNameFrag\n            followers {\n              totalCount\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        ... on User {\n          id\n          ...VDliveAvatarFrag\n          ...VDliveNameFrag\n          username\n          followers {\n            totalCount\n            __typename\n          }\n          rerun {\n            entries {\n              pastbroadcast {\n                id\n                category {\n                  id\n                  title\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    liveCategories(first: $categoryFirst) {\n      list {\n        id\n        backendID\n        title\n        imgUrl\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def homepage_browse_page_search_category(search_text):
        payload = {
            "operationName": "BrowsePageSearchCategory",
            "variables": {
                "text": search_text,
                "first": 14
            },
            "query": "query BrowsePageSearchCategory($text: String!, $first: Int, $after: String) {\n  search(text: $text) {\n    trendingCategories(first: $first, after: $after) {\n      ...HomeCategoriesFrag\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment HomeCategoriesFrag on CategoryConnection {\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  list {\n    ...VCategoryCardFrag\n    __typename\n  }\n  __typename\n}\n\nfragment VCategoryCardFrag on Category {\n  id\n  backendID\n  title\n  imgUrl\n  watchingCount\n  __typename\n}\n"
        }
        return payload

    @staticmethod
    def homepage_category_live_stream_page(categoryid):
        payload = {
            "operationName": "CategoryLivestreamsPage",
            "variables": {
                "first": 150,
                "categoryID": categoryid,
                "languageID": None,
                "showNSFW": True,
                "showMatureContent": True
            },
            "query": "query CategoryLivestreamsPage($first: Int, $after: String, $languageID: Int, $categoryID: Int!, $showNSFW: Boolean, $order: LivestreamSortOrder, $userLanguageCode: String, $showMatureContent: Boolean) {\n  category(id: $categoryID) {\n    id\n    backendID\n    title\n    imgUrl\n    coverImgUrl\n    watchingCount\n    languages {\n      ...LanguageFrag\n      __typename\n    }\n    __typename\n  }\n  livestreams(input: {first: $first, after: $after, languageID: $languageID, categoryID: $categoryID, showNSFW: $showNSFW, order: $order, userLanguageCode: $userLanguageCode, showMatureContent: $showMatureContent}) {\n    ...VCategoryLivestreamFrag\n    __typename\n  }\n}\n\nfragment VCategoryLivestreamFrag on LivestreamConnection {\n  pageInfo {\n    endCursor\n    hasNextPage\n    __typename\n  }\n  list {\n    permlink\n    ageRestriction\n    earnRestriction\n    ...VLivestreamSnapFrag\n    __typename\n  }\n  __typename\n}\n\nfragment VLivestreamSnapFrag on Livestream {\n  id\n  creator {\n    id\n    username\n    displayname\n    myChatBadges\n    ...VDliveAvatarFrag\n    ...VDliveNameFrag\n    __typename\n  }\n  permlink\n  title\n  totalReward\n  watchingCount\n  earnRestriction\n  ageRestriction\n  thumbnailUrl\n  lastUpdatedAt\n  category {\n    id\n    title\n    __typename\n  }\n  language {\n    id\n    language\n    __typename\n  }\n  tags\n  __typename\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n\nfragment LanguageFrag on Language {\n  id\n  backendID\n  language\n  code\n  __typename\n}\n"
        }

        return payload


class MatureRelatedAPI:
    @staticmethod
    def CheckMaturePopupClosedByUsername(username):
        payload = {
              "operationName": "CheckMaturePopupClosedByUsername",
              "variables": {
                "username": username
              },
              "query": "query CheckMaturePopupClosedByUsername($username: String!) {\n  checkMaturePopupClosedByUsername(username: $username) {\n    isClosed\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
            }
        return payload


class MyProfileAPI:
    @staticmethod
    def VideoPermlink():
        payload = {
          "operationName": "VideoPermlink",
          "variables": {},
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "47739a80af2c7fa5b81f5431904a9f5dc9b1fdaf2f84de1cbc8bc0dc072f3a52"
            }
          }
        }
        return payload

    @staticmethod
    def UploadSearchCategory(categoryName):
        payload = {
          "operationName": "UploadSearchCategory",
          "variables": {
            "text": "qaTest"
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "29e85a6ed7256fb31aadd10a2e1c590de507634a150123786a16a7d16c01ab6b"
            }
          }
        }
        return payload

    @staticmethod
    def UploadGeneratePresignUrl(fileName, hash):
        payload = {
          "operationName": "UploadGeneratePresignUrl",
          "variables": {
            "hash": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwZXJtbGluayI6ImF1dG9tYXRpb24rQTY4Wm9uUFNSIiwiZXhwIjoxNzE2NTM1MzEzLCJpc3MiOiJMaW5vQXBwVHJhbnNjb2RlciJ9.PiUCWgdsu8j79thHUzl4Y4eqr37Q3bSvFyhRV_DceW8",
            "filename": "mp4"
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "d5c9666317e2b2bfde1cbf3736c80c01294a6c19ecc7a2f406bc755961561bd8"
            }
          }
        }
        return payload

    @staticmethod
    def UploadAddVideo(permlink, thumbnailUrl, title, content, filename, bucketName, region, categoryId, languageId):
        payload = {
          "operationName": "UploadAddVideo",
          "variables": {
            "video": {
              "permlink": permlink,
              "thumbnailUrl": thumbnailUrl,
              "title": title,
              "content": content,
              "filename": filename,
              "bucketName": bucketName,
              "region": region,
              "categoryId": categoryId,
              "languageId": languageId
            }
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "a01d82b6355c1e46274199381a64403773019ed866973a0d51489a473b3d2bd2"
            }
          }
        }
        return payload

    @staticmethod
    def LivestreamProfileVideo(displayname):
        payload = {
          "operationName": "LivestreamProfileVideo",
          "variables": {
            "displayname": displayname,
            "sortedBy": "Trending",
            "first": 20
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "df2b8483dbe1fb13ef47e3cf6af8d230571061d7038625587c7ed066bdbdddd3"
            }
          }
        }
        return payload


