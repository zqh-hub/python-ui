##### Python_UI

###### 开启浏览器

```python
from selenium import webdriver

# Safari([ driver path ])
driver = webdriver.Safari()
driver.get("https://www.baidu.com")
driver.quit()

注意：最新版本的selenium不需要再指定driver的路径，直接访问即可
# seleium 4.x
from selenium import webdriver
web = webdriver.Chrome()
web.get("https://blog.csdn.net/")
```
###### 加载策略
|策略|解释|
|--|--|
none|等待html下载完成，不等待解析完成就开始执行操作，selenium 会直接返回
eager|等待HTML 完全加载和解析完毕就开始执行操作，忽略加载样式表、图像和子框架
normal|等待整个页面加载完毕再开始执行操作
```python
# selenium 4.x
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = "normal"
web = webdriver.Chrome(options=options)
web.get("https://blog.csdn.net/")

web.quit()
```
###### 访问操作

```python
driver.back()  # 返回
driver.forward()  # 前进
driver.refresh()  # 刷新
```

###### 获取标题

```python
driver.title
```
###### 获取焦点
```python
# 返回的是一个元素，这个元素与通过find_element定位到的无异，可以执行send_key等方法
ele = driver.switch_to.active_element

# 参考：https://blog.csdn.net/huilan_same/article/details/52338073
```
###### 判断元素是否可用
```python
# 可用返回true,不可用返回false
val attr = driver.findElement(By.name("btnK")).isEnabled()
```
###### 判断元素是否被选择
```python
# 被选择返回true,否则为false
element.isSelected()
```
###### 获取tagName
```python
element.tag_name
```
###### 获取元素的坐标/尺寸
```python
element.rect # {'height': 44, 'width': 548, 'x': 298, 'y': 209.265625}
```
###### 获取元素的CSS
```python
element.value_of_css_property('属性名')
```
###### 获取网址

```python
driver.current_url
```

###### 获取当前页面句柄

```python
driver.current_window_handle
```

###### 获取属性的值

```python
kw_input = driver.find_element(By.XPATH, "//input[@id='kw']")
class_atr = kw_input.get_attribute("class")
```
###### 隐式等待
```python
driver.implicitly_wait(time) #此方法有局限性，一般不用
```

###### 显式等待

```python
WebDriverWait(driver, 等待时间,频率).until(ec.条件((元素)))

eg:
WebDriverWait(driver, 13, 0.3).until(ec.visibility_of_element_located((By.XPATH, "//input[@id='kw']")))
```

###### 切换iframe

```python
# 方式一：
driver.switch_to.frame(name/index/iframe_ele) # index从1开始

# 方式二：
WebDriverWait(driver,10).until(ec.frame_to_be_available_and_switch_to_it(name/index/iframe_ele))
```

###### 返回iframe

```python
# 返回默认，即最顶层
driver.switch_to.default_content()

# 返回父级iframe
driver.switch_to.parent_frame()
```

###### 窗口切换

```python
driver.switch_to.window(handles[-1])

# 注意：先进的在后面
百度首页 ['page-893F7E89-9B14-330B2E3F69BE']
进去所有 ['page-23C60CC7-98C1-BECC6908EE7E', 'page-893F7E89-9B14-330B2E3F69BE']
```

###### 等待新窗口出现

```python
# 一定要在新的窗口打开之前获取handles
handles = driver.window_handles
driver.find_element(By.XPATH, '//*[@id="1"]/h3/a').click()
# 新的窗口打开，hanles变化，进行等待操作
WebDriverWait(driver, 10).until(ec.new_window_is_opened(handles))
# 再次获取，进行切换
handles = driver.window_handles
driver.switch_to.window(handles[0])
```

###### alert切换

```python
alert = driver.switch_to.alert  # 切换
alert.accept()  # 接受
alert.dismiss() # 取消
alert.text # 获取文本
# 有时，使用.text获取不到文本值，可以使用ele.get_attribute("textContent")尝试

```

###### 等待alert

```python
WebDriverWait(driver, 10).until(ec.alert_is_present())
alert = driver.switch_to.alert
# alert_is_present好像也能自己进行切换，但是最好还是自己进行

eg:
alert = ec.alert_is_present()(driver)
if alert:
    alert.accept()
else:
    print("没有alert")
```
###### Prompt 提示框
```python
driver.find_element(By.LINK_TEXT, "See a sample prompt").click()
alert = Alert(driver)
# 向提示框输入文字
alert.send_keys("Selenium")
alert.accept()
  
```
###### ActionChains鼠标操作
```python
from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).move_to_element(element).perform()
```

