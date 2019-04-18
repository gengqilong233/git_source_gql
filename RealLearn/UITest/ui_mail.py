from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get('https://mail.qq.com')

print('Befor login =================================================')
befor_title = driver.title
befor_url = driver.current_url
print('当前title:',befor_title)
print('当前url：%s' %befor_url)

sleep(1)
# driver.maximize_window()
driver.maximize_window()
AP_btn = driver.find_element_by_xpath('/html/body/div/div[1]/div/a[1]').click()
account = driver.find_element_by_id('u').send_keys('965456595')
password = driver.find_element_by_id('p').send_keys('babaleile1')
login_btn = driver.find_element_by_id('go').click()

sleep(1)
user = driver.find_elements_by_xpath('//*[@id="ct"]/div/div[3]/div[1]/div[1]').te
print('After login =================================================')
after_url = driver.current_url
after_title = driver.title
print('当前title:',after_title)
print('当前url：%s' %after_url)
print('用户：', user)
if after_title == 'QQ邮箱':
    print('通过')
else:
    print('失败')

