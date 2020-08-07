#!/usr/bin

__author__ = "Mojtaba Eshghie"

import os
import time

CONTAINERS = {
    'router_a',
    'router_b'
}
DOCKER_EXEC = 'docker exec -d {container} vppctl {vpp_command}'
DOCKER_BUILD = 'docker build -t router .'
DOCKER_STOP = 'docker stop {container}'
DOCKER_REMOVE = 'docker rmi -f {container}'
DOCKER_RUN = 'docker run -v /etc/vpp -d --name {container} router'


print('------------------------- CloudVPP Demo -------------------------')

# container stopping phase:
print('### container stopping phase')
for container in CONTAINERS:
    os.system(DOCKER_STOP.format(container=container))
os.system('docker system prune')


# image removal phase
print('### image removal phase')
for container in CONTAINERS:
    os.system(DOCKER_REMOVE.format(container=container))


# building phase
print('### building phase')
os.system(DOCKER_BUILD)


# running phase
print('### running phase')
os.system(DOCKER_RUN.format(container='router_a'))
os.system("docker run -d --volumes-from router_a --name router_b router")


# execution phase
print('### execution phase')
print('Applying configurations, this takes a while. Sit tight...')
for container in CONTAINERS:
    config_path = 'conf/{container}.conf'.format(container=container)
    with open(config_path, 'r') as command_file:
        print(config_path)
        for vpp_command in command_file.readlines():
            print('applying: {vpp_command}')
            time.sleep(1)
            os.system(DOCKER_EXEC.format(vpp_command=vpp_command, container=container))
