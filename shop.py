import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

a = 'David@gmail.com'
b = 'IxgPgWv9~q'
driver = webdriver.Chrome('D:\QATesting\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
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

shop = driver.find_element_by_id('menu-item-40')
shop.click()
book = driver.find_element_by_css_selector('#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.outofstock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img')
book.click()

book_name = driver.find_element_by_css_selector('#product-181 > div.summary.entry-summary > h1')
book_name_text = book_name.text
assert book_name_text == 'HTML5 Forms'

driver.quit()

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

a = 'David@gmail.com'
b = 'IxgPgWv9~q'
driver = webdriver.Chrome('D:\QATesting\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
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

shop = driver.find_element_by_id('menu-item-40')
shop.click()
html = driver.find_element_by_css_selector('#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a')
html.click()

amount = len(driver.find_elements_by_class_name('woocommerce-LoopProduct-link'))

assert amount == 3

driver.quit()

import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select

a = 'David@gmail.com'
b = 'IxgPgWv9~q'
driver = webdriver.Chrome('D:\QATesting\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
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

shop = driver.find_element_by_id('menu-item-40')
shop.click()

# Проверка сортировки по умолчанию
items_selector = driver.find_element_by_name("orderby")
items_selector_default = items_selector.get_attribute("value")
if items_selector_default == "menu_order":
    print("Выбрана сортировка по умолчанию")
else:
    print("Выбрана сортировка НЕ по умолчанию")
# Сортировка от большего к меньшему и проверка
select = Select(items_selector)
select.select_by_value("price-desc")
items_selector = driver.find_element_by_name("orderby")
items_selector_low = items_selector.get_attribute("value")
if items_selector_low == "price-desc":
    print("Выбрана сортировка по убыванию")
else:
    print("Выбрана сортировка НЕ по убыванию")

driver.quit()



import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

a = 'David@gmail.com'
b = 'IxgPgWv9~q'
driver = webdriver.Chrome('D:\QATesting\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
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

time.sleep(1)
shop = driver.find_element_by_id('menu-item-40')
shop.click()

book = driver.find_element_by_css_selector('#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.outofstock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > img')
book.click()

old_price = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span')
old_price = old_price.text
assert old_price == '₹600.00'
new_price = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span')
new_price = new_price.text
assert new_price == '₹450.00'

img = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-169 > div.images > a > img'))
).click()

img_close = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.pp_pic_holder.pp_woocommerce > div.pp_content_container > div > div > div > div.pp_fade > div.pp_details > a'))
).click()

driver.quit()

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

a = 'David@gmail.com'
b = 'IxgPgWv9~q'
driver = webdriver.Chrome('D:\QATesting\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
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

time.sleep(1)
shop = driver.find_element_by_id('menu-item-40')
shop.click()
book = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
book.click()
time.sleep(1)
quantity_check = driver.find_element_by_class_name('cartcontents')
quantity_check_text = quantity_check.text
assert quantity_check_text == '1 Item'
price_check = driver.find_element_by_class_name('amount')
price_check_text = price_check.text
assert price_check_text == '₹180.00'
quantity_check.click()

price = WebDriverWait(driver, 2).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span'), '₹180.00')
)

total_price = WebDriverWait(driver, 2).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span'), '₹183.60')
)

driver.quit()

import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

a = 'David@gmail.com'
b = 'IxgPgWv9~q'
driver = webdriver.Chrome('D:\QATesting\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
driver.get('https://practice.automationtesting.in')

time.sleep(1)
shop = driver.find_element_by_id('menu-item-40')
shop.click()

driver.execute_script("window.scrollBy(0, 300);")
book_1 = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
book_1.click()
time.sleep(2)
book_2 = driver.find_element_by_css_selector('#content > ul > li.post-180.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
book_2.click()
time.sleep(1)
basket = driver.find_element_by_class_name('wpmenucart-contents')
basket.click()
time.sleep(2)
del_book = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a')
del_book.click()

undo = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div.woocommerce-message > a'))
)
undo.click()

quantity = driver.find_element_by_name('cart[045117b0e0a11a242b9765e79cbf113f][qty]')
quantity.clear()
quantity.send_keys(3)
time.sleep(1)
update = driver.find_element_by_name('update_cart')
update.click()
quantity_check = quantity.get_attribute('value')
assert quantity_check == '3'

time.sleep(1)
apply = driver.find_element_by_name('apply_coupon')
apply.click()

check = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > ul > li'), 'Please enter a coupon code.')
)

driver.quit()


import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

a = 'David@gmail.com'
b = 'IxgPgWv9~q'
driver = webdriver.Chrome('D:\QATesting\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 5)
driver.get('https://practice.automationtesting.in')

time.sleep(1)
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")

book = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
book.click()
time.sleep(1)

basket = driver.find_element_by_class_name('cartcontents')
basket.click()

checkout = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div > div > div > a')))
checkout.click()
first_name = wait.until(
    EC.element_to_be_clickable((By.ID, 'billing_first_name')))
first_name.send_keys('David')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Smith')
email = driver.find_element_by_id('billing_email')
email.send_keys(a)
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('+15144397007')
country = driver.find_element_by_id('s2id_billing_country')
country.click()
country_search = driver.find_element_by_id('s2id_autogen1_search')
country_search.send_keys('Canada')
time.sleep(2)
country_canada = driver.find_element_by_id('select2-result-label-340')
country_canada.click()
time.sleep(1)
address = driver.find_element_by_id('billing_address_1')
address.send_keys('M. Jean - Louis Lemieux 1400 Boul. De Maissoneuve, app-204')
city = driver.find_element_by_id('billing_city')
city.send_keys('Montreal')
province = driver.find_element_by_id('select2-chosen-2')
province.click()
province_search = driver.find_element_by_id('s2id_autogen2_search')
province_search.send_keys('Q')
time.sleep(1)
province_1 = driver.find_element_by_id('select2-result-label-354')
province_1.click()
postcode = driver.find_element_by_id('billing_postcode')
postcode.send_keys('H3T 7N8')

time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")

payment = driver.find_element_by_id('payment_method_cheque')
payment.click()
place_order = driver.find_element_by_id('place_order')
place_order.click()

text_check = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))
playment = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > td'), 'Check Payments'))

driver.quit()