import numpy as np

#numpy的学习

#多维的创建

'''
这里的[]就是传入一个list类型的数据
'''

a1 = np.array([1,2,3,4])
#这里a2是两行三列的
a2 = np.array([[1.0,2,3],[0.5,4,9]])
#返回a1,a2的矩阵为多大的
print(a1.shape)
print(a2.shape)
#返回维度
print(a1.ndim)
print(a2.ndim)
#返回a1,a2的大小
print(a1.size)
print(a2.size)
#返回a1,a2的数据类型
print(a1.dtype)
print(a2.dtype)
#返回a1,a2中最小的值
print(a1.min())
print(a2.min())

print('---------------')

'''
除了前面介绍的直接使用 np.array 创建数组外，NumPy 还有多种方法可以创建多维数组：

    np.arange 类似于 Python 内置的 range，创建一维数组；
    np.ones 创建元素值全部为 1 的数组；
    np.zeros 创建元素值全为 0 的数组；
    np.empty 创建空值多维数组，只分配内存，不填充任何值；
    np.random.random 创建元素值为随机值的多维数组；

当没有指定 dtype 类型时，多维数组元素类型默认是 float64

'''

a1 = np.arange(4)
print(a1)

#可以通过dtype来指定元素的数据类型
a1 = np.ones((3,4),dtype=np.int64)
print(a1)

a1 = np.zeros((3,3))
print(a1)

a1 = np.ones((2,2,3))
print(a1)

#生产随机的矩阵
a1 = np.random.random((10))
print(a1)

print('----------------')

#ndarray 对象还可以通过 reshape 方法变形为其他维度的数组

a1 = np.arange(12)
print(a1.reshape(4,3))

print('========================')

#多维数组的索引

'''
这里的索引与python中列表的工作方式是一样的
'''
a1 = np.arange(7)
print(a1)
print(a1[1:7:2])
print(a1[1:5])

'''
并且在这里可以通过切片来赋值
'''
a1[5:8] = -1
print(a1)

'''
多维数组的切片
对于二维数组，可以通过 a[x, y] 的方式进行索引，三维数组可以通过 a[x, y, z] 的方式进行
'''

a1 = np.arange(12).reshape(3,4)
print(a1)
#打印a1的第一行
print(a1[0])
print(a1[0,1])
#打印a1的第一列
print(a1[:,0])
print(a1[:,1])

print('-----------')

#我们再看一个三维数组
a1 = np.arange(27).reshape(3,3,3)
print(a1)
print('-----------------')
print(a1[0,0])
print('-----------------')
#这是选择第二维度上的元素
print(a1[:,0])
print('-----------------')
#这是选择第三维度上的元素s
print(a1[:,:,0])

print('===================')

#多维数组的运算

'''
多维数组与标量的运算
'''
a1 = np.arange(12).reshape(3,4)
print(a1)
print('-----------------')
print(a1+1)
print('-----------------')
print(a1*2)
print('-----------------')

'''
多维数组间的运算
'''

a1 = np.arange(4).reshape(2,2)
a2 = np.arange(4,8).reshape(2,2)

print('----------------')

print(a1)
print(a2)

print('----------------')
#元素间对于运算
print(a1-a2)
print(a1*a2)

print('----------------')

#多维数组间进行矩阵运算
print(a1.dot(a2))

print('-----------------')

'''
这个是一个很好的用法

多维数组还支持逻辑比较运算，比如我们想知道一个多维数组中哪些值大于某一个指定值？典型的做法是通过循环实现，但是在 NumPy 中却可以直接通过比较实现
'''

a1 = np.arange(12).reshape(4,3)

a2 = a1 > 5
print(a2)
print('---------------------')
print(a1[a2])

'''
NumPy 的多维数组还有一些方法，可以用于统计数组中一些统计量，假如 a 为一个多维数组，则：

    a.sum 计算多维数组的所有元素的和；
    a.max 最大值计算；
    a.min 最小值计算；
    a.mean 平均值计算；
    a.std 标准差计算；
    a.var 方差计算；

以上所有方法，都可以接受一个 axis 参数，用于指定具体统计哪根轴上的数据。比如二维数组，可以理解为有 x, y 两根轴，分别代表行和列，指定 axis=0 时代表分别统计每列上的数据，axis=1 时，代表分别统计每一行上的数据。没有指定axis 参数时，代表统计所有元素。

'''

print('-------------------')

print(a1)

print(a1.sum())
#统计每一列上的元素的和
print(a1.sum(axis=0))
#统计每一行上元素的和
print(a1.sum(axis=1))

