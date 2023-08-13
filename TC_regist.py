from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import string
import random
import time

#sloving chrome closes immediately and automatically
chr_opt = webdriver.ChromeOptions()
chr_opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(chr_opt)
driver.implicitly_wait(5)

url = 'http://demostore.supersqa.com/my-account/'
email_field_id = 'reg_email'
psswd_field_id = 'reg_password'

# go to url
driver.get(url)
driver.maximize_window()
email_field = driver.find_element(By.ID, email_field_id)

#generate random Email
letters = string.ascii_lowercase
random_sting = ''.join(random.choice(letters) for i in range(15))
random_email = random_sting + "@supersqa.com"

# type in the email field
email_field.send_keys(random_email)

#find password field and enter password
password_filed = driver.find_element(By.ID, psswd_field_id)
password_filed.send_keys('password!12365')

time.sleep(2)
register_btn = driver.find_element(By.CSS_SELECTOR, 'button[value=Register]')
register_btn.click()

logout_btn = driver.find_element(By.XPATH, '//*[@id="post-9"]/div/div/nav/ul/li[6]/a')

if logout_btn.is_displayed() :
    print('Pass.')
else:
    raise Exception('user not logged in after registering')

#another way
try:
    logout_btn = driver.find_element(By.XPATH, '//*[@id="post-9"]/div/div/nav/ul/li[6]/a')
except:
    raise Exception('user not logged in after registering')