from config import WeLogin, SendMail, wakeDyno
import schedule
import time
import sys

def job():
  WeLogin()
  SendMail()

  
scheduler1 = schedule.Scheduler() #wakeDyno
scheduler2 = schedule.Scheduler() # send email
#scheduler3 = schedule.Scheduler()
#scheduler4 = schedule.Scheduler()

scheduler1.every(28).minutes.do(wakeDyno)
#scheduler2.every(2).days.at("04:20").do(job) # that will send the email every 2 days @ 6:20 AM Cairo time.
#scheduler2.every(2).days.at("04:20").do(job)
scheduler2.every().day.at("04:20").do(job) # 6:20 AM Cairo time.
#scheduler3.every().tuesday.at("04:20").do(job)
#scheduler4.every().thursday.at("04:20").do(job)

while True:
  try:
    scheduler1.run_pending()
    scheduler2.run_pending()
    #scheduler3.run_pending()
    #scheduler4.run_pending()
  except:
    time.sleep(5)
    scheduler1.run_pending()
    time.sleep(5)
    scheduler2.run_pending()
    time.sleep(5)
    #scheduler3.run_pending()
    time.sleep(5)
    #scheduler4.run_pending()
  time.sleep(1)

  
 
  

