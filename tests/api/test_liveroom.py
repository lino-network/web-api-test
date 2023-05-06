import requests
import json



def test_follow_user(api_url, auth_header):
    # 请求的body
    body = {
        "operationName": "FollowUser",
        "variables": {
            "streamer": "vanguardkek"
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "daf146d77e754b6b5a7acd945ff005ae028b33feaa3c79e04e71505190003a5d"
            }
        }
    }
    
    # 发送请求
    response = requests.post(api_url, headers=auth_header, json=body)
    
    # 解析响应
    data = response.json()
    
    # 断言响应结果
    response_data = response.json()['data']
    assert response.status_code == 200
    assert response_data['follow']['err'] is None

    # 查询sidebar中是否有刚follow的主播
    query = {
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

    response = requests.post(api_url, headers=auth_header, json=query)
    assert response.status_code == 200
    followee_list = response.json()["data"]["me"]["private"]["followeeFeed"]["list"]
    assert any(streamer["id"] == "user:vanguardkek" for streamer in followee_list)

    