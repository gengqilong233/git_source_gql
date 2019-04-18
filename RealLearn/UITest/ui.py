from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.maximize_window()

bai_text = driver.find_element_by_class_name('s_ipt')
js = "arguments[0].style.border='6px solid red'" # 通过这两段代码可以时间定为元素出标红
driver.execute_script(js, bai_text)
dirpath = os.path.dirname(os.path.dirname(__file__))
screenShot = dirpath + r'/UITest/ScreenShot/baiduTest.png' # 图片文件路径名称
driver.get_screenshot_as_file(screenShot)

# 实现的方式很简单，就是定位到元素后，执行js样式
driver.execute_script(js, bai_text)

# bai_text.send_keys('selenium') # 输入信息
# bai_text.send_keys(Keys.BACK_SPACE) # 删除最后一个
# bai_text.send_keys(Keys.SPACE) # 输入空格
# bai_text.send_keys('百度') # 继续输入仍然使用send_keys()
# bai_text.send_keys(Keys.CONTROL, 'a') # 【全选】输入框中内容
# sleep(2)
# bai_text.send_keys(Keys.CONTROL, 'x') # 【剪切】选择内容
# sleep(2)
# bai_text.send_keys(Keys.CONTROL, 'v') # 【粘贴】选择内容
# bai_text.send_keys(Keys.CONTROL, 'c') # 【复制】选择内容
# bai_text.send_keys(Keys.ENTER) # 【提交】回车键


# text =driver.find_element_by_id('cp').text
# print('百度页面底部信息：%s' %text) # 获取文本
#
# above = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
# ActionChains(driver).move_to_element(above).perform() # 鼠标悬停
# sleep(2)
#
# driver.find_element_by_class_name('s_ipt').send_keys('百度') # 输入信息
# size = driver.find_element_by_class_name('s_ipt').size # 获取尺寸
# print('输入框尺寸：%s' %size)
#
# driver.find_element_by_id('su').click() # 点击
# xianshi = driver.find_element_by_id('su').is_displayed() # 获取是否可见
# print('是否可见：%s' %xianshi)
#
# driver.find_element_by_class_name('s_ipt').clear() # 清空输入框
# sleep(1)
#
# driver.find_element_by_class_name('s_ipt').submit() # 模拟回车键提交
# sleep(1)
#
# driver.set_window_size(400, 400) # 设置浏览器大小
# sleep(1)
#
# driver.maximize_window() # 设置浏览器全屏
#
# driver.back() # 后退
#
# driver.forward() # 前进
#
# driver.refresh() # 刷新
#
# sleep(1)
# driver.quit()

# 多窗口切换============================================================================================================

# baidu_handle = driver.current_window_handle # 获得当前页面句柄（百度首页）
# print('百度首页句柄：%s' %baidu_handle)
#
# driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click() # 点击登录
# sleep(1)
# driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[4]/a').click() # 点击注册
# driver.close() # 关闭句柄窗口
#
# # 坑  事实证明，新开窗口后，获取当前页句柄，仍是百度首页的，可以执行下边代码试试
# # zhuce_handle = driver.current_window_handle # 获得当前页面句柄（注册页）
# # print('注册页句柄：%s' %zhuce_handle)
# # driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').send_keys('测试用户名') # 在注册页输入用户名
#
# all_handle = driver.window_handles # 获得当前浏览器所有页面句柄返回list
# print('当前浏览器所有句柄：%s' %all_handle)
#
# # 通过for判断是不是百度首页句柄，不是的话当做注册页句柄进行操作
# for handle in all_handle: # 疑问：如果浏览器有两个以上的窗口怎么区分？
#     if handle != baidu_handle:
#         print('1111')
#         driver.switch_to.window(handle)
#         driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').send_keys('测试用户名')
#     else:
#         print(22222)
#         driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__closeBtn"]').click() # 点击关闭登录浮层
#         driver.find_element_by_class_name('s_ipt').send_keys('这个是首页')

