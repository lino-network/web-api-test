import requests
import json
#轮播检查
def test_homepage_carousels(api_url, api_headers):
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
        }
    }

    response = requests.post(api_url, headers=api_headers, json=payload)

    assert response.status_code == 200
    assert "data" in response.json()

def test_homepage_livestream(api_url, api_headers):
    payload = {
        "operationName": "HomePageLivestream",
        "variables": {
            "first": 20,
            "languageID": None,
            "categoryID": None,
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

    response = requests.post(api_url, headers=api_headers, json=payload)

    assert response.status_code == 200
    assert "data" in response.json()

def test_homepage_list_recommendation(api_url, auth_header):
    payload = {
        "operationName": "HomePageListRecommendation",
        "variables": {
            "first": 40,
            "after": "0",
            "languageID": None,
            "categoryID": None,
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
    response = requests.post(api_url, json=payload, headers=auth_header)
    response_json = response.json()
    # print(response_json)
    data = response_json.get('data')
    print(data)
    home_page_list_recommendation = data.get('listRecommendation')
    print(home_page_list_recommendation)
    assert home_page_list_recommendation is not None

    assert response.status_code == 200


def test_global_information_recommend(api_url, auth_header):
    payload = {
        "operationName": "GlobalInformationRecommend",
        "variables": {
            "limit": 50,
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "f58123b70a8319382f44c077489e4fca285c2b06bc318e46605eb79644a6b0f3"
            }
        }
    }
    response = requests.post(api_url, json=payload, headers=auth_header)
    response_json = json.loads(response.text)

    # 判断 recommendChannels 数组是否为空
    recommend_channels = response_json['data']['globalInfo']['recommendChannels']
    assert len(recommend_channels) > 0

    assert response.status_code == 200



