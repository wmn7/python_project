#matplotlib入门

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame

'''
N = 50
x = np.random.random((N))
y = np.random.random((N))
colors = np.random.random((N))
#区域的面积
area = np.pi*(15*np.random.rand(N))**2
plt.scatter(x,y,s=area,c=colors,alpha=0.5)
#只能保存成png的格式
plt.savefig('test.png')
#plt.show()
'''

#matplotlib入门

'''
matplotlib 是面向对象的绘图工具包，绘制的图形中每一个元素都是一个对象，比如线条，文字，刻度等信息，可以通过修改这些对象的属性，从而改变绘图样式。

matplotlib 中主要的绘图对象列表如下：

    Figure 对象，可以想象为一张画布；
    Axes 对象，字面理解为坐标轴（因为每一个 Axes 都有一套 X Y轴坐标系，绘制图形时基于此坐标系绘制。) 也可以认为是子图，在一个 Figure 对象中可以包含多个 Axes 对象，也就是说一张画布可以包含多个子图；
    Line2D 对象，代表线条；
    Text 对象，代表了文字，比如一张子图需要标题，就可以使用一个 Text 对象；

虽然 matplotlib 是面向对象的绘图工具包，但是也提供了一些常用的绘图方法，可以直接调用 plt 模块相关方法就可以完成各种绘图需求，这是因为 plt 模块内部保存了当前的 Figure 对象信息，当使用 plt 的相关方法绘图时，底层实际调用了当前 Figure 对象的相关方法。在前面的散点图例子中，我们没有创建过任何 Figure 对象也成功的绘制出了图形，这就是因为 plt 会默认创建 Figure 对象，并将它保存在 plt 模块内部。可以通过 plt.gcf() 和 plt.gca() 分别获取当前用于绘图的 Figure 和 Axes 对象。
'''


'''
fig.add_subplot(1, 1, 1) 方法，用于在 Figure 对象上创建一个新 Axes 对象，由于 Figure 对象可以包含多个 Axes 对象，所以这里的参数含义是说，添加一个 Axes 对象到布局为一行一列的第一个位置上。

当然可以改变布局，比如 fig.add_subplot(2, 2, 1) 含义是添加一个 Axes 对象到布局为两行两列的第一个位置上，也就是说我们依次调用 fig.add_subplot(2, 2, 2), fig.add_subplot(2, 2, 3), fig.add_subplot(2, 2, 4） 在 Figure 对象上插入四个 Axes 对象，布局为两行两列
'''

'''
fig1 = plt.figure()
ax1 = fig1.add_subplot(2, 2, 1)
ax2 = fig1.add_subplot(2, 2, 2)
ax3 = fig1.add_subplot(2, 2, 3)
ax4 = fig1.add_subplot(2, 2, 4)
ax1.plot(np.random.randn(50).cumsum(), 'k--')
ax2.hist(np.random.randn(100), bins=20, color='k')
ax3.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
'''

'''
解决matplotlib库show()方法不显示图片
是plt.show()而不是pic01.show()
'''
#fig1.savefig('1.png')

'''
#常规属性设置

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#设置标题
ax.set_title('Axes Example')

#先把刻度保存在数组里
major_ticks = np.arange(0,101,20)
minor_ticks = np.arange(0,101,5)

#设置刻度
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks,minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks,minor=True)

#设置x,y轴标签
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')

#设置网格
ax.grid(which='minor',alpha=0.2)
ax.grid(which='major',alpha=0.5)

#添加文字
ax.text(43.5,50,"shiyanlou")

#定制绘制曲线的颜色
x = np.linspace(0, 10,100)
'''

'''
前两个参数分别对应于 X, Y 轴的数据，绘图时会根据 x 和 x ** (1/8) 值序列确定曲线的位置。第三个参数 b-- 代表绘制的曲线是 blue 蓝色，样式是虚线
'''
#ax.plot(x, x ** 4, 'b--', label=r'$y = x^{4}$')
#ax.plot(x, x ** 3, 'r--', label=r'$y = x^{3}$')

#ax.plot(x, x ** (1/2), 'r.', label=r'$y = x^{1/2}$')

'''
ax.plot(x, x ** 2, 'b.', label=r'$y = x^{2}$')

ax.plot(x, x, 'g-', label=r'$y = x$')

#生成图例
ax.legend()

plt.show()

'''

#常用图形

#线性图--plot

'''
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = np.linspace(0,10,100)
y = np.linspace(10,20,100)
ax.plot(x,y)
plt.show()
'''

#直方图

'''
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#产生均值为0，标准差为20的1000个值
data = np.random.normal(0,20,1000)
#产生x轴的刻度
bins = np.arange(-100,100,5)
ax.hist(data,bins=bins)
plt.show()
'''

#散点图

'''
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x = np.arange(1,101)
y = 20+3*x+np.random.normal(0,60,100)
ax.scatter(x,y)
plt.show()
'''

#箱线图

'''
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# 产生 50 个小于 100 的随机数
spread = np.random.rand(50) * 100
# 产生 25 个值为 50 的数据
center = np.ones(25) * 50
# 异常值
outlier_high = np.random.rand(10) * 100 + 100
outlier_low = np.random.rand(10) * -100
#拼接上面的数据
data = np.concatenate((spread, center, outlier_high, outlier_low))

ax.boxplot(data)
plt.show()
'''

#pandas绘图

#cumsum是求累计和
'''
s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))

s.plot()
plt.show()
'''
#画箱线图
df = pd.DataFrame(np.random.rand(5,4), columns=['A', 'B', 'C', 'D'])
df.boxplot()
plt.show()

