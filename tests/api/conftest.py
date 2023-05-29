# 一些常用的钩子函数和fixture如下：
import os
import sys
curlPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curlPath)[0]
print(rootPath)
sys.path.append(os.path.split(rootPath)[0])
from loadData import payloadData
import loadData.payloadData as Payload

# pytest_configure(config)：在pytest的配置初始化时执行，可以用来设置全局的pytest配置。
# pytest_sessionstart(session)：在pytest测试会话开始时执行，可以用来初始化一些测试环境。
# pytest_sessionfinish(session, exitstatus)：在pytest测试会话结束时执行，可以用来清理测试环境。
# pytest_runtest_setup(item)：在每个测试用例执行前执行，可以用来准备测试数据和测试环境。
# pytest_runtest_teardown(item, nextitem)：在每个测试用例执行后执行，可以用来清理测试环境。
# pytest_addoption(parser)：用于向pytest添加自定义的命令行选项。
# pytest_generate_tests(metafunc)：用于自动生成测试用例，可以根据不同的测试参数自动生成多个测试用例。
# 自定义fixture：fixture是一种用于提供测试用例所需数据和对象的机制，可以在测试用例中通过装饰器的方式使用。在conftest.py中，你可以定义自己的fixture，以提供测试所需的数据和对象。常见的fixture有：request、tmpdir、monkeypatch、capfd等。

import pytest
import requests
import yaml
from loadData import payloadData


@pytest.fixture(scope='session')
def get_config_data():
    # 获取当前脚本所在文件夹路径
    print('44444444')
    print(os.getcwd())
    curPath = os.path.abspath(os.path.join(os.getcwd(), "../../config"))
    # 获取yaml文件路径
    print(curPath)
    yamlPath = os.path.join(curPath, "config.yaml")

    # open方法打开直接读出来
    with open(yamlPath, 'r', encoding='utf-8') as f:
        config = f.read()
    print(config)
    testData = yaml.load(config, Loader=yaml.FullLoader)  # 用load方法转字典
    return testData['apiData']


@pytest.fixture(scope='session')
def api_headers():
    headers = {
        # 'Authorization': 'Bearer YOUR_AUTH_TOKEN_HERE',
        'Content-Type': 'application/json'
    }
    return headers


@pytest.fixture(scope='session')
def api_url():
    return 'https://graphigo.prd.dlive.tv/'
    # return 'https://graphigo.stg.dlive.tv/'


@pytest.fixture(scope='session')
def auth_header(get_config_data):
    token = {'authorization': get_config_data['auth_token']}
    return token


@pytest.fixture(scope='session')
def get_login_auth(api_headers, get_config_data):
    response = requests.session().post(get_config_data['url'], headers=api_headers,
                                       json=payloadData.login(get_config_data['login_user'], get_config_data['pwd']))
    text = response.json()
    print(text)
    auth_token = text['data']['loginWithEmail']['me']['private']['accessToken']
    return auth_token





