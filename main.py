from config import WeLogin, SendMail, wakeDyno
import schedule
import time

def job():
  WeLogin()
  SendMail()

scheduler1 = schedule.Scheduler()
scheduler2 = schedule.Scheduler()

schedule1.every(28).minutes.do(wakeDyno)
schedule2.every(2).days.at("4:25").do(job)

while True:
  schedule1.run_pending()
  schedule2.run_pending()
  time.sleep(1)

  
 
  

