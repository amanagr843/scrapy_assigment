import scrapy
from scrapy_splash import SplashRequest
class Myspider(scrapy.Spider):
    name  = 'myspider'
    def start_requests(self):
        yield SplashRequest(
            url = 'https://in.seamsfriendly.com/',
            callback = self.parse
        )
    def parse(self,response):
        for item in list(response.css('div.ProductItem__Wrapper')):
            image_urls = []
            for w in item.css('a.ProductItem__ImageWrapper > div > img').attrib['data-widths'].replace('[','').replace(']','').split(","):
                image_urls.append(item.css('a.ProductItem__ImageWrapper > div > img').attrib['data-src'][2:].replace('{width}',w))
            yield { 
                'image-urls' : image_urls,
                'title' : item.css('h2.ProductItem__Title > a::text').get(),
                'price' : item.css('span.ProductItem__Price::text').get().replace("₹",""),
            }