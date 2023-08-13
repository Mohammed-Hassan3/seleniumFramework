from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chr_opt = webdriver.ChromeOptions()
chr_opt.add_experimental_option('detach', True)


driver = webdriver.Chrome(chr_opt)
driver.get('file:///C:/Users/melbe/Desktop/QA-Automation/python_selenium_course_material/provided_code/python_selenium_course_material/SELENIUM_SECTION/Waits/page_with_slow_image.html')
#driver.implicitly_wait(5)
#my_img = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))
wait = WebDriverWait(driver,10)
my_img = wait.until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))

print('found image')