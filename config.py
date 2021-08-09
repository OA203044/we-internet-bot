# add these Heroku (Config Vars)
'''
CHROMEDRIVER_PATH --> /app/.chromedriver/bin/chromedriver
GOOGLE_CHROME_BIN --> /app/.apt/usr/bin/google-chrome
heroku_var_sndrEmail --> # use different emails for sender and reciver to avoid ur mails getting into spam folder
heroku_var_2FApass -->   # you need to trun on 2FA on the sender email, and then get an app password (google that if u don't know what i'm talking about)
heroku_var_rcvrEmail --> 
heroku_var_WENum --> # land line number with province code with no spaces
heroku_var_WEpass -->
'''

# add these Heroku (Buildpacks)
'''
heroku/python
https://github.com/heroku/heroku-buildpack-google-chrome
https://github.com/heroku/heroku-buildpack-chromedriver
'''


############### Code starts here ###############
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime, timedelta
import os
import smtplib

global acounter
acounter=0


# Selenium stuff (optimized for heroku)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


############### Functions ###############

def WeLogin():
  global rate
  global days
  global date_formatted
  global GB
  
  driver.get ('https://my.te.eg/user/login')
  time.sleep(5)
  print(driver.title)
  driver.find_element_by_class_name('p-inputmask').send_keys(os.environ.get("heroku_var_WENum"))
  time.sleep(1)
  driver.find_element_by_id ('password').send_keys(os.environ.get("heroku_var_WEpass"))
  time.sleep(1)
  arr=driver.find_elements_by_css_selector('span.p-button-label')
  arr[1].click()
  time.sleep(3)


  # login successful
  print(driver.title)
  # getting remainning GB
  ff = driver.find_element_by_class_name('usage-details').text
  usedGB = float(ff[:len(ff)-5]) #extract the number from text
  GB = 140 - usedGB
  time.sleep(1)

  #اضغط ع تفاصيل الاستهلاك
  driver.get('https://my.te.eg/offering/overview')  time.sleep(2)
  print(driver.title)

  # تاريخ الشحن ك نص
  driver.get('https://my.te.eg/offering/overview')
  time.sleep(2)
  tt = driver.find_element_by_class_name('mr-auto').text
  date_text = tt[14:24]
  
  # تحويل النص لتاريخ
  date_formatted = datetime.strptime(date_text,"%Y-%m-%d")
  #get current date and time
  now = datetime.now()
  difference = now-date_formatted
  #الايام المتبقية
  days=30-difference.days
  # معدل الاستهلاك ... المعدل الطبيعي 140/30 = 4.66 جيجا في اليوم
  rate = GB/days
  #print("%.2f" % rate)
  time.sleep(3)
  driver.quit()
    
##############################
  
def SendMail():  
  global rate
  global days
  global date_formatted
  global GB
  global acounter
  acounter=0

  server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
  # you need to trun on 2FA on the sender email, and then get an app password (goole that if u don't know ehat i'm taking about)
  server.login(os.environ.get("heroku_var_sndrEmail"), os.environ.get("heroku_var_2FApass"))
  rate = str(round(rate, 2))
  print(rate)
  date = date_formatted + timedelta(30)
  date = date.strftime("%d/%m/%Y")
  rate_str = '#Rate: ' + str(rate) + ' GB'
  days_str = '#Remaining: ' +str(GB)+ ' GB & '+ str(days) + ' days'
  date_str = '#You have to recharge before: ' + str(date)

  subject = 'WE Internet Consumption'
  body = rate_str + '\n\n' + days_str + '\n\n' + date_str
  msg = f'Subject: {subject}\n\n{body}'

  server.sendmail(os.environ.get("heroku_var_sndrEmail"), os.environ.get("heroku_var_rcvrEmail"), msg)

  print('\n### Email was sent successfully! ###')
  server.quit()
  
##############################

# if dyno receives no web traffic in a 30-minute period, it will sleep! so we will run this func. every 29 min or so
def wakeDyno(): 
  global acounter
  acounter+=1
  
  driver.get ('https://docs.python.org/3')
  print('didn\'t sleep yet!')
  print('# about '+str(round(acounter*28/60,2))+ ' hours has passed!')
    
##############################

  


