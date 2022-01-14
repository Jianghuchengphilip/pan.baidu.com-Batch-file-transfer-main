from selenium import webdriver
import csv
import json
import time
f = open("url+password.csv","r+",encoding="utf-8-sig",newline="")#将百度网盘网址与密码存在csv文件中
readers = csv.reader(f)
for reader in readers:
    try:
        print(reader[0], reader[1], "传输中。。。。")
        web = webdriver.Chrome(executable_path="./chromedriver.exe")
        web.get(reader[0])
        cookie_in = open("baidu_cookie.json", "r+", encoding="utf-8")
        listcookies = json.loads(cookie_in.read())
        for cookie in listcookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            web.add_cookie(cookie_dict=cookie)
        web.refresh()
        web.get(reader[0])
        web.find_element_by_id("accessCode").send_keys(reader[1])
        web.find_element_by_class_name("g-button-blue-large").click()
        time.sleep(3)
        web.find_element_by_class_name("tools-share-save-hb").click()
        time.sleep(3)
        js = 'document.getElementsByClassName("g-button-blue-large")[1].click()'
        web.execute_script(js)
        web.quit()
        print(reader[0], reader[1], "传输完成。。。。")
    except:
        pass