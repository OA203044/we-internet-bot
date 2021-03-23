from config import WeLogin, SendMail, wakeDyno
import schedule
import time

def job():
  WeLogin()
  SendMail()

scheduler1 = schedule.Scheduler()
scheduler2 = schedule.Scheduler()

scheduler1.every(28).minutes.do(wakeDyno)
scheduler2.every().day.at("17:26").do(job)

while True:
  scheduler1.run_pending()
  scheduler2.run_pending()
  time.sleep(1)

  
 
  

