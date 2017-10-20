#!/usr/bin/env python3

# 打开关闭文件

'''
open() 函数需要两个参数，第一个参数是文件路径或文件名，第二个是文件的打开模式。模式通常是下面这样的

    "r"，以只读模式打开，你只能读取文件但不能编辑/删除文件的任何内容
    "w"，以写入模式打开，如果文件存在将会删除里面的所有内容，然后打开这个文件进行写入
    "a"，以追加模式代开，写入到文件中的任何数据将自动添加到末尾
    "b"，以二进制的方式代开

文件使用完毕后应该使用file.close()来关闭文件

在实际情况中，我们应该尝试使用 with 语句处理文件对象，它会在文件用完后会自动关闭，就算发生异常也没关系。它是 try-finally 块的简写
在代码块中不需要使用close,因为在代码执行到with语句之外，文件会自动关闭

'''

with open('./test.txt') as file:
    count = 0
    for line in file:
        count = count+1
    print('文件行数：'+str(count))


print('----------------')

# 读取文件内容

'''
使用 read() 可以一次性读取整个文件的内容到字符串
项目开发中，我们需要谨慎使用 read() 读取整个文件，因为有可能你的系统内存并不足够存储整个文件的内容。
'''

'''
处理文本文件的时候，我们通常会采用逐行处理，
readline() 就是用来每次读取文件的一行，
readlines() 可以读取所有行，
但不同于 read()，这个函数的返回的是一个列表，列表中每个元素都是对应文本文件中一行内容的字符串
readlines返回一个数组
'''

file = open('./test.txt')
file_line = file.readlines()
print(file_line)
file.close()

#使用for循环遍历文件对象读取每一行
file = open('./test.txt')
for x in file:
    # 默认print结尾会有回车
    print(x,end='')
file.close()
# 写入文件

'''
常用的写入文件的方法是write()
ｗ模式打开会覆盖之前的内容，ａ模式则进行追加
'''

file = open('./test.txt','a')
file.write('nice to meet you\n')
file.close()

#使用with写法不用写close，之前都需要写close
with open('./test.txt','a') as file:
    file.write('nice to meet you too\n')


with open('./test.txt') as file:
    count = 0
    for file_line in file:
        count = count+1
        print(file_line,end='')
    print(count)


print('------------------------')

'''
# 拷贝文件
import sys

def copy_file(src,dst):
    with open(src,'r') as file1:
        with open(dst,'w') as file2:
            file2.write(file1.read())

if __name__ == '__main__':
    if len(sys.argv)==3:
        copy_file(sys.argv[1],sys.argv[2])
    else:
        print("Parameter Error")
        sys.exit(-1)
    sys.exit(0)
'''

# pickle和json序列化

'''
注意写入和读取文件都需要使用 b 二进制模式。
'''

# 使用pickle序列化

'''
dumps 和 loads 分别执行了序列化和反序列化的操作
'''

import pickle
course = {1:'Linux',2:'Vim',3:'Git'}
with open('./course.data','wb') as file:
    pickle.dump(course,file)

with open('./course.data','rb') as file:
    result = pickle.load(file)
    print(result)


#json

'''
JSON 序列化后的内容为字符串，所以文本写入和读取不需要用二进制格式
'''

import json
course = {1:'Linux',2:'Vim',3:'Git'}
print(type(list(course.keys())[1]))
with open('course.json','w') as file:
    file.write(json.dumps(course))

with open('course.json','r') as file:
    result = json.loads(file.read())
    print(result)
print(type(list(result.keys())[0]))
# os.path 文件与文件夹操作


'''
在这里简单介绍下 os.path 这个非常常用的标准库，这个库主要的用途是获取和处理文件及文件夹属性。

下面代码举例介绍几个常用的方法，更多的内容在使用到的时候查阅文档。

    os.path.abspath(path) 返回文件的绝对路径
    os.path.basename(path) 返回文件名
    os.path.dirname(path) 返回文件路径
    os.path.isfile(path) 判断路径是否为文件
    os.path.isdir(path) 判断路径是否为目录
    os.path.exists(path) 判断路径是否存在
    os.path.join(path1[, path2[, ...]]) 把目录和文件名合成一个路径

'''


