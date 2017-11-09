#!/usr/bin/env python3


'''
编辑mysql的配置文件，修改编码方式
sudo vim /etc/mysql/my.cnf

[client]
default-character-set = utf8

[mysqld]
character-set-server = utf8

[mysql]
default-character-set = utf8
'''

'''
pip3 install sqlalchemy

sudo apt-get install libmysqlclient-dev
pip3 install mysqlclient
'''

'''
创建项目

用 scrapy 提供的 startproject 命令创建一个 scrapy 项目

scrapy startproject shiyanlou

'''

'''
创建爬虫
scrapy 的 genspider 命令可以快速初始化一个爬虫模版，使用方法如下

scrapy genspider <name> <domain>

name 这个爬虫的名称，domain 指定要爬取的网站。
要进入第二个目录去初始化

cd /home/shiyanlou/Code/shiyanlou/shiyanlou
scrapy genspider courses shiyanlou.com

scrapy 会在 spiders 目录下新建一个 courses.py 的文件，并且在文件中为我们初始化了代码结构

'''

'''
修改items.py文件，为爬去的内容定义一个item

定义 Item 非常简单，只需要继承 scrapy.Item 类，将每个要爬取
    的数据声明为 scrapy.Field()。下面中上一节中每个课程要爬取的 4 
    个数据。


name = scrapy.Field()
description = scrapy.Field()
type = scrapy.Field()
students = scrapy.Field()

'''

'''
Item Pipeline

如果把 scrapy 想象成一个产品线，spider 负责从网页上爬取数据，Item 相当于一个包装盒，对爬取的数据进行标准化包装，然后就把扔到Pipeline 流水线中

主要在 Pipeline 对 Item 进行这几项处理：

    验证爬取到的数据 (检查 item 是否有特定的 field)
    检查数据是否重复
    存储到数据库

'''


'''
定义 Model，创建表

在 items.py 所在目录下创建 models.py，在里面使用 sqlalchemy 语法定义 courses 表结构
'''

'''
保存 item 到数据库
创建好数据表后，就可以在 pipeline 写编写代码将 爬取到的每个 item 存入数据库中。
'''