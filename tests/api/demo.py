# import json
# import requests
#
#
# import loadData.payloadData as Payload
#
#
# def test_follow_user(get_config_data, auth_header):
#     print(get_config_data)
#     response = requests.post(get_config_data['url'], headers=auth_header,
#                              json=Payload.follow_user(get_config_data['follow_user']))
#     response_json = json.loads(response.text)
#     print(response_json)
#     assert response.status_code == 200
#     assert response_json['data']['follow']['err'] is None
#
#
# def test_follow_user_in_sidebar(get_config_data, auth_header):
#     response = requests.post(get_config_data['url'], headers=auth_header,
#                              json=Payload.sidebar_follow_user_list())
#     response_json = json.loads(response.text)
#     print(response_json)
#     assert response.status_code == 200
#     follow_list = response_json['data']['me']['private']['followeeFeed']['list']
#     print(follow_list)
#     for i in follow_list:
#         if i['username'] == 'appletron':
#             print('44444')
#             assert True
#
#
#
import json

import requests


# def calculate_new_viewers(viewers, base_increase=0.1, increase_rate=0.0001):
#
#     increase = base_increase + viewers * increase_rate
#
#     new_viewers = viewers + int(viewers * increase)
#     return new_viewers
#
#
# a = calculate_new_viewers(1, 0.1, 4)
# print(a)


def create(display, email, pwd):
    headers = {
        'Content-Type': 'application/json'
    }

    payload = {
          "operationName": "RegisterWithEmail",
          "variables": {
            "email": email,
            "password": pwd,
            "recaptchaToken": "0.mxf8C9RktVD7fvKmFkaYgpcpY_hisVkdjKXFYYh6tM_HaUIlOUiAtmIaQ0pXGtPFm-ChPiT60-Kw3LjRR_d8Y7uHBsgLw4yUurC_sJY9bkCX4So-A0XACrGriaKVRVP0gyxgYLUttZ-EyiiJ0sXceCwThfqbcodf_Q_t2tRp7RyehdBaCz0Gh7TkO7NxiZEi7k3nB07DcWG6gsljKXy6MepD6rqeqhWSA51phLe-Vsg_OO1say_xKiYnCSfa_E6RrvuwSxr9N_jh-r3dIdtXqD_Z0_IWIboXSI28rgbkLIJjkiRY9DPfbXAnIXFnO6IeprVtQXt-EfZysc2VQ0RCe4J7I8s_iYub_wKGzT780yjx3_q8KcfTK-MfEli4R4v9Z8TzytmiUGGh_Y8E2HB_X4N3ZXy7sk5kkybQBiWet2wbvn6q2bHQLA8fK5o9BOq6_dpAEsxtlJ5clr8Jrz66UyeBfE_qesFHzSYsZ6XWuDWpUrJ3tkt2c3-6omG6BgQqc1GDUW1qmY25gs8AmeGmHfzJzjUV5Zhlc0NPhoXAHBmIbjPMGMiJBIykBx-ws2wZeqqDi8yztwYXzU9umTCx6eKTROtMSRsHrRF5vt8SIYaC5YadUiZFSCDlKQ9wydUsI2Avt98ZEXk2HcTesOyyzPNkwtCRQU-7DY-y9BZH2iEMxl6GV-Widv8N0C3AYQCxF1a8-HfcgF3Crtru8TZJ-pzmdtlGuskLGiaT2nAz_I2QEdBs-mjQz9bl9V0nRNgcM3DpXj7pmL7q4iNJmxC6LA.hy0IXMyNboTqUZ1SAGcyzg.4934e6dc6d5b7d5b59a0b24106e4c80ef9e4dd0e35a63fd650f3b5e05b2c3de5",
            "deviceType": "WEB",
            "displayname": display,
            "language": "zh"
          },
          "extensions": {
            "persistedQuery": {
              "version": 1,
              "sha256Hash": "01dd44cb2b5a8bd5eea8d3b7024295553447d2dc64490a2f15cd9332a1fc8c57"
            }
          }
        }
    response = requests.post('https://graphigo.stg.dlive.tv/', headers=headers, json=payload)
    response_json = json.loads(response.text)
    # print(response_json)
    auth_token = response_json['data']['registerWithEmail']['me']['private']['accessToken']
    return {'authorization': auth_token}


# print(create('nios1@nqmo.com', 'password1234'))
for i in range(26, 37):
    e = str(i) + '@nqmo.com'
    p = 'password1234'
    d = str(i) + 'nqmo'
    print(create(d, e, p))




