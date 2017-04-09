import scrapy

class QuotesSpider(scrapy.Spider):
    name = "gamespot"
    start_urls = [
        'https://www.gamespot.com/'
    ]
    
    def parse(self, response):
        base_url = 'https://www.gamespot.com'
        for article in response.css('article'):
            yield {
                'title': article.css('a div h3::text').extract_first(),
                'image': article.css('a figure div.media-img img').xpath('@src').extract_first(),
                'votes': article.css('a figure div.media-type span span::text').extract_first(),
                'link': base_url + article.css('a').xpath('@href').extract_first(),
                'summary': article.css('a div p::text').extract_first()
            }