| 方法              | 描述                   |
| ----------------- | ---------------------- |
| click()           | 单击鼠标左键           |
| click_and_hold()  | 点击鼠标左键，不松开   |
| context_click()   | 点击鼠标右键           |
| double_click()    | 双击鼠标左键           |
| drag_and_drop()   | 拖拽到某个元素然后松开 |
| move_to_element() | 鼠标移动到某个元素     |
| key_down()        | 按下某个键盘上的键     |
| key_up()          | 松开某个键             |

```python
element.send_keys("1234")
# 输入123，并按enter键
ele.send_keys("1234"+Keys.ENTER)
actions.key_down(Keys.COMMAND).send_keys('a').key_up(Keys.COMMAND)  # 全选
actions.key_down(Keys.COMMAND).send_keys('c').key_up(Keys.COMMAND)  # 复制
actions.perform() # 执行
```
###### http代理
```python
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--proxy-server=http://127.0.0.1:8888")
driver = webdriver.Chrome(executable_path="F:\work\driver\chromedriver_89_0_4389_23.exe", chrome_options=chromeOptions)

# 下面的方式也可以，不过我没实验成功
PROXY = "http://127.0.0.1:8888"
desired_capabilities = webdriver.DesiredCapabilities.CHROME["proxy"] = {'proxyType': 'MANUAL',
                                                                        "ftpProxy": PROXY,
                                                                        "sslProxy": PROXY,
                                                                        'httpProxy': PROXY}
driver = webdriver.Chrome(executable_path="F:\work\driver\chromedriver_89_0_4389_23.exe",
                          desired_capabilities=desired_capabilities)
```
###### Select操作

```python
select = Select(element)
select.select_by_index()  # 通过下标
select.select_by_value()  # 通过value属性 
select.select_by_visible_text()  # 通过select的文本
```
###### JS 滑动页面
```python
# 将ele移动到可视区域，元素顶部[底部]与浏览器顶部[底部]对齐
driver.execute_script("arguments[0].scrollIntoView([false]);", element)

# 将整个页面滚动到底部与顶部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 底部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")  # 顶部
```

###### JS移除属性

```python
driver.execute_script("arguments[0].removeAttribute("某属性")",element)

eg:
driver.execute_script('arguments[0].removeAttribute("readonly")',element)
```

###### 文件上传Win32

```python
import win32gui
import win32con
# FindWindow(class,text)
# FindWindowEx(父级,搜索的范围,子级的class,子级的text)
# "C:\\Users\\eric\\Documents\\new.txt"

def upload_file_by_win32(file_path):
    dialog = win32gui.FindWindow("#32770", "打开")  # 最高级
    combo_box_32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # ComboBoxEx32 的父级是 #32770
    combo_box = win32gui.FindWindowEx(combo_box_32, 0, "ComboBox", None) # ComboBox 的父级是 ComboBoxEx32
    edit = win32gui.FindWindowEx(combo_box, 0, "Edit", None) # edit 的父级是 ComboBox
    
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)") # 打开 的父级是 #32770
    
    # 进行文件发送
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
```

