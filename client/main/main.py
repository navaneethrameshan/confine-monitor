from client.main import log

from common.schedule import Schedule
import store
import config

def start_monitoring():
    sched = Schedule(config.TIMEPERIOD)
    sched.schedule(store.monitorStore)

def main():
    start_monitoring()
