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


def login(username, password):
    payload = {
          "operationName": "EmailLogin",
          "variables": {
            "email": "automation@nqmo.com",
            "password": "Pwd@1234"
          },
          "query": "mutation EmailLogin($email: String!, $password: String!, $recaptchaToken: String, $deviceType: DeviceType) {\n  loginWithEmail(email: $email, password: $password, recaptchaToken: $recaptchaToken, deviceType: $deviceType) {\n    me {\n      id\n      private {\n        accessToken\n        __typename\n      }\n      __typename\n    }\n    twofactorToken\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
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
        "query":  "mutation UnfollowUser($streamer: String!) {\n  unfollow(streamer: $streamer) {\n    err {\n      code\n      message\n      __typename\n    }\n    __typename\n  }\n}\n",

        "variables": {
            "streamer": user_id
        }
    }
    return payload


def send_chat(stream_name, message, emoList: []):  # 直播间发信息
    payload = {
        "operationName": "SendStreamChatMessage",
        "variables": {
            "input": {
                "streamer": stream_name,
                "message": message,
                "roomRole": "Member",
                "subscribing": True,
                "emojis": emoList
            }
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "848cbe91a57458ed402716e7b57b7a128c3b5a8385a6ebe14d9deff8d1eda73c"
            }
        }
    }
    return payload


def Live_stream_profile_followers(streamer_display_name):  # 其他关注主播的主播
    payload = {
        "operationName": "LivestreamProfileFollowers",
        "variables": {
            "displayname": streamer_display_name,
            "sortedBy": "AZ",
            "first": 20,
            "isLoggedIn": True
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "698db968db04e78c79fe1d48461a5af4596a1337e33386f45cad1cb7d4da3dce"
            }
        }
    }
    return payload


def Live_stream_profile_following(streamer_display_name):  # 主播关注的直播间
    payload = {
        "operationName": "LivestreamProfileFollowing",
        "variables": {
            "displayname": streamer_display_name,
            "sortedBy": "AZ",
            "first": 20,
            "isLoggedIn": True
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "76690ef91938871b85d1155bd9061d6bce3dec7f375db20160c4ce14bf2ff9ad"
            }
        }
    }
    return payload


def top_contributors(streamer_display_name, time='THIS_MONTH'):  # 最杰出贡献者
    payload = {
        "operationName": "TopContributors",
        "variables": {
            "displayname": streamer_display_name,
            "first": 3,
            "rule": time,
            "queryStream": False
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "41f574b3d8a3d0e81c28546c4cebeb2d7179a7dbfa1fc3469e6d681e19fb49d5"
            }
        }
    }
    return payload


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
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "42dbd0f6f50503b37cd48e4cc76aa7d0bb9f6c3f3dea48567951e856b4d93788"
            }
        }
    }
    return payload


def add_gift_sub(streamer_name, count):  # 分发gift sub
    payload = {
        "operationName": "AddGiftSub",
        # "query": 'mutation AddGiftSub($streamer: String!, $toUser: String, $count: Int) {giftSub(streamer: $streamer, toUser: $toUser, count: $count) '
        #          '{ err { code message __typename} __typename}}',
        "variables": {
            "streamer": streamer_name,
            "count": int(count)
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "4f14249cf00d8548aa75c5f992a3ddc741833ee9b4317f5a4c897c1e5743666d"
            }
        }
    }
    return payload


def add_gift_sub_claim(streamer_name):  # 领取gift sub
    payload = {
        "operationName": "AddGiftSubClaim",
        "variables": {
            "streamer": streamer_name
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "21f80889b2afd31652216b1e80abb69467fa20853e8529bfbb78ed1fe0c9d069"
            }
        }
    }
    return payload


def chest_user_transfer(amount):  # 加lemon进宝箱
    payload = {
        "operationName": "ChestUserTransfer",
        "variables": {
            "amount": amount
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "c4812157f22bbaef70ac21a3a2800bd0e94110f3b011abf4766d1d5f0a28c950"
            }
        }
    }
    return payload


def give_away_start():  # 开启宝箱
    payload = {
        "operationName": "GiveawayStart",
        "variables": {},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "71fb36c294173f06f0755ab2cecf724e58ad6e135d3bfddbcb2f57eab6e773bf"
            }
        }
    }
    return payload


def give_away_claim(streamer_name):  # 用户抢宝箱
    payload = {
        "operationName": "GiveawayClaim",
        "variables": {
            "streamer": streamer_name
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "9f013d22643dc9363fe89cc20f0e8d45e3141859907f8d5bbadae713be5a2332"
            }
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


def homepage_categories():
    payload = {
        "operationName": "HomePageCategories",
        "variables": {
            "first": 15,
            "languageID": 'null'
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "386f2dbb71fa1d28e3c9bbff30e41beb7c09dd845b02dcf01c35856076e354dc"
            }
        }
    }
    return payload