###### selenium控制已经登陆的网站
```python
# 此针对的是mac
# 第一步,打开chrome的debug模式
vim .zprofile
PATH="/Applications/Google Chrome.app/Contents/MacOS:${PATH}"
export PATH

命令行运行：
Google\ Chrome -remote-debugging-port=9222   # 注意，运行前要把浏览器的所有进行都关闭

# python脚本
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"    # debug地址
driver = webdriver.Chrome(path_config.CHROME_DRIVER_PATH, options=options)
driver.maximize_window()
driver.get("https://situnionpay-dashboard.pinpula.com/admin/index")
time.sleep(3)
driver.find_element(By.XPATH, "//span[text()='基础功能']").click()

time.sleep(3)
driver.quit()
```
###### cookie操作
```python
driver.add_cookie({"name": "key", "value": "value"})
driver.get_cookie("foo")  # 获取指定的字段
driver.get_cookies()  # 获取全部

driver.delete_cookie("test1")  # [{'name': 'test2', 'path': '/'}, {'name': 'test1', 'path': '/'}] 删除后：只有name=test2的了

driver.delete_all_cookies() # 删除所有

# 例子：
# getcookie.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("F:\work\driver\chromedriver_89_0_4389_23.exe")
driver.get("https://www.tapd.cn/cloud_logins/login")
driver.find_element(By.ID, "username").send_keys("zhaoqinghe@tecpie.com")
driver.find_element(By.ID, "password_input").send_keys("Zqh139499")
driver.find_element(By.ID, "tcloud_login_button").click()
cookies = driver.get_cookies()
print(type(cookies))
with open("cookie.txt", "w") as f:
    f.write(str(cookies))

driver.quit()

# addcookie.py
import time

from selenium import webdriver

with open("cookie.txt", "r") as f:
    data = f.read()
cookies = eval(data)
driver = webdriver.Chrome("F:\work\driver\chromedriver_89_0_4389_23.exe")
driver.get("https://www.tapd.cn/my_worktable#&filter_close=true")
driver.maximize_window()
for i in cookies:
    driver.add_cookie(i)

driver.refresh()	# 这里一定要刷新
driver.quit()
```
###### Same-Site Cookie属性
```python
# Same-Site的作用
在实际操作中，我们在“知乎”上可能会要点击链接跳转到第三方的网站，这样，如果第三方是恶意网站，就会泄露信息。Same-Site 就是用来限制是否发送给第三方网站信息
# 三个参数
Strict：
	最为严格，完全禁止第三方 Cookie，跨站点时，任何情况下都不会发送 Cookie
	Set-Cookie: CookieName=CookieValue; SameSite=Strict;
Lax：
	规则稍稍放宽，大多数情况也是不发送第三方 Cookie，但是导航到目标网址的 Get 请求除外
	Set-Cookie: CookieName=CookieValue; SameSite=Lax;
None：
	Chrome 计划将Lax变为默认设置。这时，网站可以选择显式关闭SameSite属性，将其设为None。不过，前提是必须同时设置Secure属性（Cookie 只能通过 HTTPS 协议发送），否则无效
	Set-Cookie: widget_session=abc123; SameSite=None; Secure
	
# selenium
driver.add_cookie({"name": "foo", "value": "value", 'sameSite': 'Strict'})
driver.add_cookie({"name": "foo1", "value": "value", 'sameSite': 'Lax'})
```
###### browsermobproxy 
```python
# 参考：https://zhuanlan.zhihu.com/p/363008064

from browsermobproxy import Server
from selenium import webdriver

server = Server(r"F:\work\driver\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat")
server.start()
proxy = server.create_proxy()
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server={0}'.format(proxy.proxy))
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome(executable_path="F:\\work\\driver\\chromedriver.exe", options=options)
proxy.new_har("my_test", options={'captureHeaders': True, 'captureContent': True})
driver.get("https://www.baidu.com")
res = proxy.har
with open("proxy_res.txt", 'w', encoding="utf-8") as f:
    f.write(str(res))
```
###### 破解滑动验证码
```python
# 参考
# 参考：https://www.cnblogs.com/zgn1666818478/p/13151052.html     https://www.cnblogs.com/lmx123/p/9246215.html
import time
from collections import Counter
from functools import reduce

import cv2
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/coco/Documents/YZT/unionpay_ui/driver/chromedriver")
driver.maximize_window()
driver.get("https://situnionpay-dashboard.pinpula.com/admin/login")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("15518612123")
driver.find_element(By.XPATH, "//span[text()='获取验证码']/parent::button").click()
time.sleep(1)
img = driver.find_element(By.XPATH, "//div[@class='verify-img-panel']")
location = img.location
size = img.size
print(location, size)
left, up = location["x"] * 2, location["y"] * 2
right, down = left + size["width"] * 2, up + size["height"] * 2
driver.save_screenshot("all_img.png")
all_img = Image.open("all_img.png")
img_ver = all_img.crop((left, up, right, down))
img_ver.save("captcha.png")

''' -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- '''
img = cv2.imread("captcha.png", 0)
img = cv2.GaussianBlur(img, (3, 3), 0)
canny = cv2.Canny(img, 200, 600)
x_len, y_len = canny.shape
x_arr = []
for i in range(1, x_len):
    for j in range(1, y_len):
        if canny[i, j] == 255:
            x_arr.append(j)
print("顺序打印看一下：", sorted(x_arr))
# 根据频率统计得到缺口距离y轴距离
former_dict = Counter(x_arr).most_common(5)
distance = max(dict(former_dict).keys()) + 17
print("distance = ", distance)
''' -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- '''
track = []
current = 0  # 当前位移
mid = distance * 4 / 5  # 设定一个阈值进行改变加速度
t = 1  # 计算间隔
v = 0  # 初速度
while current < distance:
    if current < mid:
        a = 1  # 加速度为正1
    else:
        a = -2  # 加速度为负2
    v0 = v  # 初速度v0
    v = v0 + a * t  # 当前速度v = v0 + at
    # 移动距离x = v0t + 1/2 * a * t^2
    move = v0 * t + 1 / 2 * a * t * t
    current += move  # 当前位移
    track.append(round(move))  # 加入轨迹

''' -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- '''
drag = driver.find_element(By.XPATH, "//div[@class='verify-move-block']")
ActionChains(driver).click_and_hold(drag).perform()
filter_track = list(filter(lambda x: x > 0, track))
print("过滤掉为0的轨迹列表：", filter_track)
print("reduce获取到和值：", reduce(lambda x, y: x + y, track))
for dis in track[:-12]:
    ActionChains(driver).move_by_offset(xoffset=dis, yoffset=0).perform()
ActionChains(driver).release(drag).perform()
time.sleep(4)

```
###### logging

