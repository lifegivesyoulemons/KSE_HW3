import scrapy

class JeansSpider(scrapy.Spider):
    name = 'jeans'
    allowed_domains = ['obozrevatel.com', 'segodnya.ua', '24tv.ua', 'tsn.ua',
                      'strana.ua', 'pravda.com.ua', 'rbc.ua', 'unian.com',
                      'gordonua.com', 'nv.ua', 'liga.net', 'censor.net.ua',
                      'censor.net', '112.ua', 'korrespondent.net', 'unian.ua',
                      'unian.net', 'imi.org.ua', 'znaj.ua', 'ukranews.com',
                      'politeka.net', 'interfax.com.ua', 'apostrophe.ua',
                      'unn.com.ua', 'bagnet.org', 'kp.ua', 
                     ]
    start_urls = [
        f'https://imi.org.ua/monitoring-types/doslidzhennya-dzhynsy/page/{i}/'
        for i in range(1, 3)
    ]

    def parse(self, response):
        for href in response.css('article a.standart__post::attr(href)'):
            yield scrapy.Request(href.extract(), callback=self.parse_imi)

    def parse_imi(self, response):
        for href in response.css('.inner__container a::attr(href)'):
            yield scrapy.Request(href.extract(), callback=self.parse_news)
      
    def parse_news(self, response):
        yield {
            'link': response.request.url,
            'html': response.text,
        }