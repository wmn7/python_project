#!/usr/bin/env python3

# datetime模块--提供日期和时间的计算
'''
datetime 模块提供了一些类用于操作日期时间及其相关的计算。比较常用三个类型：

    date 封装了日期操作
    datetime 封装日期+时间操作
    timedelta 表示一个时间间隔，也就是日期时间的差值

'''

from datetime import date,datetime,timedelta

t = datetime.now()
print(t)
# 显示为哪一号
print(t.day)
#　将datetime对象与字符串之间相互转换
print(datetime.strftime(t,'%Y-%m-%d %H:%M:%S'))
print(datetime.strptime('2017-10-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

# 使用timedelta 表示时间差值
print(t+timedelta(hours=3))

# os模块--模块提供了一些接口来获取操作系统的一些信息和使用操作系统功能。

import os

#获取当前工作目录
print(os.getcwd())
# 生成 n 个字节的随机数，用于加密，比如作为 Flask 的 SECRET_KEY
print(os.urandom(10))

# sys 模块可以用于用与获取 Python 解释器当前的一些状态变量，最常用的就是获取执行 Python 脚本时传入的参数，比如说执行 test.py时传入了一些参数
'''
python3 test.py arg1 arg2 arg3
那么在 Python 程序中就可以通过 sys.argv 来获取这些参数
sys.argv  # ['test.py', 'arg1', 'arg2', 'arg3']
'''

#requests模块
import requests
r = requests.get('https://www.shiyanlou.com')
print(r.headers)

# base64模块
import base64
print(base64.b64encode(b'hello world'))
print(base64.b64decode(base64.b64encode(b'hello world')))

# collections模块
# collections模块提供一些特殊的容器,如下

from collections import OrderedDict,namedtuple,Counter
import json

'''
OrderedDict 是一个特殊的字典。字典本质上是一个哈希表，其实现一般是无序的，OrderedDict 能保持元素插入的顺序：
'''

d = OrderedDict()
d['apple'] = 1
d['google'] = 2
d['facebook'] = 3
print(d)
print(d['apple'])
print(d.keys())#和字典类型的用法是一样的
print(json.dumps(d))

'''
使用普通的元组（tuple）存在一个问题，每次用下标去获取元素，可能会不知道你这个下标下的元素到底代表什么。namedtuple 能够用来创建类似于元组的类型，可以用索引来访问数据，能够迭代，也可以通过属性名访问数据。
'''

point = namedtuple('User',['name','sex','age'])
p = point(1,2,3)
print(p.name)


'''
Counter 用来统计一个可迭代对象中各个元素出现的次数，以字符串为例：
'''
c = Counter('wdeqfqesacedzascweda')
print(c)
print(c.most_common(3))