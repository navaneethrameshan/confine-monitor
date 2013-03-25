import commands
import os
from client.nodeinfo.sysinfo.common import nt_diskstatus, nt_diskpartitions, usage_percent


def get_disk_usage(path):
    """Return disk usage associated with path."""
    st = os.statvfs(path)
    free = st.f_bavail * st.f_frsize
    total = st.f_blocks * st.f_frsize
    used = (st.f_blocks - st.f_bfree) * st.f_frsize
    percent = usage_percent(used, total,_round=1)
    return nt_diskstatus(total, used, free, percent)

def disk_partitions():
    ret_list=[]
    first_line=True
    disk_info = commands.getoutput('df')
    disk_partition = disk_info.split("\n")

    for values in disk_partition:
        if(first_line):
            first_line = False
            continue
        else:
            device, blocks, used, available, use_percent, mountpoint=values.split()
            ntuple = nt_diskpartitions(device, blocks, used, available, use_percent, mountpoint)

        ret_list.append(ntuple)

    return ret_list

def disk_all():
    disk = {}
    total_space = 0
    for part in disk_partitions():
        usage = get_disk_usage(part.mountpoint)
        total_space = total_space + usage.total
        disk [part.device] = {
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "percent_usage": usage.percent,
            "mount": part.mountpoint}

    disk['size'] = total_space
    return disk


def main():
    for part in disk_partitions():
        print part
        usage = get_disk_usage(part.mountpoint)
        print usage
        print "\n"

if __name__ == '__main__':
  #  main()   # print disk_partition
    print disk_all()