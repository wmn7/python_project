#!/usr/bin/env python3

# lambda函数--匿名函数
double = lambda x:x*2
print(double(2))

# slice--获取一个序列（列表或元组）或者字符串的一部份，返回一个新的序列或者字符串，使用方法是中括号中指定一个列表的开始下标与结束下标，用冒号隔开

# 下标的对应关系
'''
 0  1  2  3  4  5  6
 a  b  c  d  e  f  g
-7 -6 -5 -4 -3 -2 -1
'''
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:3])
print(letters[:3])

# 列表解析（list comprehension）
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 获取numbers中的所有偶数
print([x for x in numbers if x%2==0])
#　对numbers中的每个数求平方
print([x*x for x in numbers])

# map和filter函数
print(list(map(lambda x : x * x,numbers)))
print(list(filter(lambda x : x % 2 == 0,numbers)))

# 字典解析（dict comprehension）--

# 理解了列表解析，字典解析就很容易了，就是把列表改为字典，处理的对象是字典中的 key 和 value。直接看例子吧：

d = {'a':1,'b':2,'c':3}
dn = {k:v*v for k,v in d.items()}
print(dn)

#迭代器
'''
首先明白迭代器和可迭代对象的区别。一个一个读取、操作对象称为迭代，Python 中，可迭代（Iterable）对象就是你能用 for…in 迭代它的元素，比如列表是可迭代的
而迭代器是指，你能要用 next 函数不断的去获取它的下一个值，直到迭代器返回 StopIteration异常。所有的可迭代对象都可以通过 iter 函数去获取它的迭代器
'''
letters = ['a','b','c']
for i in letters:
    print(i)

it = iter(letters)
print(next(it))

# 生成器

'''
和列表解析有点像，只不过使用的是圆括号。不同于列表可以反复迭代，再迭代这个迭代器，它不会打印元素，也不回报错。
使用生成器有什么好处呢？因为生成器不是把所有元素存在内存，而是动态生成的，所以当你要迭代的对象有非常多的元素时，使用生成器能为你节约很多内存，这是一个内存友好的特性。
'''

g = (x**x for x in range(1,4))
for x in g:
    print(x)
print('----------')
#下面一遍是不会被打印的
for x in g:
    print(x)

#yield
'''
而 yield 返回的是一个生成器，函数碰到 return 就直接返回了，使用了 yield 的函数，到 yield 返回一个元素，当再次迭代生成器时，会从 yield 后面继续执行，知道遇到下一个 yield 或者函数结束退出
'''
def fib(n):
    current = 0
    a , b = 1 , 1
    while current<n:
        yield a
        a , b = b , a + b
        current = current + 1

f5 = fib(5)
for i in f5:
    print(i)


# 装饰器
from datetime import datetime
from functools import wraps
def log(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        print('Function ' + func.__name__ + ' has been called at '+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return func(*args,**kwargs)
    return decorator

# 就是在执行add函数的时候,把add函数作为参数传入log函数
@log
def add(x,y):
    return x+y

print(add(1,2))






