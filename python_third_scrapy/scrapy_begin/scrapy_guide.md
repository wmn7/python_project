# scrapy爬虫项目总结


## 连接数据库

将mysql编码设置为utf-8

```
打开配置文件
sudo vim /etc/mysql/my.cnf

添加下面的配置
[client]
default-character-set = utf8

[mysqld]
character-set-server = utf8

[mysql]
default-character-set = utf8
```

设置好编码格式后进入数据库，创建database给爬虫使用

```
使用sqlalchemy连接mysql
pip3 install sqlalchemy

还需要安装 Python3 连接 MySQL 的驱动程序 mysqlclient
sudo apt-get install libmysqlclient-dev
pip3 install mysqlclient
```


首先要保证mysql开始运行

```
sudo service mysql start
```

## 创建 Scrapy 项目

使用startproject创建一个项目，最后的参数为项目的名字

```
scrapy startproject shiyanlou
```

## Item 容器

爬虫的主要目标是从网页中提取结构化的信息，scrapy 爬虫可以将爬取到的数据作为一个 Python dict 返回，但由于 dict 的无序性，所以它不太适合存放结构性数据。scrapy 推荐使用 Item 容器来存放爬取到的数据。

所有的 items 写在 `items.py` 中，下面举一个例子

```python
import scrapy


class CourseItem(scrapy.Item):

    """
    定义 Item 非常简单，只需要继承 scrapy.Item 类，将每个要爬取的数据声明为 scrapy.Field()。
    """

    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()
```

如果要爬取图片，要在items.py里增加一个item

```python
class CourseImageItem(scrapy.Item):
    # 要下载的图片 url 列表
    image_urls = scrapy.Field()
    # 下载的图片会先放着这里
    images = scrapy.Field()

```

## Models 创建表(如果要链接数据库的话要做)

在 items.py 所在目录下创建 models.py，在里面使用 sqlalchemy 语法定义 courses 表结构。
这个表是用来存放你爬取到的数据的。

示例代码：

```python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer,Date


engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    description = Column(String(1024))
    type = Column(String(64), index=True)
    students = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
```

最后要运行python3 models.py,去创建表



## 创建爬虫

进入上面创建项目后的目录,如在上面是shiyanlou，使用genspider命令快速初始化一个爬虫的模板

```
scrapy genspider <name> <domain>
```

name 这个爬虫的名称，domain 指定要爬取的网站

这是scrapy会在spiders目录下新建一个name.py的文件,文件名字是你爬虫的名字

**注意在这里要import我们在items里面定义的类**

```python
# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'

    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_tmpl.format(i) for i in range(1, 23))

    def parse(self, response):
        for course in response.css('div.course-body'):
            # 将返回结果包装为 CourseItem 其它地方同上一节
            item = CourseItem({
                'name': course.css('div.course-name::text').extract_first(),
                'description': course.css('div.course-desc::text').extract_first(),
                'type': course.css('div.course-footer span.pull-right::text').extract_first(default='免费'),
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
            })
            '''
            也可以写成像这里这样
            item = CourseItem()
            item['name'] = course.css('div.course-name::text').extract_first()
            item['description'] = course.css('div.course-desc::text').extract_first()
            '''
            yield item
```


## Item Pipeline

如果把 scrapy 想象成一个产品线，spider 负责从网页上爬取数据，Item 相当于一个包装盒，对爬取的数据进行标准化包装，然后就把扔到Pipeline 流水线中。

主要在 Pipeline 对 Item 进行这几项处理：

    验证爬取到的数据 (检查 item 是否有特定的 field)
    检查数据是否重复
    存储到数据库

### pipeline规范格式

下面是范例代码

```python
class ShiyanlouPipline(object):
    def process_item(self, item, spider):
        return item

    def open_spider(self, spider):
        """ 
        当爬虫被开启的时候调用
        """
        pass

    def close_spider(self, spider):
        """ 
        当爬虫被关闭的时候调用
        """
        pass
```

### 保存 Item 到数据库

参考下面的代码

```python
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, engine
from datetime import datetime

class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        # 提取的学习人数是字符串，把它转换成 int
        item['students'] = int(item['students'])
        # 根据 item 创建 Course Model 对象并添加到 session
        # item 可以当成字典来用，所以也可以使用字典解构, 相当于
        # Course(
        #     name=item['name'],
        #     type=item['type'],
        #     ...,
        # )
        self.session.add(Course(**item))
        return item
        #必须要返回一个item

    def open_spider(self, spider):
        """ 在爬虫被开启的时候，创建数据库 session
        """
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        """ 爬虫关闭后，提交 session 然后关闭 session
        """
        self.session.commit()
        self.session.close()
```

我们编写的pipeline默认是关闭的，要开启他，需要在settings.py将下面的代码取消注释

```python
# 默认是被注释的
ITEM_PIPELINES = {
    'shiyanlou.pipelines.ShiyanlouPipeline': 300
}
```

### Item 过滤

```python

from scrapy.exceptions import DropItem

class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        item['students'] = int(item['students'])
        if item['students'] < 1000:
            # 对于不需要的 item，raise DropItem 异常
            raise DropItem('Course students less than 1000.')
        else:
            self.session.add(Course(**item))

```

## 运行
scrapy crawl name(爬虫的名字)


