
from client.nodeinfo.sysinfo import systeminfo
from client.nodeinfo.sysinfo import nodeinfo
from client.nodeinfo.datagenerator import datagenerator
from filelock import FileLock
import config
import string
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
 #TODO: Uncomment later   system_info.update(sliverinfo.collectAllData())

# TODO: Remove this later---for now attach fake data
    system_info.update(datagenerator.collectAllData_fake())


    config.update_current_seq_number()

    s = shelve.open('log_shelf.db', writeback = True)
    try:
        print("writing to file" + str(system_info))
        s[str(config.get_current_seq_number())]= system_info
    finally:
        s.close()

#   # system_info.update({"timestamp":config.get_current_system_timestamp()})
#    log = file("monitor-log", 'aw')
#    with FileLock("monitor-log") as lock:
#        print("Lock Acquired")
#        print("writing to file")
#        str_system_info = str(system_info)
#        string.strip(system_info,"\n")
#        print repr(str(system_info) + '\n')
#        log.writelines(str(system_info) + '\n')
#        print("Lock Released")
#    log.close()
