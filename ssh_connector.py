import paramiko
import pandas as pd

routers  = pd.read_csv('device_list.csv')
for i in routers:
    print(i)

client_list = []   #list of ssh client objects

'''
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=)#
'''