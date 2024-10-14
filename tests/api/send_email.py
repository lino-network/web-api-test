import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import sys
import os
curlPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curlPath)[0]
print(rootPath)
sys.path.append(os.path.split(rootPath)[0])
import subprocess
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def create_directory_if_not_exists(directory_path):
    # 判断文件夹是否存在
    if not os.path.exists(directory_path):
        # 如果不存在，则创建文件夹
        os.makedirs(directory_path)
        print(f"文件夹 '{directory_path}' 已创建。")
    else:
        print(f"文件夹 '{directory_path}' 已存在。")


def get_report_server(report_path):
    # 定义命令和参数
    command = 'allure'  # 你的命令

    # 判断操作系统
    if sys.platform.startswith('win'):
        # Windows
        command += '.bat'  # Windows下使用.bat扩展名
    elif sys.platform.startswith('darwin'):
        # macOS
        command += ''  # macOS下不需要扩展名
    # 执行 allure serve 命令
    process = subprocess.Popen([command, 'open', report_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 获取输出并解析服务器地址
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if 'http' in str(output):
            server = str(output).split('<')[1].split('>')[0]
            return server
        if output:
         # 解码并查找服务器地址
            output_str = output.decode('utf-8')
            match = re.search(r'http://localhost:\d+', output_str)
            if match:
                print(f"Allure server is running at: {match.group(0)}")
                print("match:" + match.group(0))
                return match.group(0)
    # 等待进程结束
    process.wait()


def open_allure_report_and_screenshot(url, screenshot_path):
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # 启动时最大化窗口

    # 启动 Chrome 浏览器
    chrome_options.add_argument('-incognito')
    driver = webdriver.Chrome(chrome_options)

    try:
        # 打开 Allure 报告
        driver.get(url)

        # 等待页面加载
        time.sleep(5)  # 根据需要调整等待时间

        # 截图并保存
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

    finally:
        # 关闭浏览器
        driver.quit()


def send_email(subject, description, to_emails, attachment_path):
    from_email = 'apple2024826@outlook.com'  # 替换为您的邮箱
    password = 'Pwd@1234'        # 替换为您的邮箱密码

    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)  # 将多个收件人用逗号分隔
    msg['Subject'] = subject

    # 添加邮件正文
    msg.attach(MIMEText(description, 'plain'))

    # 添加附件
    with open(attachment_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
        msg.attach(part)

    # 发送邮件
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as server:  # 使用 Outlook 的 SMTP 服务器
            server.starttls()  # 启用 TLS
            server.login(from_email, password)
            server.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')


if __name__ == '__main__':
    # 请替换为您的 Allure 报告路径和截图保存路径
    script_path = os.path.dirname(os.path.abspath(__file__))
    print("脚本所在路径:", script_path)
    report_folder = script_path + '/report_screenshot'
    create_directory_if_not_exists(report_folder)
    r_path = script_path + '/report/results-710'    # Allure 报告的路径
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%b %d, %Y")
    path = report_folder + '/screenshot_' + str(currentDateAndTime) + '.png'  # 截图保存的路径
    url1 = get_report_server(r_path)
    open_allure_report_and_screenshot(url1, path)

    subject1 = 'API automation report'
    body = 'Automation report see below screenshot'
    receiver_emails = ["helen.liang@tron.network", "apple.zhang@tron.network"]
   # attachment_path1 = '/Users/apple.zhang/Desktop/code/web-api-test/tests/api/report_screenshot/screenshot_2024-08-28 18:14:51.840990.png'  # 替换为您的 PNG 图片路径

    send_email(subject1, body, receiver_emails, path)
