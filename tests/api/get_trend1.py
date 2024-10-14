import os
import json
import ast

from tests.api.get_report import get_report_server, open_allure_report_and_screenshot


# 获取下一个文件夹的名称，以及最近一个趋势的数据
def get_dir(allure_path):
    if not os.path.exists(allure_path):
        # 如果不存在，则创建文件夹
        os.makedirs(allure_path)
        print(f"文件夹 '{allure_path}' 已创建。")
    else:
        print(f"文件夹 '{allure_path}' 已存在。")
    print("allure_path", allure_path)
    # 判断之前是否生成过报告
    first_path = allure_path + "/1"
    if os.path.exists(first_path):
            all_result_dir = os.listdir(allure_path)
            # 这个地方要注意，如果是mac，listdir获取到一个.DS_store的文件，使用下方的sort会报错，因而要先all_result_dir中将它remove掉
            for i in all_result_dir:
                if i == '.DS_Store':
                    all_result_dir.remove(i)
            print('00000000')
            print(all_result_dir)
            print(type(all_result_dir))
            all_result_dir.sort(key=int)

            # 取出最近一次执行的历史趋势的json
            history_file = os.path.join(allure_path, str(int(all_result_dir[-1])), 'widgets', 'history-trend.json')
            with open(history_file) as f:
                data = f.read()
            # 将下一次要生成的文件夹序号以及最新的历史趋势数据返回
            return int(all_result_dir[-1]) + 1, data
    else:
        # 如果之前没有生成过，就创建一个文件夹
            os.makedirs(os.path.join(allure_path, '1'))
            return 1, None


# 获取最新生成的趋势数据，这个数据里其实只有本次的结果，没有历史的结果
def update_new_single(buildOrder, allure_path):
    new_single_file = os.path.join(allure_path, str(buildOrder), 'widgets', 'history-trend.json')
    with open(new_single_file, 'r+') as f:
        # data1 = f.read()
        data = json.load(f)
        # 写入本次是第几次执行、测试报告的路径
        data[0]["buildOrder"] = int(buildOrder)
        data[0]['reportUrl'] = f'http://localhost:63342/web-api-test/tests/api/allure_report/{str(buildOrder)}/index.html'
    with open(new_single_file, 'w+') as f:
        json.dump(data, f)


# 重写新生成的history-trend.json文件，用历史+本次=最新
def update_file(buildOrder, allure_path):
    old_data = os.path.join(allure_path, str(int(buildOrder) - 1), 'widgets', 'history-trend.json')
    new_data = os.path.join(allure_path, str(int(buildOrder)), 'widgets', 'history-trend.json')
    with open(old_data) as f:
        old = json.load(f)
        dict = []
        for i in range(len(old)):
            dict.append(old[i])
        print(dict)
    with open(new_data) as f:
        r = f.read()
        new_list = ast.literal_eval(r)
        for i in range(len(dict)):
            new_list.append(dict[i])
    with open(new_data, 'w') as f:
        json.dump(new_list, f)


# 调用
def test_allure(test_path, allure_xml_path, allure_path):
    print(allure_path)
    buildOrder, old_data = get_dir(allure_path)
    # 先使用command生成xml文件
    command = f'pytest {test_path} -s --alluredir={os.path.join(allure_xml_path, str(buildOrder))}'
    os.system(command)
    # 再使用command1由xml生成json文件的测试报告
    command1 = f'allure generate {os.path.join(allure_xml_path, str(buildOrder))} -o {os.path.join(allure_path, str(buildOrder))} --clean'
    print(command1)
    os.system(command1)
    update_new_single(buildOrder, allure_path)
    if buildOrder != 1:
        update_file(buildOrder, allure_path)


# os.system('ls')
# script_path = os.path.dirname(os.path.abspath(__file__))
# print("脚本所在路径:", script_path)
# 需要执行的测试脚本的路径
# test_path1 = "./test_streamerIncentive.py"
# # 需要生成的xml的路径
# allure_xml_path1 = "./allure_results"
# # 需要生成测试报告的路径
# allure_path1 = "./allure_reports"
# test_allure(test_path1, allure_xml_path1, allure_path1)
# aa = os.listdir(allure_path1)
# for i in aa:
#     if i == '.DS_Store':
#         aa.remove(i)
# bb = sorted(aa, key=int)
# print(bb[-1])
# command = 'allure open ./allure_reports/' + bb[-1]
# print(command)
# os.system(command)
# print(allure_path1 + '/' + str(bb[-1]))
# url1 = get_report_server(allure_path1 + '/' + str(bb[-1]))
# print(url1)
# open_allure_report_and_screenshot(url1, './report_screenshot')

# allure_path1 = './APIReport/report'
# aa = os.listdir(allure_path1)
# for i in aa:
#     if i == '.DS_Store':
#         aa.remove(i)
# bb = sorted(aa, key=int)
# print(allure_path1 + '/' + str(bb[-1]))
# url1 = get_report_server(allure_path1 + '/' + str(bb[-1]))
# print(url1)
# open_allure_report_and_screenshot(url1, './report_screenshot')


