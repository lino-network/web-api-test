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
            "email": username,
            "password": password
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "ee5f1abab8122a4441ed378b01f0905612ce3e053c80c1eb1f15cd28310ff017"
            }
        }
    }
    return payload


def follow_user(user_id):
    payload = {
        "operationName": "FollowUser",
        "variables": {
            "streamer": user_id
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "daf146d77e754b6b5a7acd945ff005ae028b33feaa3c79e04e71505190003a5d"
            }
        }
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
        "variables": {
            "streamer": user_id
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "681ef3737bb34799ffe779b420db05b7f83bc8c3f17cdd17c7181bd7eca9859c"
            }
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
            "first": 40,
            "after": "0",
            "showNSFW": True,
            "userLanguageCode": "",
            "showMatureContent": True
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "1668c6da479e8bf5cbffdff4006228499d14ead02f29cdb53a7a31404e191067"
            }
        }
    }
    return payload


def homepage_livestream():
    payload = {
        "operationName": "HomePageLivestream",
        "variables": {
            "first": 20,
            "after": "0",
            "showNSFW": True,
            "order": "TRENDING",
            "userLanguageCode": "en",
            "showMatureContent": True
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "02887b79493a97ee84d3119a377208f843e8a35ed25f2dfe0deb1b55c1a5adcd"
            }
        }
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
        }
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
    def MeDashboard(self, username):
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
