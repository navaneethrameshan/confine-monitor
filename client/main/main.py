from client.main import log

from common.schedule import Schedule
import store
import config

def start_monitoring():
    sched = Schedule(config.TIMEPERIOD)
    sched.schedule(store.monitorStore)

def main():
    start_monitoring()

def lol():
    log.get_all_info_since(2)
   # log.get_shelve_elements()

if __name__ == "__main__":
   # lol()
    main()