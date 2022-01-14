# pan.baidu.com-Batch-file-transfer
## 安装说明：

###  step1、pip install selenium

###  step2、下载自己版本（chrome浏览器输入chrome://settings/help的版本号）对应的chromedriver.exe（[ChromeDriver - WebDriver for Chrome - Downloads (chromium.org)](https://chromedriver.chromium.org/downloads)）

### step3、替换文件夹中原本的chromedriver.exe


## 使用说明：

### step1、将需要自动化转存网盘的网址与密码以第一列为网址第二列为密码一一对应的格式写入csv文件中（excel）。
### step2、运行获取百度网盘cookie.py，并快速在弹出的浏览器界面中登录自己的百度网盘账户,运行结束后文件目录下会出现baidu_cookie.json文件。(请误删除)(需要在30s内登录上百度网盘，如果网速过慢可以调大n，第六行time.sleep(n))
### step3、将百度网盘下载.py中的```f = open("修改成step1对应的文件名","r+",encoding="utf-8-sig",newline="")```，修改后运行。（可以默认写在url+password.csv中）

