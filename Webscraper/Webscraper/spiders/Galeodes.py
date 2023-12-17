import scrapy
from Webscraper.items import Galeodes_articles

class GaleodesSpider(scrapy.Spider):
    name = "Galeodes"
    allowed_domains = ["www.wired.com"]
    start_urls = ["https://www.wired.com/tag/cybersecurity/"]
    page_count = 2

    custom_settings = {
        "FEED_EXPORT_FIELDS": ["Link", "Title", "Timestamp"],
        "DOWNLOADER_MIDDLEWARES": {
            "Webscraper.middlewares.CebrennusMiddleware": 400,
        },
        "ITEM_PIPELINES" : {
            "Webscraper.pipelines.GaleodesPipeline": 200,
        },
    }

    def parse(self, response):
        posts = response.css(".summary-item__content")

        for post in posts:
            articles = Galeodes_articles()

            scraped_link = "https://www.wired.com" + post.css(".summary-item__hed-link ::attr(href)").get()
            articles["Link"] = scraped_link
            articles["Title"] = post.css(".summary-item__hed ::text").get()

            # Make a request to get the timestamp
            yield scrapy.Request(scraped_link, callback=self.extract_timestamp, meta={'item': articles.copy()})


        total_page = 50
        next_page_url = f"https://www.wired.com/tag/cybersecurity/?page={self.page_count}/"
        if self.page_count <= total_page:
            self.page_count += 1
            yield response.follow(next_page_url, callback=self.parse)


    def extract_timestamp(self, response):
        # Extract timestamp and retrieve the item from the meta
        time = response.css("time ::text").get()
        articles = response.meta['item']
        articles["Timestamp"] = time
        yield articles