```python
# 级别
DEBUG,INFO,WARNING,ERROR,CRITICAL

# code
import time
import logging
from common import dir_config

class MyLog:
    def loging(self, msg, level):
        # 日志收集器
        my_logging = logging.getLogger("zqh_log")
        
        # 设置级别
        my_logging.setLevel("DEBUG")
        log_format = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        
        # 创建输出渠道
        handler = logging.StreamHandler()
        handler.setLevel("DEBUG")
        handler.setFormatter(log_format)

        # 输出到文件及指定格式
        shot_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        file_handler = logging.FileHandler(dir_config.log_path + "{0}_log.txt".format(shot_time), encoding="utf-8")
        file_handler.setLevel("DEBUG")
        file_handler.setFormatter(log_format)

        # 进行对接
        my_logging.addHandler(handler)
        my_logging.addHandler(file_handler)

        if level == "DEBUG":
            my_logging.debug(msg)
        elif level == "INFO":
            my_logging.info(msg)
        elif level == "WARING":
            my_logging.warning(msg)
        elif level == "ERROR":
            my_logging.error(msg)
        elif level == "CRITICAL":
            my_logging.critical(msg)

        # 关闭渠道
        my_logging.removeHandler(handler)
        my_logging.removeHandler(file_handler)
```

###### Unittest report

```python
import time
import unittest
from common import dir_config
from common.HTMLTestRunner import HTMLTestRunner
from case.login_case import LoginCase

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTests(loader.loadTestsFromTestCase(LoginCase))
shot_time = time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time()))
with open(dir_config.report_path + "{}_report.html".format(shot_time), "wb") as report:
    runner = HTMLTestRunner(stream=report, verbosity=2, title="我的report", description="哈哈")
    runner.run(suite)
```

###### pytest

```python
# 搜索规则
默认会从项目根目录进行搜索测试用例，搜索规则：
	1、符合命名规则 test_*.py 或者 *_test.py 的文件
	2、以test_开头的函数名
	3、以Test开头的测试类(没有__init__函数)中test_开头的函数

# ptest-mark
在测试用例/测试类前加上：@pytest.mark.标记名
可多次加mark
@pytest.mark.smoke
@pytest.mark.demo
def test_01(self):
	pass

# pytest 运行
pytest -s  -s:会输出日志
pytest -m 标记名  -m:搜索带有 标记名 的测试用例
```

###### pytest fixtures

```python
在测试用例中创建"conftest.py"，这个文件要与测试用例平级，或者是测试用例的父级
import pytest
from selenium import webdriver
from data import common_data
from page.index_page import IndexPage
from page.login_page import LoginPage

driver = None


# 声明这个函数是fixture,scope是指定这个函数的范围，默认是function
@pytest.fixture(scope="class")
def access_web():
    # 前置
    global driver
    driver = webdriver.Chrome(common_data.driver)
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    driver.get("http://localhost:7070/login?from=%2F")
    driver.maximize_window()
    yield driver, login_page, index_page   # 分割线，返回值
    driver.close()


@pytest.fixture()
def refresh_page():
    global driver
    yield
    driver.refresh()
    
    
# conftest.py创建好后，进入测试用例

@pytest.mark.usefixtures("access_web")   # 范围是calss的fixture
class TestLoginCase:
    @pytest.mark.usefixtures("refresh_page")  # 范围是function的fixture
    def test_success_login(self, access_web): # 通过函数名进行传返回值
        access_web[1].submit_login("admin", "8161f26d2408481f8e92f31ad617e28d")
        assert access_web[2].def_get_welcome_title() == "欢迎来到 Jenkins!"
```

###### pytest参数化

```python
 # success_data就是success_login的参数名
  @pytest.mark.parametrize("success_data", login_data.success_login)
    def test_success_login(self, access_web, success_data):
        access_web[1].submit_login(success_data["username"], success_data["password"])
        assert access_web[2].def_get_welcome_title() == success_data["msg"]
```