def homepage_list_recommendation():  # 推荐系统
    payload = {
        "operationName": "HomePageListRecommendation",
        "variables": {
            "first": 40,
            "after": "0",
            "showNSFW": True,
            "userLanguageCode": "en",
            "showMatureContent": True
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "35160b344e48b47fbc781b60f92f7e6bf1bfcdea1ba1a08b311be56fef38b7d2"
            }
        }
    }
    return payload


def homepage_global_information_recommend():  # 主页左边的推荐列表
    payload = {
        "operationName": "GlobalInformationRecommend",
        "variables": {
            "limit": 30
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "f58123b70a8319382f44c077489e4fca285c2b06bc318e46605eb79644a6b0f3"
            }
        }
    }
    return payload

def homepage_nav_search_result(search_text):
    payload = {
        "operationName": "NavSearchResult",
        "variables": {
            "text": search_text,
            "userFirst": 8,
            "categoryFirst": 3
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "4943f85b80688382280a7ffb895f49baa099c624e6878da93c13a433438b6d81"
            }
        },
        "query": "query NavSearchResult($text: String!, $userFirst: Int, $categoryFirst: Int) {\n  search(text: $text) {\n    allUsers(first: $userFirst) {\n      list {\n        ... on Livestream {\n          id\n          category {\n            id\n            title\n            __typename\n          }\n          creator {\n            id\n            ...VDliveAvatarFrag\n            ...VDliveNameFrag\n            followers {\n              totalCount\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        ... on User {\n          id\n          ...VDliveAvatarFrag\n          ...VDliveNameFrag\n          username\n          followers {\n            totalCount\n            __typename\n          }\n          rerun {\n            entries {\n              pastbroadcast {\n                id\n                category {\n                  id\n                  title\n                  __typename\n                }\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    liveCategories(first: $categoryFirst) {\n      list {\n        id\n        backendID\n        title\n        imgUrl\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment VDliveAvatarFrag on User {\n  id\n  avatar\n  effect\n  __typename\n}\n\nfragment VDliveNameFrag on User {\n  id\n  displayname\n  partnerStatus\n  __typename\n}\n"
    }
    return payload

    


def homepage_browse_page_search_category(search_text):
    payload = {
        "operationName": "BrowsePageSearchCategory",
        "variables": {
            "text": search_text,
            "first": 14
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "3e7231352e1802ba18027591ee411d2ca59030bdfd490b6d54c8d67971001ece"
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
    payload ={
        "operationName": "MeRebillyCards",
        "variables": {},
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "c338f2610965aa4328a7da2c8012e81f565acf3de7c0c109eb9702507d014511"
            }
        }
    }
    return payload

def ActivityUserDonationRank():
    payload ={
        "operationName": "ActivityUserDonationRank",
        "variables": {
            "username": "automation",
            "rankingType": "THIS_WEEK",
            "isStreamer": True
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "0a3cf0be08ae880d5894313d0be07f656fed47ec729f698545463761ca5f9c3d"
            }
        }
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

def test_me_balance():{
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
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "9f719304dbe7a32983da173d9ba737bc4c4d5b4bdc558163e01afad91be6db9c"
            }
        }
    }
    return payload


def browser_register_notification(token):
    payload = {
        "operationName": "BrowserRegisterNotification",
        "variables": {
            "token": token
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "20d6ecfcdb7dc10b4008037e9eee326755b370e69dc9cfce2a407718cb2e5eff"
            }
        }
    }
    return payload


class DaskboardAPI:
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
                  "sha256Hash": "fe703ef0933440b5ffdf75c5f7662bd99ce9687f8c7d9e29961c82b244c21704"
                }
              }
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
              }
        }
        return payload

    @staticmethod
    def DashboardSearchCategories(searchText):
        payload = {
              "operationName": "DashboardSearchCategories",
              "variables": {
                "text": searchText
              },
              "extensions": {
                "persistedQuery": {
                  "version": 1,
                  "sha256Hash": "4eb124d36b62fa4258d2179ed8f5647b1f5370f32eb7492988dca5b016f6d487"
                }
              }
        }
        return payload

    @staticmethod
    def RerunEnableSwitch():
        payload = {
          "operationName": "RerunEnableSwitch",
          "variables": {},
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "c00825f9268b8b4a2c35cb7febae59ae955c6bd704c7e2e49021c0374ba70a40"
            }
          }
        }
        return payload


    @staticmethod
    def RerunDisableSwitch():
        payload = {
          "operationName": "RerunDisableSwitch",
          "variables": {},
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "40e24830c03e591246e493012a9d290d4f8ca9252f83bb089b2e4c93802f3259"
            }
          }
        }
        return payload


class LiveRoomAPI:
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
    def LivestreamTreasureChestAddCheck(streamerDisplayName, amount):   # 加lemon 进宝箱
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
    def LivestreamTreasureChestWinners(streamer_name):   # 宝箱中奖名单
        payload = {
          "operationName": "LivestreamTreasureChestWinners",
          "variables": {
            "displayname": streamer_name,
            "isLoggedIn": True
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "94ea7f30d7e9e7ce0f04eb9944f4d2c373dcc7650f565beb050658142b61bf60"
            }
          }
        }

