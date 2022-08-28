import time

from selenium import webdriver

driver = webdriver.Chrome('D:\QATesting\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://practice.automationtesting.in')

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
book = driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3')
book.click()

btn = driver.find_element_by_class_name('reviews_tab')
btn.click()

star = driver.find_element_by_class_name('star-5')
star.click()
comment = driver.find_element_by_id('comment')
comment.send_keys('Nice book!')
name = driver.find_element_by_id('author')
name.send_keys('David')
mail = driver.find_element_by_id('email')
mail.send_keys('David@gmail.com')
submit = driver.find_element_by_class_name('submit')
submit.click()

driver.quit()