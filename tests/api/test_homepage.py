import requests
import json
import loadData.payloadData as Payload



def test_homepage_carousels(get_config_data, api_headers): #轮播检查
    response = requests.post(get_config_data['url'], headers=api_headers,
                            json=Payload.homepage_carousels())
    assert response.status_code == 200
    response_json = json.loads(response.text)
    print(response_json)
    assert "data" in response.json()


def test_homepage_livestream(get_config_data, api_headers): #画廊直播间检查
    response = requests.post(get_config_data['url'], headers=api_headers,
                            json=Payload.homepage_livestream())
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 200
    assert "data" in response.json()


def test_homepage_list_recommendation(get_config_data, api_headers):# 推荐系统
    response = requests.post(get_config_data['url'], headers=api_headers,
                            json=Payload.homepage_list_recommendation())
    assert response.status_code == 200                       
    response_json = json.loads(response.text)
    print(response_json)
    data = response_json.get('data')
    home_page_list_recommendation = data.get('listRecommendation')
    print(home_page_list_recommendation)
    assert home_page_list_recommendation is not None



def test_homepage_global_information_recommend(get_config_data, api_headers):# 主页左边的推荐列表
    response = requests.post(get_config_data['url'], headers=api_headers,
                            json=Payload.homepage_global_information_recommend())
    response_json = json.loads(response.text)

    # 判断 recommendChannels 数组是否为空
    recommend_channels = response_json['data']['globalInfo']['recommendChannels']
    assert len(recommend_channels) > 0

    assert response.status_code == 200


def test_homepage_nav_search_result(get_config_data, api_headers):
    response = requests.post(get_config_data['url'], headers=api_headers,
                            json=Payload.homepage_nav_search_result())
    assert response.status_code == 200

    # 解析返回结果
    data = json.loads(response.text)
    print(data)
    users = data['data']['search']['allUsers']['list']
    print(users)

    # 搜索"displayname": "automation"
    found_user = False
    for user in users:
        if user['creator']['displayname'] == 'automation':
            found_user = True
            break
    # 检查结果
    assert found_user == True

