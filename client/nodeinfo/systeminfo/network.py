import psutil
from psutil._compat import print_

def to_meg(n):
    return str(int(n / 1024 / 1024)) + "M"

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i+1)*10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n



def network_all():
    network= {}
    value = psutil.network_io_counters(pernic=True)

    for interface in value.keys():
        network[interface] = {'bytes_sent': value[interface].bytes_sent,
                              'bytes_recv': value[interface].bytes_recv}

    network['total'] = {'bytes_sent': psutil.network_io_counters().bytes_sent,
                        'bytes_recv': psutil.network_io_counters().bytes_recv}

    return network

def main():
    print_('Network Information\n------')
    #bytes_sent= psutil.network_io_counters().bytes_sent
    #print (bytes2human(bytes_sent))

    print psutil.network_io_counters(pernic=True)

if __name__ == '__main__':
   main()