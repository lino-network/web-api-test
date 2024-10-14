
#/bin/bash
script_dir=$(dirname "$(realpath "$0")")
echo "当前脚本所在目录: $script_dir"

# 定义日期格式
DATE=$(date +%Y%m%d)
echo "当前脚本所在目录: $script_dir"

# 进入测试用例目录
cd script_dir

# 拉取最新的 master 分支
git pull origin master

# 执行 pytest 并指定结果输出目录
pytest --alluredir=./report/results-$DATE

# 生成 Allure 报告
allure generate ./report/results-$DATE -o ./report/report-$DATE --clean

# 打包生成的报告
#zip -r output-report-$DATE.zip output-report-$DATE

# 发送邮件通知
python /Users/helen/Downloads/Code/web-api-test/tests/api/send_email.py "output-report-$DATE.zip"

# 保持服务器运行
wait
