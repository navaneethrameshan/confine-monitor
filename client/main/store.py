
from client.nodeinfo.sliverinfo import sliverinfo
from client.nodeinfo.sysinfo import nodeinfo
from filelock import FileLock
import config
import time
import shelve


def monitorStore():
    """
    Get monitored information
    Attach the sequence number
    Attach timestamp
    Store in the log file
    """
   # commented to use psutil system info system_info = systeminfo.get_all_info()

    system_info = nodeinfo.node_all()
    system_info ['monitored_timestamp'] = config.get_current_system_timestamp()

    # Attach sliver info to system info
    system_info.update(sliverinfo.collectAllData())

    config.update_current_seq_number()

    s = shelve.open('log_shelf.db', writeback = True)
    try:
        print("writing to file" + str(config.get_current_seq_number()))
        s['current_seq_number']= config.get_current_seq_number()

        print("writing to file" + str(system_info))
        s[str(config.get_current_seq_number())]= system_info

    finally:
        while(1):
            try:
                s.close()
                break
            except OSError:
                print("Exception caught while closing file!! OS Error: file not found. Trying again in 1 second")
                time.sleep(1)
                continue

