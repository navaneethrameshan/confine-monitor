from subprocess import check_output
from client.nodeinfo.sliverinfo import lxc
from client.nodeinfo.sliverinfo.lxc import utils

def collectData(container):
    container_info = {}
    all_info = {}

    container_info['container'] = container
    container_info.update(utils.container_mem_usage(container))
    container_info.update(utils.container_cpu_usage(container))
    container_info.update(utils.get_name(container))

    all_info[container] = container_info
    #    print all_info.items()
    return all_info


def collectAllData():
    container_info = {}
    all_info = {}

    container_list = lxc.utils.getRunningContainers()
    print 'Monitoring all started containers: '
    for container in container_list:
        if not "7d" in container:
            container_info.update(collectData(container))

    all_info['slivers'] = container_info

    print all_info.items()
    return all_info

def main():
    collectAllData()

