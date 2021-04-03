from config import WeLogin, SendMail, wakeDyno
import schedule
import time
import sys

def job():
  WeLogin()
  SendMail()

scheduler1 = schedule.Scheduler()
scheduler2 = schedule.Scheduler()

scheduler1.every(28).minutes.do(wakeDyno)
#scheduler2.every(2).days.at("04:20").do(job) # that will send the email every 2 days @ 6:20 AM Cairo time.
scheduler2.every(2).days.at("04:20").do(job)

while True:
  try:
    scheduler1.run_pending()
    scheduler2.run_pending()
  except:
    time.sleep(5)
    scheduler1.run_pending()
    time.sleep(5)
    scheduler2.run_pending()
  time.sleep(1)

  
 
  

