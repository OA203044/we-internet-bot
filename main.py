import selenium
from selenium import webdriver
import time
from datetime import datetime
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


# login successful
print(driver.title)

# getting remainning GB
array=driver.find_elements_by_css_selector('tspan')
GB=float(array[3].text)
time.sleep(3)

#اضغط ع تفاصيل الاستهلاك
driver.find_element_by_css_selector('button.btn.btn-primary').click()
time.sleep(3)
print(driver.title)



#get_attribute("value")
# تاريخ الشحن ك نص
date_text= driver.find_element_by_css_selector('div.col-sm-6').text
# تحويل النص لتاريخ
date_formatted = datetime.strptime(date_text,"%Y-%m-%d")
#get current date and time
now = datetime.now()
difference = now-date_formatted
#الايام المتبقية
days=30-difference.days
# معدل الاستهلاك ... المعدل الطبيعي 250/30 = 8.33 جيجا في اليوم
rate=GB/days
print("%.2f" % rate)
driver.get ('https://github.com')

time.sleep(2)

driver.quit()
