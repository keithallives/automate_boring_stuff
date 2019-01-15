from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://github.com/login')
username_elem = browser.find_element_by_id('login_field')
username_elem.send_keys('keithallives')
password_elem = browser.find_element_by_id('password')
password_elem.send_keys('123456')
password_elem.submit()