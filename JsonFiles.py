# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 11:55:41 2021

@author: Maulen
"""

import json
import random
from datetime import datetime

trimmed = ' asd '
timestamp = ' asd_ '

def Importsensordata():
    data = {}
    data['sensordata'] = []
    data['sensordata'].append({
        'sensor_id': 'ID1',
        'model': 'WS-0001',
        'payload': 'some data'
    })
    data['sensordata'].append({
        'sensor_id': 'ID2',
        'model': 'WS-0002',
        'payload': 'asdasd'
    })
    data['sensordata'].append({
        'sensor_id': 'ID3',
        'model': 'WS-0003',
        'payload': trimmed
    })
    data['sensordata'].append({
        'sensor_id': 'ID4',
        'model': 'WS-0004',
        'payload': timestamp
    })


    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
        
Importsensordata()
    
#read in console
print('PRINTING ALL SENSORS TO CONSOLE...')
print('_________________________________')
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['sensordata']:
        print('Sensor_id: ' + p['sensor_id'])
        print('Model: ' + p['model'])
        print('Payload: ' + p['payload'])
        print('')



#padToMultiple WS-0002
for s in data['sensordata']:
    s = (s['payload'])
    if s == 'asdasd':
        break

def padtomultipiple(s):
    while len(s) % 5 !=0:
        s = s + random.choice('#')
    return s
        


#trim and padToMultiple WS-0003
for whitespace in data['sensordata']:
    whitespace = (whitespace['payload'])
    if whitespace == ' asd ':
        whitespace = whitespace.strip()
        break
    
pad = padtomultipiple(s)
trimmed = padtomultipiple(whitespace)



#trim, padToMultiple, addTimestamp WS-0004

for fortimestamp in data['sensordata']:
    fortimestamp = (fortimestamp['payload'])
    if fortimestamp == ' asd_ ':
        fortimestamp = fortimestamp.strip()
        break

def addtimestamp(t):
    now = datetime.now() # current date and time
    date_time = now.strftime("%m%d%Y%H%M%S")
    #print("date and time:",date_time)
    t = fortimestamp+date_time
    return t

timestamp = addtimestamp(fortimestamp)



#results
print ('______RESULTS_______________:')
print ('WS-0002 - padToMultiple: ', pad)
print ('WS-0003 - trim, padToMultiple: ', whitespace,',',trimmed)
print ('WS-0004 - trim, padToMultiple, addTimestamp: ', whitespace,',',trimmed,
       ',',timestamp)
print ('')

#writing to file WS-0003, WS-0004
Importsensordata()
