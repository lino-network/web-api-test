import os
import sys
from datetime import datetime

curlPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curlPath)[0]
print(rootPath)
sys.path.append(os.path.split(rootPath)[0])
from tests.api.get_trend1 import get_allure
from tests.api.send_email import create_directory_if_not_exists, open_allure_report_and_screenshot
from tests.api.send_email import get_report_server
from tests.api.send_email import send_email

if __name__ == '__main__':
    os.system('ls')
    script_path = os.path.dirname(os.path.abspath(__file__))
    print("脚本所在路径:", script_path)
    report_folder = 'report_screenshot'
    report_path_folder = 'APIReport'
    create_directory_if_not_exists(script_path + '/' + report_folder)
    create_directory_if_not_exists(script_path + '/' + report_path_folder)
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%Y%m%d" + "_" + "%H%M%S")
    # report = './' + report_path_folder + '/report-' + currentTime
    # results = './' + report_path_folder + '/results-' + currentTime
    report = './' + report_path_folder + '/report'
    results = './' + report_path_folder + '/results'
    # 获取历史记录
    test_path1 = './'
    # # 需要生成的xml的路径
    allure_xml_path1 = results
    # 需要生成测试报告的路径
    allure_path1 = report
    get_allure(test_path1, allure_xml_path1, allure_path1)
    aa = os.listdir(allure_path1)
    for i in aa:
        if i == '.DS_Store':
            aa.remove(i)
    bb = sorted(aa, key=int)
    # print(bb[-1])
    # command = 'allure open ./allure_report/' + bb[-1]
    # print(command)
    # os.system(command)

    # os.system('pytest --alluredir=' + results)
    # os.system('allure generate ' + results + ' -o ' + report + ' --clean')

    path = report_folder + '/screenshot_' + str(currentTime) + '.png'  # 截图保存的路径
    # url1 = get_report_server(results)
    url1 = get_report_server(allure_path1 + '/' + str(bb[-1]))
    print(url1)
    open_allure_report_and_screenshot(url1, path)

    subject1 = 'API automation report'
    body = 'Automation report see below screenshot'
    receiver_emails = ["helen.liang@tron.network", "apple.zhang@tron.network"]
    #receiver_emails = ["apple.zhang@tron.network"]

    send_email(subject1, body, receiver_emails, path)
    os.system('taskkill /F /IM java.exe')

