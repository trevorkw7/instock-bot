from apscheduler.schedulers.blocking import BlockingScheduler
import fredmeyer

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=5)

def run():
    print("execute")
    fredmeyer.runCheck()
    
sched.start()