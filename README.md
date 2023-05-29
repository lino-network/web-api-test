streamer: automation/Pwd@1234
viewer: automationviewer/Pwd@1234

pytest test_homepage.py --html=tests/report/report.html
pytest -k test_homepage_carousels