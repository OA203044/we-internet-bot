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

time.sleep(5)
driver.find_element_by_id('MobileNumberID').send_keys('0238728551')
time.sleep(1)
driver.find_element_by_id ('PasswordID').send_keys('mni0AMHK')
time.sleep(1)
driver.find_element_by_id('singInBtn').click()
time.sleep(5)

print(driver.title)
# login successful
time.sleep(3)

find_elements_by_class_name('block prepaid')
button = driver.find_element_by_link_text("عرض التفاصيل")
button.click()
time.sleep(3)
print(driver.title)






driver.quit();
