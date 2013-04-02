#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from client.nodeinfo.sliverinfo.lxc.cgroup import cgroup
from client.nodeinfo.sliverinfo import lxc
import sys

def getRunningContainers():
    lxcdir=os.listdir(lxc.basepath)
    ret = []
    for entry in lxcdir:
        if os.path.isdir(os.path.join(lxc.basepath, entry)):
            ret.append(entry)
    return ret

def byte2MiByte(val):
    return val/1024/1024

def container_mem_usage(name):
    inst = cgroup(name)

    memlimit = int(inst.getValue("memory.limit_in_bytes"))
    memswlimit = int(inst.getValue("memory.memsw.limit_in_bytes"))
    memused = int(inst.getValue("memory.usage_in_bytes"))
    memswused = int(inst.getValue("memory.memsw.usage_in_bytes"))

    mem_total = memlimit
    mem_used = memused
    mem_free = memlimit-memused
    if (memlimit!=0):
        mem_percent_used = memused/float(memlimit)*100
    else:
        mem_percent_used = None

    swap_total = memswlimit-memlimit
    swap_used = memswused-memused
    swap_free = swap_total -swap_used
    if(swap_total!=0):
        swap_percent_used = swap_used/float(swap_total)*100
    else:
        swap_percent_used = None

    total = memswlimit
    total_used = memswused
    total_free = memswlimit-memswused

    if(memswlimit!=0):
        total_percent_used = memswused/float(memswlimit)*100
    else:
        total_percent_used= None



    #print "         %12s	%12s	%12s	%12s" % ("total","used","free", "percent used")
    #print "Mem  :	%12i	%12i	%12i	%12i" % (byte2MiByte(memlimit),byte2MiByte(memused),byte2MiByte(memlimit-memused), memused/float(memlimit)*100)
    #print "Swap :	%12i	%12i	%12i	%12i" % (byte2MiByte(memswlimit-memlimit),byte2MiByte(memswused-memused),byte2MiByte(memswlimit-memlimit-(memswused-memused)), (memswused-memused)/float(memswlimit-memlimit)*100)
    #print "Total:	%12i	%12i	%12i	%12i" % (byte2MiByte(memswlimit),byte2MiByte(memswused),byte2MiByte(memswlimit-memswused), memswused/float(memswlimit)*100)

    return {'memory':{'mem_total': mem_total, 'mem_used': mem_used, 'mem_free': mem_free, 'mem_percent_used': mem_percent_used,
                      'swap_total':swap_total, 'swap_used': swap_used, 'swap_free': swap_free, 'swap_percent_used': swap_percent_used,
                      'total': total, 'total_used': total_used, 'total_free': total_free, 'total_percent_used': total_percent_used}}


def container_cpu_usage(name):
    inst = cgroup(name)
    cpu_usage = inst.getValue("cpuacct.usage")
    return {'cpu':{'cpu_usage': cpu_usage}}


def get_name(container):
    slice_name = ''
    sliver_name = ''

    if (os.path.exists('/lxc/images/%s/config' % (container,))):
        with open('/lxc/images/%s/config' % (container,), 'r') as f:
            line = f.readline()
            if line.startswith('lxc.utsname'):
                line.rstrip('\n')
                info = line.split('=')
                sliver_name = info[-1]
                (slice_name,node_name) = info[-1].split('_')


    return {'sliver_name': sliver_name, 'slice_name': slice_name}
