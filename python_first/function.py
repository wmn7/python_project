#!/usr/bin/env python

'''
def char_count(str,char):
    return str.count(char)

result = char_count('asdaaedafeafaf','a')
print(result)
'''

'''
import sys
import time

def char_count(str='abcdefg'):
    char_list=set(str)
    for char in char_list:
        print(char,str.count(char))

if __name__=='__main__':
    try:
        para = sys.argv[1]
        start = time.time()
        char_count(para)   
        end = time.time()
        print('time spending',end-start)    
    except:
        char_count()
        print('default')

'''

def connect(ipaddress,*ports):
    print("IP:",ipaddress)
    for port in ports:
        print('Port:',port)

connect('192,168.1.1',22,23,24)
