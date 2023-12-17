import scrapy
from Webscraper.items import Hyptiotes_articles


class HyptiotesSpider(scrapy.Spider):
    name = "Hyptiotes"
    allowed_domains = ["thehackernews.com"]
    start_urls = ["https://thehackernews.com/"]
    page_count = 1

    custom_settings = {
        "FEED_EXPORT_FIELDS": ["Link", "Title", "Timestamp"],
        "DOWNLOADER_MIDDLEWARES": {
            "Webscraper.middlewares.CebrennusMiddleware": 400,
        },
    }

    def parse(self, response):
        posts = response.css(".body-post")

        for post in posts:
            articles = Hyptiotes_articles()

            articles["Link"] = (post.css(".story-link ::attr(href)").get(),)
            articles["Title"] = (post.css(".home-title ::text").get(),)
            articles["Timestamp"] = (post.xpath('//span[@class="h-datetime"]/i/following-sibling::text()').get().strip(),)
            yield articles

        next_page_url = response.css(".blog-pager-older-link-mobile ::attr(href)").get()
        if self.page_count <= 100:
            self.page_count += 1
            yield response.follow(next_page_url, callback=self.parse)
