import scrapy
import re
from tenholes.items import TenholesItem
from redis import Redis
import logging


class TestSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['http://tenholes.com/article/view?id=654']
    start_url = start_urls[0]
    article_count = int(re.search(r'\d+', start_url).group(0))

    def parse(self, response, **kwargs):
        conn = Redis('127.0.0.1',port=6379)
        for article_id in range(self.article_count,0,-1):
            url = 'http://tenholes.com/article/view?id=' + str(article_id)
            ex = conn.sadd('urls', url)
            if ex == 1:
                # logging.warning('出现异常。')
                logging.warning('在爬取这个URL（%s）时出现了警告',response.url)
                yield scrapy.Request(url,callback=self.parse_next_page)
            else:
                logging.warning('出现异常。')
                print('网站无数据更新')

    def parse_next_page(self, response):
        # if response.xpath('/html/body/div[6]/div/div/text()').extract_first() == '文章不存在':
        #     pass
        logging.warning('出现异常。')
        id = re.search(r'\d+', response.request.url).group(0)
        title = response.xpath('/html/body/div[6]/div[2]/div/h3/text()').extract_first()
        time = response.xpath('/html/body/div[6]/div[2]/div/div/span[3]/text()').extract_first()
        content = response.xpath('/html/body/div[6]/div[3]//p/text()').extract()
        content = ' '.join(content)
        item = TenholesItem()
        item['id'] = id
        item['title'] = title
        item['time'] = time
        item['content'] = content
        yield item











