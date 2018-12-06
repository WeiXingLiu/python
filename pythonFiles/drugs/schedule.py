
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
from find import beginFetchDetail
from helper import deleteTableData
def job():
    # deleteTableData()
    beginFetchDetail('')

if __name__ == '__main__':
    schedulers = BackgroundScheduler()

    schedulers.add_job(job, 'cron', hour=8, minute=59, second=25)
    # schedulers.add_job(job, 'interval', minutes=3)
    # schedulers.add_job(job, 'date', run_date='2018-10-08 17:42:00')

    schedulers.start()

    while True:
        time.sleep(10)