#对a1进行开放运算
print(np.sqrt(a1))

print('==================')

'''
在数据分析中，我们更多的针对表格数据进行处理，也就是 NumPy 中的二维数组数据，尽管 NumPy 对于多维数组的支持已经足够强大，但 Pandas 处理这些二维数据时更加得心应手。Pandas 建立在 NumPy 基础之上，但增加了更加高级实用的功能，比如数据自动对齐功能，时间序列的支持，缺失数据的灵活处理等等。
'''


#pandas的学习

# series和dataframe

import pandas as pd
from pandas import Series,DataFrame

'''
Series 和 DataFrame 是 Pandas 中的两种核心数据结构，大部分 Pandas 的功能都围绕着两种数据结构进行。

Series 是值的序列，可以理解为一维数组，它只有一个列和 索引。索引可以定制，当不指定时默认使用整数索引，而且索引可以被命名
'''

s1 = Series([1,2,3,4,5])
print(s1)

s2 = Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s2)
print(s2.index)

print('-----------------')

'''
DataFrame 类似于二维数组，有行和列之分，除了像 Series 一样，多个行有索引而外，每个列上面还可以有标签 label, 索引和标签本身都可以被命名
'''

df = DataFrame(np.random.random((5,4)),index=['a','b','c','d','e'],columns=['A','B','C','D'])

print(df)

print('-----------------')

#选择其中部分数据
s2 = Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s2)
print(s2['a':'d'])
print(s2[0:4])
print(s2['c'])

print('------------------')

df = DataFrame(np.random.random((5,4)),index=['a','b','c','d','e'],columns=['A','B','C','D'])

print(df)

print('------------------')
#选中一列
print(df['A'])
#选中一行
print(df.loc['a'])
#选中多列
print(df.loc[:,['B','D']])
#选中某一具体的元素
print('------------------')
print(df.loc['a','A'])

#缺失值和数据自动对齐

'''
在 Pandas 中最重要的一个功能是，它可以对不同索引的对象进行算术运算。比如将两个 Series 数据进行相加时，如果存在不同的索引，则结果是两个索引的并集，
'''
print('-------------------')
s1 = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = Series([2, 3, 4, 5], index=['b', 'c', 'd', 'e'])
print(s1)
print(s2)
print(s1+s2)

'''
以上代码中创建了两个 s1 和 s2 两个 Series 序列，两者具有相同的索引 ['b', 'c', 'd'], 所以在进行相加时，相同索引上的值会相加，但不重叠的索引引入 NaN 值，也就是缺失值。而缺失值会在运算中传播，所以最终结果也是 NaN 值。根据相同的索引进行自动计算，这就是自动对齐功能。同样的规则，在 DataFrame 数据中也生效
'''

print('-------------------')
df1 = DataFrame(np.arange(9).reshape(3,3),columns=list('ABC'),index=list('abc'))

df2 = DataFrame(np.arange(12).reshape(3,4),columns=list('ABDE'),index=list('bcd'))

print(df1)
print(df2)
print(df1+df2)

'''
当然我们在计算时，可以指定使用值来填充 NaN 值，然后带入计算过程
'''

print(df1.add(df2,fill_value=0))
'''
我们指定了使用 0 填充 NaN 值，然后带入计算过程，注意这里填充的不是最终的运算结果。可以看到依然有元素为 NaN 值，这是因为这个位置的元素在 df1 和 df2 中都未定义。

大部分的 Series 和 DataFrame 操作中都支持数据自动对齐功能，同时也支持 fill_value 参数指定 NaN 值的填充值。
'''

print('------------------')

#常规运算

'''
在 Pandas 中还有一种比较常见的操作是将函数应用到每行或者每一列上面，DataFrame 的 apply 方法可以实现此功能，比如想统计每行和每列的极差（最大值和最小值之差）
'''

#columns是列标

df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('ABC'), index=list('abc'))

print(df1)
f = lambda x:x.max()-x.min()
#统计出每列的极差
print(df1.apply(f))
#统计出每行的极差
print(df1.apply(f,axis=1))

'''
如果想将某函数应用到每一个元素上，对于 DataFrame 数据可使用 df.applymap 方法，而对于 Series 数据可以使用 s.map 方法
'''

print(df1.applymap(lambda x:x+1))

print('------------------')

#常用统计

print('===================')

'''
describe 方法可以得知当前数据的一些常用统计信息
'''

df1 = DataFrame(np.arange(9).reshape(3,3), columns=list('ABC'), index=list('abc'))

print(df1)

