import scrapy
from scrapyTest.items import ScrapytestItem
import urllib

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['yikm.net']
    start_urls = ['https://www.yikm.net']

    def parse(self,response):
        type_url = response.xpath("//ul[@id='menuul']/li/a/@href")
        for i in type_url:
            start_url = f'https://www.yikm.net/{str(type_url)}'
            yield scrapy.Request(start_url,callback=self.type_list)

    def type_list(self, response):
        item = ScrapytestItem()
        #print(response.request.headers['User-Agent'])
        next_url_data = response.xpath("/html/body/article/nav[2]/ul/li[2]/a/@href").extract_first()
        data_all = response.xpath("//div[@class='row']/div[@class='col-md-3 col-xs-6']")
        none = " "
        for i in data_all:
            play_url = i.xpath(".//a/@href").extract_first()
            play_imgurl = i.xpath(".//a//img[@class='img img-raised']/@src").extract_first()
            play_title = i.xpath(".//div[@class='table']/span/text()").extract()
            for title_all in play_title:
                all = title_all+none
            all+=all
            play_name = i.xpath(".//div[@class='table']/h4/a/text()").extract_first()
            item['游戏地址'] = (f'https://www.yikm.net{play_url}', )
            item['游戏名字'] =  play_name,
            item['游戏类型'] =  all,
            item['游戏图片'] = play_imgurl
            yield item
            if next_url_data is not "#":
                next_url = f'https://www.yikm.net{next_url_data}'
                next_url = urllib.parse.urljoin(response.url,next_url)
                yield scrapy.Request(next_url,callback=self.type_list,meta={'item': item})


