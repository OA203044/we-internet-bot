import selenium
import time
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Now you can start using Selenium

driver.get ('https://my.te.eg/#/home/signin')
print(driver.title)

time.sleep(3)
driver.find_element_by_id('MobileNumberID').send_keys('0238728551')
time.sleep(1)
driver.find_element_by_id ('PasswordID').send_keys('mni0AMHK')
time.sleep(1)
driver.find_element_by_id('singInBtn').click()
time.sleep(3)

print(driver.title)
# login successful
time.sleep(3)

#driver.find_element_by_class_name('block.prepaid')
driver.find_element_by_css_selector('button.btn.btn-primary').click()
time.sleep(3)
print(driver.title)

#driver.find_element_by_xpath("//*[text()='يوم']"))
print(driver.find_element_by_css_selector('div.col-sm-6'))






driver.quit()
