
from client.nodeinfo.sliverinfo import sliverinfo
from client.nodeinfo.sysinfo import nodeinfo
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

    while(1):
        try:
            try:
                print("writing to file" + str(config.get_current_seq_number()))
                s['current_seq_number']= config.get_current_seq_number()

                print("writing to file" + str(system_info))
                s[str(config.get_current_seq_number())]= system_info
            finally:
                s.close()
                break

        except OSError:
            # In some research devices, the underlying dbm has a bug which needs to be handled explicitly
            print("Exception caught while handling shelve file!! OS Error: file not found. Trying again in 1 second")
            time.sleep(1)
            continue


