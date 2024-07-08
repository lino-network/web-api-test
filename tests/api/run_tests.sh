#!/bin/bash

# 定义日期格式
DATE=$(date +%Y%m%d)

# 进入测试用例目录
cd /Users/helen/Downloads/Code/web-api-test/tests/api/

# 拉取最新的 master 分支
git pull origin master

# 执行 pytest 并指定结果输出目录
pytest --alluredir=./output-results-$DATE

# 生成 Allure 报告
allure generate ./output-results-$DATE -o ./output-report-$DATE --clean

# 打包生成的报告
zip -r output-report-$DATE.zip output-report-$DATE

# 发送邮件通知
python /Users/helen/Downloads/Code/web-api-test/tests/api/send_email.py "output-report-$DATE.zip"

# 保持服务器运行
wait
