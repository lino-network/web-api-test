streamer: automation/Pwd@1234
viewer: automationviewer/Pwd@1234

pytest test_homepage.py --html=tests/report/report.html
pytest -k test_homepage_carousels


执行全部的case:
1.cd 到当前用例的路径
2.执行用例输入命令：pytest --alluredir=./output-results    # alluredir后面接的是报告的路径，名字可以写跑的日期
3.生成结果： allure generate ./output-results -o ./output-report --clean

例子: 
pytest --alluredir=./output-results-20230629
allure generate ./output-results-20230629 -o ./output-report-20230629 --clean