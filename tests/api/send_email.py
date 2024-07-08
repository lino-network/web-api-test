import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import sys

def send_email(zip_file, receiver_emails):
    sender_email = 'helenliang2024sr71@outlook.com'
    password = 'hjq1989517'
    
    # 创建邮件对象
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_emails)
    message["Subject"] = "Automated Test Report"
    
    # 邮件正文内容
    body = "Hello, please find the test report attached."
    message.attach(MIMEText(body, "plain"))
    
    # 添加压缩文件为附件
    attachment = open(zip_file, 'rb')
    base = MIMEBase('application', 'octet-stream')
    base.set_payload(attachment.read())
    encoders.encode_base64(base)
    base.add_header('Content-Disposition', f'attachment; filename={zip_file}')
    message.attach(base)
    
    # SMTP服务器设置（以 Outlook 为例）
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    server.login(sender_email, password)
    
    # 发送邮件
    server.send_message(message)
    server.quit()

if __name__ == "__main__":
    zip_file = sys.argv[1]
    receiver_emails = ["helen.liang@tron.network", "apple.zhang@tron.network"]  # 添加所有的收件人邮箱
    send_email(zip_file, receiver_emails)
