#!/usr/bin/env python3

'''
安装scrapy爬虫框架
sudo python3 -m pip install scrapy
测试是否安装成功
在命令行里输入scrapy,出现版本号等信息则安装成功
'''

#scrapy内置两种数据提取语法:css和xpath

'''
可以使用scrapy shell来进行操作

scrapy shell [url]

需要提供一个网页的 url，执行命令后，scrapy 会自动去下载这个 url 对应的网页，将结果封装为 scrapy 内部的一个 response 对象并注入到 python shell 中，在这个 response 对象上，可以直接使用 scrapy 内置的css 和 xpath 数据提取器。


要在?和&前面加转意符\
scrapy shell https://www.shiyanlou.com/courses/\?category=all\&course_type=all\&fee=all\&tag=Python\&unfold=0

'''

#css
'''
例如要提取例子网页中 ID 为 images 的 div 下所有 a 标签的文本:
response.css('div#images a::text').extract()

div#images 表示 id 为 images 的 div，如果是类名为 images，这里就是 div.images。
extract 函数执行提取操作，返回一个列表

提取所有 a 标签的 href 链接
response.css('div#images a::attr(href)').extract()
不只是 href，任何标签的任意属性都可以用 attr() 提取

response.css('div#images a img::attr(src)').extract()
a标签里的img标签的src属性
'''

#xpath

'''
nodename 	选取此节点的所有子节点。
/ 	从根节点选取。
// 	从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
. 	选取当前节点。
.. 	选取当前节点的父节点。
@ 	选取属性。
'''

'''
用 scrapy 的 xpath 语法提取 div#images a 的所有文本，可以这样写：
response.xpath('//div[@id="images"]/a/text()').extract()


用 XPath 语法提取所有图片链接：@表示选取属性
response.xpath('//div[@id="images"]/a/img/@src').extract()

'''

#re和re_first方法－－使用正则表达式对内容作进一步处理

'''
response.css('div#images a::text').re('Name: (.+) ')
'''

#scrapy runspider shiyanlou_courses_spider.py -o data.json
