from apscheduler.schedulers.blocking import BlockingScheduler
import fredmeyer

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=1)

def run():
    print("execute")
    fredmeyer.runCheck()
    
sched.start()