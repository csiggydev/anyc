#!/usr/bin/env python

'''
Author: Chris Segalas
Simple Netmiko script to retrieve list of remote VPN users on an ASA 

'''

# module imports

from netmiko import Netmiko
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')
ip = input('IP address: ')

# device dictionary - user input for IP address, username, pw and network device type.
device = {
      'host': ip,
      'username': username,
      'password': password,
      'device_type': 'cisco_asa',
        }
net_conn = Netmiko(**device)
print('Connected to:',  ip)
users = net_conn.send_command('show vpn- anyconnect | i User|Assign|Dur|Group') # Show Users, IP addresses, login duration and tunnel+policy groups
print(users)
net_conn.cleanup()
net_conn.disconnect()
print('Closed connection to ASA.')