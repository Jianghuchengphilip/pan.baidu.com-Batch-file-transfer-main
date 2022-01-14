from selenium import webdriver
import time
import json
web = webdriver.Chrome(executable_path="./chromedriver.exe")
web.get("https://pan.baidu.com/")
time.sleep(30)
baidu_cookie = web.get_cookies()
print(baidu_cookie)
with open("baidu_cookie.json","w+",encoding="utf-8") as f:
    f.write(json.dumps(baidu_cookie))
