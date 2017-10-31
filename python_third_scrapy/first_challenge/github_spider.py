import scrapy

#scrapy runspider github_spider.py -o data.json

class ShiyanlouCoursesSpider(scrapy.Spider):

    name = 'shiyanlou-courses'

    @property
    def start_urls(self):
        """ 
        start_urls 需要是一个可迭代对象，所以，你可以把它写成一个列表、集合或者生成器，这里用的是生成器
        """
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'

        return (url_tmpl.format(i) for i in range(1, 4))

    def parse(self, response):
        for githubRepositories in response.xpath('//div[@id="user-repositories-list"]/ul/li'):
            yield {
                "name": githubRepositories.xpath('.//h3/a/text()').re_first('[^\w]*(\w*)'),
                "update_time": githubRepositories.xpath('.//div/relative-time/@datetime').extract_first()
            }

            '''
            name = response.xpath('//div[@id="user-repositories-list"]/ul/li')
            name[1].xpath('.//h3/a/text()').re_first('[^\w]*(\w*)')
            name[1].xpath('.//div/relative-time/@datetime').extract_first()
            '''