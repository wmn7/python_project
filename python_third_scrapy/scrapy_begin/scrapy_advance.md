# scrapy爬虫高级应用

## 页面追随

在页面的url不是很好获取的时候，更常用的做法是从一个或者多个链接爬取页面后，再从页面中解析出需要的链接继续爬取。

这是复杂的写法

```python
# -*- coding: utf-8 -*-
import scrapy


class CoursesFollowSpider(scrapy.Spider):
    name = 'courses_follow'
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        yield {
            'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author': response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }
        # 从返回的 response 解析出“进阶课程”里的课程链接，依次构造
        # 请求，再将本函数指定为回调函数，类似递归
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href').extract():
            # 解析出的 url 是相对 url，可以手动将它构造为全 url
            # 或者使用 response.urljoin() 函数
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse)
```

关于urljoin可以看下面的例子

```
>>> response.urljoin('/course/1')
'https://www.shiyanlou.com/course/1'
```

我们可以使用response.follow来简化代码

```python
# -*- coding: utf-8 -*-
import scrapy


class CoursesFollowSpider(scrapy.Spider):
    name = 'courses_follow'
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        yield {
            'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author': response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }
        # 不需要 extract 了
        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href'):
            # 不需要构造全 url 了
            yield response.follow(url, callback=self.parse)
```

```
>>> response.follow('/course/1')
<GET https://www.shiyanlou.com/course/1>
```

callback称为回调函数，在这里表示拿到了数据以后要解析，所以把数据回调=parse(解析)

## 图片下载

scrapy 内部内置了下载图片的 pipeline。下面以下载实验楼课程首页每个课程的封面图片为例展示怎么使用它。

首先需要在 items.py 中定义一个 item ，它包含俩个必要的字段：

```python
class CourseImageItem(scrapy.Item):
    # 要下载的图片 url 列表
    image_urls = scrapy.Field()
    # 下载的图片会先放着这里
    images = scrapy.Field()
```

爬虫的核心工作就是解析所有图片的链接到 CourseImgeItem 的 image_urls 中。

下面的代码作为示范

```python
# -*- coding: utf-8 -*-
import scrapy

from shiyanlou.items import CourseImageItem


class CoursesImageSpider(scrapy.Spider):
    name = 'courses_image'
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        item = CourseImageItem()
        ＃解析图片链接到 item
        item['image_urls'] = response.xpath('//div[@class="course-img"]/img/@src').extract()
        yield item
```

代码完成后需要在 settings 中启动 scrapy 内置的图片下载 pipeline，因为 ITEM_PIPELINES 里的 pipelines 会按顺序作用在每个 item 上，而我们不需要 ShiyanlouPipeline 作用在图片 item 上，所以要把它注释掉

```python
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 100,
    # 'shiyanlou.pipelines.ShiyanlouPipeline': 300
}
```

还需要配置图片存储的目录：

```python
IMAGES_STORE = 'images'
```

运行程序

```python
# 安装需要的 PIL 包
pip3 install image

# 执行图片下载爬虫
scrapy crawl courses_image

```

scrapy 会将图片下载到 images/full 下面，保存的文件名是对原文件进行的 hash。为什么会有一个 full 目录呢？full 目录代表下载的图片的原尺寸的，因为 scrapy 可以配置改变下载图片的尺寸，比如在 settings 中给你添加下面的配置生成小图片：

```python
IMAGES_THUMBS = {
    'small': (50, 50)
}

```


## item包含多个页面数据

在前面几节实现的爬虫中，组成 item 的数据全部都是在一个页面中获取的。但是在实际的爬虫项目中，经常会遇到从不同的页面抓取数据组成一个 item。下面通过一个例子展示怎么处理这种情况。

有一个需求，爬取实验楼课程首页所有课程的名称、封面图片链接和课程作者。课程名称和封面图片链接在课程主页就能爬到，课程作者只有点击课程，进入课程详情页面才能看到，怎么办呢？

scrapy 的解决方案是多级 request 与 parse。简单的说就是先请求课程首页，在回调函数 parse 中解析出课程名称和课程图片链接，然后在 parse 函数再构造一个请求到课程详情页面，再在处理课程详情页的回调函数中解析出课程作者。


首先在 items.py 中创建 相应的 Item 类：

```
class MultipageCourseItem(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()
```

下面是示例代码

```python
# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import MultipageCourseItem


class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        for course in response.css('a.course-box'):
            item = MultipageCourseItem()
            # 解析课程名称
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract_first()
            # 解析课程图片
            item['image'] = course.xpath('.//img/@src').extract_first()
            # 构造课程详情页面的链接，爬取到的链接是相对链接，调用 urljoin 方法构造全链接
            course_url = response.urljoin(course.xpath('@href').extract_first())
            # 构造到课程详情页的请求，指定回调函数
            request = scrapy.Request(course_url, callback=self.parse_author)
            # 将未完成的 item 通过 meta 传入 parse_author
            request.meta['item'] = item
            yield request

    def parse_author(self, response):
        # 获取未完成的 item
        item = response.meta['item']
        # 解析课程作者
        item['author'] = response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        # item 构造完成，生成
        yield item
```


## 模拟登录

模拟登录的程序的基本结构和流程

```python
# -*- coding: utf-8 -*-
import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'

    start_urls = ['https://www.shiyanlou.com/login']

    def parse(self, response):
        """ 模拟登录的核心就在这里，scrapy 会下载 start_urls 里的
        登录页面，将 response 传到这里，然后调用 FormRequest
        模拟构造一个 POST 登录请求。FormRequest 继承自 Request，
        所以 Request 的参数对它适用。FormRequest 有一类方法 `from_response` 用于快速构建 FormRequest 对象。from_response 方法会从第一步返回的 response 中获取请求的 url，form 表单信息等等，我们只需要指定必要的表单数据和回调函数就可以了。
        """
        return scrapy.FormRequest.from_response(
             # 第一个参数必须传入上一步返回的 response
             response,
             # 以字典结构传入表单数据
             formdata={},
             # 指定回调函数
             callback=self.after_login
        )

    def after_login(self, response):
        """ 登录之后的代码和普通的 scrapy 爬虫一样，构造 Request，指定 callback ...
        """
        pass

    def parse_after_login(self, response):
        pass
```

下面我们看一个例子

```python
# -*- coding: utf-8 -*-
import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = 'login_spider'

    start_urls = ['https://www.shiyanlou.com/login']

    def parse(self, response):
        # 获取表单的 csrf_token 
        csrf_token = response.xpath('//div[@class="login-body"]//input[@id="csrf_token"]/@value').extract_first()
        self.logger.info(csrf_token)
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'csrf_token': csrf_token,
                # 这里要改为自己的邮箱和密码
                'login': 'example@email.com',
                'password': 'password',
            },
            callback=self.after_login
        )

    def after_login(self, response):
        # 登录成功后构造一个访问自己主页的 scrapy.Request
        # 记得把 url 里的 id 换成你自己的，这部分数据只能看到自己的
        return [scrapy.Request(
            url='https://www.shiyanlou.com/user/634/',
            callback=self.parse_after_login
        )]

    def parse_after_login(self, response):
        """ 解析实验次数和实验时间数据，他们都在 span.info-text 结构中。实验次数位于第 2 个，实验时间位于第 3 个。
        """
        return {
            'lab_count': response.xpath('(//span[@class="info-text"])[2]/text()').re_first('[^\d]*(\d*)[^\d*]'),
            'lab_minutes': response.xpath('(//span[@class="info-text"])[3]/text()').re_first('[^\d]*(\d*)[^\d*]')
        }

```