###### pytest的重运行

```python
插件：pip install pytest-rerunfailures
使用方式：
	pytest --reruns 重试次数
	pytest --reruns 重试次数 --reruns-delay 重试间隔(s)
```

###### pytest测试报告

```python
插件：pip install pytest-html

使用：
1、生产JunitXML格式的测试报告：--junitxml=相对路径（相对项目）/Output/report/xxx.xml
2、生产result log 格式的测试报告：--resultlog=Output/report/log.txt
3、生产html格式的测试报告：--html=Output/report/test.html
```

###### allure报告

```python
1、安装allure
 > 下载Homebrew
 > brew install allure
2、allure-pytest
 > pip install allure-pytest
3、命令
 pytest --alluredir=保存路径
 allure serve 保存路径     ---生成在线网页
 allure generate 保存路径    ---生成离线网页，allure-report文件夹，点击index.html查看
 allure generate 保存的路径 --clean   ---更新离线网页
```

###### jenkins与allure

```python
1、jenkins 下载插件 Allure
2、jinkins 指定allure安装目录
	Global Tool Configuration --- Allure
3、job与allure进行配置
**注意：
	下面的alluredir、allure-results、allure-report路径要注意
```

![ui-001](/Users/eric/Documents/python/python_code/python_ui/note/img/ui-001.png)

![](/Users/eric/Documents/python/python_code/python_ui/note/img/ui-002.png)

![](/Users/eric/Documents/python/python_code/python_ui/note/img/ui-003.png)

###### 重置Jenkins的构建历史序号

```groovy
item = Jenkins.instance.getItemByFullName("your-job-name-here")
//THIS WILL REMOVE ALL BUILD HISTORY
item.builds.each() { build ->
  build.delete()
}
item.updateNextBuildNumber(1)
```



###### 附：HTMLTestRunner.py

