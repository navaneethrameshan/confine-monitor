from client.main import config

import shelve
import os

def get_all_info_since(seqnumber):
    """
    return all the information in the log file since the last seen seq number as a list
    Attach the current client timestamp, and time since the information was monitored (relative_timestamp)
    """
    system_info= {}
    path = os.path.join(os.path.dirname(__file__), '../../log_shelf.db')
    print path

    s= shelve.open(str(path))	
    #s= shelve.open('/home/navaneeth/PycharmProjects/confine_monitor/client/main/log_shelf.db')
    try:
        # TODO: check for possible race condition in get_current_seq_number and delete seen seq numbers
        # Once deleting seq numbers in logs are implemented, then check for sequence number limits.
        for seq in range(seqnumber+1, s['current_seq_number']+1):
            print seq
            if(str(seq) in s):
                value = s[str(seq)]
                # Do not persist current_timestamp and relative_timestamp. They are calculated every time a request is received in order to account for newer calculations in case of network partitions.
                value['relative_timestamp'] = config.get_current_system_timestamp()-value['monitored_timestamp']
                system_info[str(seq)] = value

    finally:
        s.close()

    #print system_info.items()
    return system_info



def get_shelve_elements():
    s= shelve.open('/home/navaneeth/PycharmProjects/confine_monitor/client/main/log_shelf.db')
    print s.keys()
    s.close()

if __name__ == '__main__':
    get_all_info_since(1000) 