print(df1.sum())
print(df1.mean())
print(df1.sum(axis=1))
#describe 方法显示了一些常用的统计信息
print(df1.describe())
#获得转置
print(df1)
print(df1.T)
print(df1.T.describe())

print('-------------------')

#数据合并和分组

df1 = DataFrame(np.random.random((3,3)))
df2 = DataFrame(np.random.random((3,3)),index=[5,6,7])

print(df1)
print(df2)
print('------------------')
#pandas.concat 函数成功的拼接了两个 DataFrame 数据
print(pd.concat([df1,df2]))

print('------------------')

df1 = DataFrame({'user_id': [5348, 13], 'course': [12, 45], 'minutes': [9, 36]})

df2 = DataFrame({'course': [12, 45], 'name': ['Linux 基础入门', '数据分析']})

print(df1)
print(df2)
#df1 和 df2 有共同的列 course, 当进行 merge 操作的时候 Pandas 会自动安装这列进行合并。
print(pd.merge(df1,df2))

print('-------------------')

#寻找user_id是5348的学习时间
df = DataFrame({'user_id': [5348, 13, 5348], 'course': [12, 45, 23], 'minutes': [9, 36, 45]})

print(df)
print('--------------------')
print(df['user_id'])

print(df[df['user_id']==5348]['minutes'])

print(df[df['user_id']==5348]['minutes'].sum())

#使用类似于数据库的 GROUP BY 功能进行计算

print('--------------------')

print(df[['user_id','minutes']])

print(df[['user_id','minutes']].groupby('user_id').sum())

print('--------------------')

#时间序列处理

print('--------------------')
'''
在 Python 中，时间处理方面的相关功能主要集中在 datetime 包中，主要有的三种对象：

    datetime.datetime 代表时间对象；
    datetime.date 代表某一天；
    datetime.timedelta 代表两个 datetime.datetime 对象之间的时间差；

'''

from datetime import datetime, timedelta

#创建简单的时间序列
dates = [datetime(2018, 1, 1), datetime(2018, 1, 2), datetime(2018, 1, 3), datetime(2018, 1,4)]
ts = Series(np.random.randn(4), index=dates)
print(ts)
#接下来就可以通过时间来对ts进行检索
print('--------------------')
#下面四种写法都是可以的
print(ts['2018/1/1'])
print(ts['2018-1-1'])
print(ts['1/1/2018'])
print(ts[datetime(2018,1,1)])

'''
在 Pandas 中生成日期范围也非常灵活，主要通过 pandas.date_range 函数完成，该函数主要有以下几个参数:

    start: 指定了日期范围的起始时间；
    end: 指定了日期范围的结束时间；
    periods: 指定了间隔范围，如果只是指定了 start 和 end 日期的其中一个，则需要改参数；
    freq: 指定了日期频率，比如 D 代表每天，H 代表每小时，M 代表月，这些频率字符前也可以指定一个整数，代表具体多少天，多少小时，比如 5D 代表 5 天。还有一些其他的频率字符串，比如 MS 代表每月第一天，BM 代表每月最后一个工作日，或者是频率组合字符串，比如 1h30min 代表 1 小时 30 分钟。

'''

print('------------------')

print(pd.date_range('2018-1-1','2019',freq='M'))

print(pd.date_range('2018-1-1','2019',freq='MS'))

print('-------------------')

'''
有的时候时间序列是按每小时显示统计的，但是我们想将统计频率转换成按天来统计，这个时候可以使用时间序列的 resample 方法，该方法非常强大，不仅仅支持高频率的数据聚合到低频率 （降采样），也支持低频率转化到高频率统计（升采样），先创建数据集
'''

dates = pd.date_range('2018-1-1','2018-1-2 23:00:00',freq = 'H')

ts = Series(np.arange(len(dates)),index=dates)

print(ts.size)
print(ts.head(5))
#这里两种显示最后五个元素的方法都是可以的
print(ts.tail(5))
print(ts[-5:])

print('------------------')

#下面将数据转为每天的统计
print(ts.resample('D').sum())
print('------------------')
print(ts.resample('D').mean())

'''
当把低频率的数据转换成高频率的数据时，默认情况下 Pandas 会引入 NaN 值，因为没办法从低频率的数据计算出高频率的数据，但可以通过 fill_method 参数指定插值方式,使用 ffill （代表用前面的值替代 NaN 值）就不会有 NaN 值出现
'''

print(ts.resample('D').mean().resample('H').mean())

print('-----------------')

print(ts.resample('D').mean().resample('H').ffill())






