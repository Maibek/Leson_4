import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
a = 'David@gmail.com'
b = 'IxgPgWv9~q'
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
driver.get('https://practice.automationtesting.in')

time.sleep(1)
account = driver.find_element_by_link_text('My Account')
account.click()
mail = driver.find_element_by_id('reg_email')
mail.send_keys(a)
password = driver.find_element_by_id('reg_password')
password.send_keys(b)
reg = driver.find_element_by_name('register')
reg.click()

driver.get('https://practice.automationtesting.in')
time.sleep(1)

account = driver.find_element_by_link_text('My Account')
account.click()
user_name = driver.find_element_by_id('username')
user_name.send_keys(a)
password = driver.find_element_by_id('password')
password.send_keys(b)
log = driver.find_element_by_name('login')
log.click()

check_text = driver.find_element_by_link_text('Logout')

driver.quit()