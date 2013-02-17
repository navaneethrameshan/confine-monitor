import shelve

import time

TIMEPERIOD = 5
RECEIVEDTIMESTAMP=[]
TIMEMAP_SERVER_CLIENT = {}
CURRENT_SEQ_NUMBER =0
LAST_SEEN_SEQ_NUMBER = 0 # useful when we want to delete seen information in the logs

def get_last_timestamp():
    return RECEIVEDTIMESTAMP[-1]


def get_current_system_timestamp():
    timestamp = time.time()
    return timestamp


def update_received_timestamp(server_timestamp):
    """
    update the received timestamp and
    initialize a map entry with the current timestamp of the client
    """
    RECEIVEDTIMESTAMP.append(server_timestamp)
    current_timestamp = get_current_system_timestamp()
    TIMEMAP_SERVER_CLIENT.update({server_timestamp:current_timestamp})


def time_elapsed_since_last_timestamp():
    """
    get relative time elapsed since the last timestamp
    """
    last_server_timestamp = get_last_timestamp()
    corresponding_client_timestamp = TIMEMAP_SERVER_CLIENT[last_server_timestamp]
    time_elapsed = get_current_system_timestamp()-corresponding_client_timestamp
    return time_elapsed


def current_server_timestamp():
    return time_elapsed_since_last_timestamp()+get_last_timestamp()


#TODO: Monitor
def update_current_seq_number():
    global CURRENT_SEQ_NUMBER
    CURRENT_SEQ_NUMBER += 1
    s = shelve.open('log_shelf.db', writeback = True)
    try:
        print("writing to file" + str(CURRENT_SEQ_NUMBER))
        s['current_seq_number']= CURRENT_SEQ_NUMBER
    finally:
        s.close()


def get_current_seq_number():
    global CURRENT_SEQ_NUMBER
    return CURRENT_SEQ_NUMBER

def update_last_seen_seq_number(seqnumber):
    LAST_SEEN_SEQ_NUMBER = seqnumber

def get_last_seen_seq_number():
    return LAST_SEEN_SEQ_NUMBER