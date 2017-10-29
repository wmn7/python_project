import os
import json

file_name = os.listdir('./files')

'''
for name in file_name:
    with open('./files/'+name,'r') as file:
        result = json.loads(file.read())
        for i in result:
            print(i,result[i],sep=' : ')
'''

file_name = {}
with open('./files/helloworld.json','r') as file:
    result = json.loads(file.read())
    for i in result:
        file_name[i] = result[i]
    print(file_name)