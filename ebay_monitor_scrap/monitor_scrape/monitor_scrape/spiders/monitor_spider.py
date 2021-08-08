import scrapy

class MonitorSpider(scrapy.Spider):
    name = 'monitor'

    def start_requests(self):
        urls = [
            'https://www.ebay.com/b/Computer-Monitors/80053/bn_317528'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")
        # filename = f'{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')

        for monitor in response.css('div.s-item__info clearfix'):
            yield {
                'name': monitor.css('h3.s-item__title s-item__title--has-tags::txt').get(),
                'price': monitor.css('span.s-item__price::txt').get()
            } 