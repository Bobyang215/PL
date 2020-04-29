from selenium import webdriver

brower = webdriver.Chrome()
brower.get('https://www.baidu.com')

# a = brower.switch_to.alert()
# print(brower)
#
# print(a.text)
# brower.find_element_by_id('User.ID').send_keys('support')
# brower.find_element_by_id('Password').send_keys('Masonsoft2001')
# brower.find_element_by_id('login_buttonn').click()
brower.implicitly_wait(10)
brower.find_element_by_class_name('lb').click()


# brower.find_element_by_name('wd').send_keys('最新小说排行榜')
# brower.find_element_by_id('su').click()
# brower.implicitly_wait(10)
#
# brower.find_element_by_name('wd').send_keys('最新疫情')
# brower.find_element_by_id('su').click()


# brower.find_element_by_name('usr_password').send_keys('123456')
# brower.find_element_by_id('login_button').click()