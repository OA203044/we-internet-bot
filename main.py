from config import WeLogin, SendMail, wakeDyno
import schedule
import time


schedule.every(28).minutes.do(wakeDyno)

def job():
  WeLogin()
  SendMail()
  
schedule.every(2).days.at("4:25").do(job)


while True:
  schedule.run_pending()
  time.sleep(1)

  
 
  

