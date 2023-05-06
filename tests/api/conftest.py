# 一些常用的钩子函数和fixture如下：

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


import pytest

@pytest.fixture()
def auth_header():
    # return {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF1dG9tYXRpb24iLCJkaXNwbGF5bmFtZSI6ImF1dG9tYXRpb24iLCJhdmF0YXIiOiJodHRwczovL2ltYWdlLmRsaXZlY2RuLmNvbS9hdmF0YXIvZGVmYXVsdDgucG5nIiwicGFydG5lcl9zdGF0dXNfc3RyaW5nIjoiR0xPQkFMX1BBUlRORVIiLCJpZCI6IiIsImxpZCI6MCwidHlwZSI6ImVtYWlsIiwicm9sZSI6Ik5vbmUiLCJvYXV0aF9hcHBpZCI6IiIsImV4cCI6MTY4NjAxODA0MiwiaWF0IjoxNjgzMzM5NjQyLCJpc3MiOiJETGl2ZSJ9.bKZLy8k5iCrUpVOcyx0xuSII-a-Yhcbxws5ZB0AQZpk"}
    return {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImhlbGVudmlld2VyIiwiZGlzcGxheW5hbWUiOiJIZWxlbnN0cmVhbWVyIiwiYXZhdGFyIjoiaHR0cHM6Ly9pbWFnZXMucHJkLmRsaXZlY2RuLmNvbS9hdmF0YXIvOWYxNzdhN2QtYzdjNy0xMWVkLThkNTEtZDIxM2FjZDZmYTY5IiwicGFydG5lcl9zdGF0dXNfc3RyaW5nIjoiVkVSSUZJRURfUEFSVE5FUiIsImlkIjoiIiwibGlkIjowLCJ0eXBlIjoiZW1haWwiLCJyb2xlIjoiTm9uZSIsIm9hdXRoX2FwcGlkIjoiIiwiZXhwIjoxNjg2MDE5MjMwLCJpYXQiOjE2ODMzNDA4MzAsImlzcyI6IkRMaXZlIn0.mDnV-Ija4pVaf_AdWH49RirK1eBL0UKYU5PYs9Jyxcg"}

