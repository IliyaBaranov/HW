import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
def wait_till_clickable(driver, selector_type, selector_value, time):
    try:
        element = WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((selector_type, selector_value))
        )
    except:
        print('error')
        return None
    else:
        return element

driver.get('https://www.saucedemo.com/')

driver.fullscreen_window()
time.sleep(1)

b1 = driver.find_element('id', 'user-name')
b1.send_keys('standard_user')
b1.send_keys(Keys.ENTER)

b2 = driver.find_element('id', 'password')
b2.send_keys('secret_sauce')
b2.send_keys(Keys.ENTER)
time.sleep(1)
b3 = driver.find_element('id', 'login-button')
b3.send_keys(Keys.ENTER)
time.sleep(1)
b4 = driver.find_element('id', 'add-to-cart-sauce-labs-backpack')
b4.click()
time.sleep(1)
b5 = driver.find_element('id', 'add-to-cart-sauce-labs-bike-light')
b5.click()
time.sleep(1)
b6 = driver.find_element('id', 'add-to-cart-sauce-labs-bolt-t-shirt')
b6.click()
time.sleep(1)
b7 = driver.find_element('id', 'shopping_cart_container')
b7.click()
time.sleep(1)
b8 = driver.find_element('id', 'checkout')
b8.click()
time.sleep(1)
b10 = driver.find_element('id', 'first-name')
b10.send_keys('a')

b11 = driver.find_element('id', 'last-name')
b11.send_keys('a')

b12 = driver.find_element('id', 'postal-code')
b12.send_keys('a')
time.sleep(1)
b13 = driver.find_element('id', 'continue')
b13.send_keys(Keys.ENTER)
time.sleep(1)
action = ActionChains(driver)
for_screen = driver.find_element(By.XPATH, '//*[@id="finish"]')
action.move_to_element(for_screen).perform()
time.sleep(1)
b15 = driver.current_window_handle
driver.switch_to.window(b15)
driver.save_screenshot(f'{b15}.png')
time.sleep(1)
b16 = driver.find_element('id', 'finish')
b16.click()
time.sleep(1)
b17 = driver.find_element('id', 'back-to-products')
b17.click()
time.sleep(1)
b20 = driver.find_element('xpath', '//*[@id="header_container"]/div[2]/div[2]/span/select')
b20.click()
b20.send_keys(Keys.ARROW_DOWN * 2)
b20.click()
time.sleep(1)
b18 = driver.find_element('id', 'react-burger-menu-btn')
b18.click()
time.sleep(1)
action2 = ActionChains(driver)
for_exit = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
action2.move_to_element(for_exit).perform()
time.sleep(1)
b19 = wait_till_clickable(driver, By.XPATH, '//*[@id="logout_sidebar_link"]', 15)
if b19:
    b19.click()
time.sleep(5)