```python
# coding=utf-8
"""
A TestRunner for use with the Python unit testing framework. It
generates a HTML report to show the result at a glance.
The simplest way to use this is to invoke its main method. E.g.
    import unittest
    import HTMLTestRunner
    ... define your tests ...
    if __name__ == '__main__':
        HTMLTestRunner.main()
For more customization options, instantiates a HTMLTestRunner object.
HTMLTestRunner is a counterpart to unittest's TextTestRunner. E.g.
    # output to a file
    fp = file('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title='My unit test',
                description='This demonstrates the report output by HTMLTestRunner.'
                )
    # Use an external stylesheet.
    # See the Template_mixin class for more customizable options
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
    # run the test
    runner.run(my_test_suite)
------------------------------------------------------------------------
Copyright (c) 2004-2007, Wai Yip Tung
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:
* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.
* Neither the name Wai Yip Tung nor the names of its contributors may be
  used to endorse or promote products derived from this software without
  specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER
OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# URL: http://tungwaiyip.info/software/HTMLTestRunner.html

__author__ = "Wai Yip Tung,  Findyou"
__version__ = "0.8.2.2"

"""
Change History
Version 0.8.2.1 -Findyou
* 改为支持python3
Version 0.8.2.1 -Findyou
* 支持中文，汉化
* 调整样式，美化（需要连入网络，使用的百度的Bootstrap.js）
* 增加 通过分类显示、测试人员、通过率的展示
* 优化“详细”与“收起”状态的变换
* 增加返回顶部的锚点
Version 0.8.2
* Show output inline instead of popup window (Viorel Lupu).
Version in 0.8.1
* Validated XHTML (Wolfgang Borgert).
* Added description of test classes and test cases.
Version in 0.8.0
* Define Template_mixin class for customization.
* Workaround a IE 6 bug that it does not treat <script> block as CDATA.
Version in 0.7.1
* Back port to Python 2.3 (Frank Horowitz).
* Fix missing scroll bars in detail log (Podi).
"""

# TODO: color stderr
# TODO: simplify javascript using ,ore than 1 class in the class attribute?

import datetime
import io
import sys
import time
import unittest
from xml.sax import saxutils
import sys


# ------------------------------------------------------------------------
# The redirectors below are used to capture output during testing. Output
# sent to sys.stdout and sys.stderr are automatically captured. However
# in some cases sys.stdout is already cached before HTMLTestRunner is
# invoked (e.g. calling logging.basicConfig). In order to capture those
# output, use the redirectors for the cached stream.
#
# e.g.
#   >>> logging.basicConfig(stream=HTMLTestRunner.stdout_redirector)
#   >>>

class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)


# ----------------------------------------------------------------------
# Template

class Template_mixin(object):
    """
    Define a HTML template for report customerization and generation.
    Overall structure of an HTML report
    HTML
    +------------------------+
    |<html>                  |
    |  <head>                |
    |                        |
    |   STYLESHEET           |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </head>               |
    |                        |
    |  <body>                |
    |                        |
    |   HEADING              |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   REPORT               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |   ENDING               |
    |   +----------------+   |
    |   |                |   |
    |   +----------------+   |
    |                        |
    |  </body>               |
    |</html>                 |
    +------------------------+
    """

    STATUS = {
        0: '通过',
        1: '失败',
        2: '错误',
    }

    DEFAULT_TITLE = '单元测试报告'
    DEFAULT_DESCRIPTION = ''
    DEFAULT_TESTER = '最棒QA'

    # ------------------------------------------------------------------------
    # HTML Template

    HTML_TMPL = r"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>%(title)s</title>
    <meta name="generator" content="%(generator)s"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet">
    <script src="http://libs.baidu.com/jquery/2.0.0/jquery.min.js"></script>
    <script src="http://libs.baidu.com/bootstrap/3.0.3/js/bootstrap.min.js"></script>
    %(stylesheet)s
</head>
<body >
<script language="javascript" type="text/javascript">
output_list = Array();
/*level 调整增加只显示通过用例的分类 --Findyou
0:Summary //all hiddenRow
1:Failed  //pt hiddenRow, ft none
2:Pass    //pt none, ft hiddenRow
3:All     //pt none, ft none
*/
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level == 2 || level == 0 ) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level < 2) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
    }
    //加入【详细】切换文字变化 --Findyou
    detail_class=document.getElementsByClassName('detail');
    //console.log(detail_class.length)
    if (level == 3) {
        for (var i = 0; i < detail_class.length; i++){
            detail_class[i].innerHTML="收起"
        }
    }
    else{
            for (var i = 0; i < detail_class.length; i++){
            detail_class[i].innerHTML="详细"
        }
    }
}
function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        //ID修改 点 为 下划线 -Findyou
        tid0 = 't' + cid.substr(1) + '_' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        //修改点击无法收起的BUG，加入【详细】切换文字变化 --Findyou
        if (toHide) {
            document.getElementById(tid).className = 'hiddenRow';
            document.getElementById(cid).innerText = "详细"
        }
        else {
            document.getElementById(tid).className = '';
            document.getElementById(cid).innerText = "收起"
        }
    }
}
function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
</script>
%(heading)s
%(report)s
%(ending)s
</body>
</html>
"""
    # variables: (title, generator, stylesheet, heading, report, ending)

    # ------------------------------------------------------------------------
    # Stylesheet
    #
    # alternatively use a <link> for external style sheet, e.g.
    #   <link rel="stylesheet" href="$url" type="text/css">

    STYLESHEET_TMPL = """
<style type="text/css" media="screen">
body        { font-family: Microsoft YaHei,Tahoma,arial,helvetica,sans-serif;padding: 20px; font-size: 80%; }
table       { font-size: 100%; }
/* -- heading ---------------------------------------------------------------------- */
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}
.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}
/* -- report ------------------------------------------------------------------------ */
#total_row  { font-weight: bold; }
.passCase   { color: #5cb85c; }
.failCase   { color: #d9534f; font-weight: bold; }
.errorCase  { color: #f0ad4e; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }
</style>
"""

    # ------------------------------------------------------------------------
    # Heading
    #

    HEADING_TMPL = """<div class='heading'>
<h1 style="font-family: Microsoft YaHei">%(title)s</h1>
%(parameters)s
<p class='description'>%(description)s</p>
</div>
"""  # variables: (title, parameters, description)

    HEADING_ATTRIBUTE_TMPL = """<p class='attribute'><strong>%(name)s : </strong> %(value)s</p>
"""  # variables: (name, value)

    # ------------------------------------------------------------------------
    # Report
    #
    # 汉化,加美化效果 --Findyou
    REPORT_TMPL = """
<p id='show_detail_line'>
<a class="btn btn-primary" href='javascript:showCase(0)'>概要{ %(passrate)s }</a>
<a class="btn btn-danger" href='javascript:showCase(1)'>失败{ %(fail)s }</a>
<a class="btn btn-success" href='javascript:showCase(2)'>通过{ %(Pass)s }</a>
<a class="btn btn-info" href='javascript:showCase(3)'>所有{ %(count)s }</a>
</p>
<table id='result_table' class="table table-condensed table-bordered table-hover">
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row' class="text-center success" style="font-weight: bold;font-size: 14px;">
    <td>用例集/测试用例</td>
    <td>总计</td>
    <td>通过</td>
    <td>失败</td>
    <td>错误</td>
    <td>详细</td>
</tr>
%(test_list)s
<tr id='total_row' class="text-center active">
    <td>总计</td>
    <td>%(count)s</td>
    <td>%(Pass)s</td>
    <td>%(fail)s</td>
    <td>%(error)s</td>
    <td>通过率：%(passrate)s</td>
</tr>
</table>
"""  # variables: (test_list, count, Pass, fail, error ,passrate)

    REPORT_CLASS_TMPL = r"""
<tr class='%(style)s warning'>
    <td>%(desc)s</td>
    <td class="text-center">%(count)s</td>
    <td class="text-center">%(Pass)s</td>
    <td class="text-center">%(fail)s</td>
    <td class="text-center">%(error)s</td>
    <td class="text-center"><a href="javascript:showClassDetail('%(cid)s',%(count)s)" class="detail" id='%(cid)s'>详细</a></td>
</tr>
"""  # variables: (style, desc, count, Pass, fail, error, cid)

    # 失败 的样式，去掉原来JS效果，美化展示效果  -Findyou
    REPORT_TEST_WITH_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'>
    <!--默认收起错误信息 -Findyou
    <button id='btn_%(tid)s' type="button"  class="btn btn-danger btn-xs collapsed" data-toggle="collapse" data-target='#div_%(tid)s'>%(status)s</button>
    <div id='div_%(tid)s' class="collapse">  -->
    <!-- 默认展开错误信息 -Findyou -->
    <button id='btn_%(tid)s' type="button"  class="btn btn-danger btn-xs" data-toggle="collapse" data-target='#div_%(tid)s'>%(status)s</button>
    <div id='div_%(tid)s' class="collapse in">
    <pre>
    %(script)s
    </pre>
    </div>
    </td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    # 通过 的样式，加标签效果  -Findyou
    REPORT_TEST_NO_OUTPUT_TMPL = r"""
<tr id='%(tid)s' class='%(Class)s'>
    <td class='%(style)s'><div class='testcase'>%(desc)s</div></td>
    <td colspan='5' align='center'><span class="label label-success success">%(status)s</span></td>
</tr>
"""  # variables: (tid, Class, style, desc, status)

    REPORT_TEST_OUTPUT_TMPL = r"""
%(id)s: %(output)s
"""  # variables: (id, output)

    # ------------------------------------------------------------------------
    # ENDING
    #
    # 增加返回顶部按钮  --Findyou
    ENDING_TMPL = """<div id='ending'>&nbsp;</div>
    <div style=" position:fixed;right:50px; bottom:30px; width:20px; height:20px;cursor:pointer">
    <a href="#"><span class="glyphicon glyphicon-eject" style = "font-size:30px;" aria-hidden="true">
    </span></a></div>
    """


# -------------------- The end of the Template class -------------------


TestResult = unittest.TestResult


class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []
        # 增加一个测试通过率 --Findyou
        self.passrate = float(0)

    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = io.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()

    def addSuccess(self, test):
        self.success_count += 1
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('../../../../../Desktop')

    def addError(self, test, err):
        self.error_count += 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')


class HTMLTestRunner(Template_mixin):
    """
    """

    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None, tester=None):
        self.stream = stream
        self.verbosity = verbosity
        if title is None:
            self.title = self.DEFAULT_TITLE
        else:
            self.title = title
        if description is None:
            self.description = self.DEFAULT_DESCRIPTION
        else:
            self.description = description
        if tester is None:
            self.tester = self.DEFAULT_TESTER
        else:
            self.tester = tester

        self.startTime = datetime.datetime.now()

    def run(self, test):
        "Run the given test case or test suite."
        result = _TestResult(self.verbosity)
        test(result)
        self.stopTime = datetime.datetime.now()
        self.generateReport(test, result)
        print('\nTime Elapsed: %s' % (self.stopTime - self.startTime), file=sys.stderr)
        return result

    def sortResult(self, result_list):
        # unittest does not seems to run in any particular order.
        # Here at least we want to group them together by class.
        rmap = {}
        classes = []
        for n, t, o, e in result_list:
            cls = t.__class__
            if cls not in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, o, e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    # 替换测试结果status为通过率 --Findyou
    def getReportAttributes(self, result):
        """
        Return report attributes as a list of (name, value).
        Override this to add custom attributes.
        """
        startTime = str(self.startTime)[:19]
        duration = str(self.stopTime - self.startTime)
        status = []
        status.append('共 %s' % (result.success_count + result.failure_count + result.error_count))
        if result.success_count: status.append('通过 %s' % result.success_count)
        if result.failure_count: status.append('失败 %s' % result.failure_count)
        if result.error_count:   status.append('错误 %s' % result.error_count)
        if status:
            status = '，'.join(status)
            self.passrate = str("%.2f%%" % (float(result.success_count) / float(
                result.success_count + result.failure_count + result.error_count) * 100))
        else:
            status = 'none'
        return [
            ('测试人员', self.tester),
            ('开始时间', startTime),
            ('合计耗时', duration),
            ('测试结果', status + "，通过率= " + self.passrate),
        ]

    def generateReport(self, test, result):
        report_attrs = self.getReportAttributes(result)
        generator = 'HTMLTestRunner %s' % __version__
        stylesheet = self._generate_stylesheet()
        heading = self._generate_heading(report_attrs)
        report = self._generate_report(result)
        ending = self._generate_ending()
        output = self.HTML_TMPL % dict(
            title=saxutils.escape(self.title),
            generator=generator,
            stylesheet=stylesheet,
            heading=heading,
            report=report,
            ending=ending,
        )
        self.stream.write(output.encode('utf8'))

    def _generate_stylesheet(self):
        return self.STYLESHEET_TMPL

    # 增加Tester显示 -Findyou
    def _generate_heading(self, report_attrs):
        a_lines = []
        for name, value in report_attrs:
            line = self.HEADING_ATTRIBUTE_TMPL % dict(
                name=saxutils.escape(name),
                value=saxutils.escape(value),
            )
            a_lines.append(line)
        heading = self.HEADING_TMPL % dict(
            title=saxutils.escape(self.title),
            parameters=''.join(a_lines),
            description=saxutils.escape(self.description),
            tester=saxutils.escape(self.tester),
        )
        return heading

    # 生成报告  --Findyou添加注释
    def _generate_report(self, result):
        rows = []
        sortedResult = self.sortResult(result.result)
        for cid, (cls, cls_results) in enumerate(sortedResult):
            # subtotal for a class
            np = nf = ne = 0
            for n, t, o, e in cls_results:
                if n == 0:
                    np += 1
                elif n == 1:
                    nf += 1
                else:
                    ne += 1

            # format class description
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s: %s' % (name, doc) or name

            row = self.REPORT_CLASS_TMPL % dict(
                style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
                desc=desc,
                count=np + nf + ne,
                Pass=np,
                fail=nf,
                error=ne,
                cid='c%s' % (cid + 1),
            )
            rows.append(row)

            for tid, (n, t, o, e) in enumerate(cls_results):
                self._generate_report_test(rows, cid, tid, n, t, o, e)

        report = self.REPORT_TMPL % dict(
            test_list=''.join(rows),
            count=str(result.success_count + result.failure_count + result.error_count),
            Pass=str(result.success_count),
            fail=str(result.failure_count),
            error=str(result.error_count),
            passrate=self.passrate,
        )
        return report

    def _generate_report_test(self, rows, cid, tid, n, t, o, e):
        # e.g. 'pt1.1', 'ft1.1', etc
        has_output = bool(o or e)
        # ID修改点为下划线,支持Bootstrap折叠展开特效 - Findyou
        tid = (n == 0 and 'p' or 'f') + 't%s_%s' % (cid + 1, tid + 1)
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""
        desc = doc and ('%s: %s' % (name, doc)) or name
        tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL

        # utf-8 支持中文 - Findyou
        # o and e should be byte string because they are collected from stdout and stderr?
        if isinstance(o, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # uo = unicode(o.encode('string_escape'))
            # uo = o.decode('latin-1')
            uo = o
        else:
            uo = o
        if isinstance(e, str):
            # TODO: some problem with 'string_escape': it escape \n and mess up formating
            # ue = unicode(e.encode('string_escape'))
            # ue = e.decode('latin-1')
            ue = e
        else:
            ue = e

        script = self.REPORT_TEST_OUTPUT_TMPL % dict(
            id=tid,
            output=saxutils.escape(uo + ue),
        )

        row = tmpl % dict(
            tid=tid,
            Class=(n == 0 and 'hiddenRow' or 'none'),
            style=n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'passCase'),
            desc=desc,
            script=script,
            status=self.STATUS[n],
        )
        rows.append(row)
        if not has_output:
            return

    def _generate_ending(self):
        return self.ENDING_TMPL


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)
```