# 警告框处理 ===========================================================================================================
# set = driver.find_element_by_xpath('//*[@id="u1"]/a[8]') # 设置
# ActionChains(driver).move_to_element(set).perform() # 鼠标悬停设置
# driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click() # 点击设置
# sleep(2)
# driver.find_element_by_class_name("prefpanelgo").click() # 点击保存
#
# a = driver.switch_to_alert().text # 提取生成alert，confirm，prompt内容
# print(a)
# # driver.switch_to_alert().dismiss() # 拒绝、关闭警告窗
# driver.switch_to_alert().accept() # 同意、接受警告窗

# ---------------------------------------------------------------------------------------------------------------------------
# 【截图】
# import os
# dirpath = os.path.dirname(os.path.dirname(__file__))
# screenShot = dirpath + r'/UITest/ScreenShot/baiduTest.png' # 图片文件路径名称
# print(screenShot)
# driver.get_screenshot_as_file(screenShot) # get_screenshot_as_file()方法接受图片路径即可保存

# ---------------------------------------------------------------------------------------------------------------------------
# 【调用JavaScript】
#     1【鼠标滚动】
# a = driver.find_element_by_class_name('s_ipt')
# a.send_keys('时间戳')
# a.submit()
# sleep(2)
# js = 'window.scrollTo(0,1000);' # 使用js的方式改变滚动条位置
# driver.execute_script(js) # 通过execute_scrip()来这行js函数
# print(1)

#   2【处理H5视频播放】
# driver.get('https://www.hfjy.com/')
# sleep(1)
# video = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]') # 页面元素定位
# url = driver.execute_script('return arguments[0].currentSrc;', video) # 返回播放url
# start = driver.execute_script('return arguments[0].play()', video) # 播放
# sleep(10) # 停10秒让它播放10秒
# stop = driver.execute_script('arguments[0].pause()') # 暂停

# ---------------------------------------------------------------------------------------------------------------------------
# 【调试debug】
#     【baseConfig()】只能捕捉客户端发送的POST请求，无法捕捉GET请求
# import logging
# logging.basicConfig(level=logging.DEBUG) # 用法
# bai_text = driver.find_element_by_class_name('s_ipt')
# bai_text.send_keys('selenium') # 输入信息
# bai_text.submit()

# ---------------------------------------------------------------------------------------------------------------------------
# 【输出HTML报告】
import HTMLTestRunner
import unittest
import time
import os
class Baidu(unittest.TestCase):
    '''百度搜索测试'''

    def setUp(self):  # unittest执行前的操作
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = 'http://www.baidu.com/'

    def test_baidu(self):
        '''搜索关键字'''
        driver = self.driver
        driver.get(self.url)
        bai_text = driver.find_element_by_class_name('s_ipt')
        bai_text.send_keys('selenium') # 输入信息
        bai_text.submit()

    def tearDown(self): # unittest执行后的操作
        self.driver.quit()

if __name__ == '__main__':
    # a = unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu"))

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    dirpath = r'D:\pycharm\PythonImport\RealLearn\UITest\logTest'

    fp = open(dirpath +'/'+ now +' result.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = '百度搜索报告', description='用例执行情况')
    runner.run(testunit)
    fp.close()

# ---------------------------------------------------------------------------------------------------------------------------



















# ======================================================================================================================
# 百度云盘登录
# driver.get('https://pan.baidu.com/')
# sleep(1)
# driver.maximize_window()
#
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__footerULoginBtn"]').click() # 点击账号密码登录
#
# driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys('13592660464') # 输入账号
# driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('123qweasd') # 输入密码
# driver.find_element_by_id('TANGRAM__PSP_4__password').submit() # 点击提交，相当于回车
# sleep(5)
#
# driver.find_element_by_xpath('//*[@id="TANGRAM__37__button_send_mobile"]').click() # 点击发送手机验证码
#
# s = input('输入验证码：')
# yanzhengma = driver.find_element_by_id('TANGRAM__37__input_label_vcode') # 验证码输入框
# yanzhengma.send_keys(s) # 输入验证码
# yanzhengma.submit() # 提交
# sleep(2)
#
# driver.find_element_by_xpath('//*[@id="dialog1"]/div[2]/div/div[2]/span').click() # 点击知道了
#
# right_click = driver.find_element_by_id('i07610616095743168')
# ActionChains(driver).context_click(right_click).perform()


# driver.quit()



