import scrapy
import re
from Webscraper.items import Cebrennus_articles


class CebrennusSpider(scrapy.Spider):
    name = "Cebrennus"
    allowed_domains = ["krebsonsecurity.com"]
    start_urls = ["https://krebsonsecurity.com/page/1/"]
    page_count = 2

    custom_settings = {
        "FEED_EXPORT_FIELDS": ["Link", "Title", "Timestamp"],
    }

    def parse(self, response):
        posts = response.css("article.post")

        for post in posts:
            articles = Cebrennus_articles()

            articles["Link"] = (post.css("h2 a ::attr(href)").get(),)
            articles["Title"] = (post.css("h2 a ::text").get(),)
            # articles['Description'] = re.sub(r'<.*?>','',post.css('div p').get()),
            articles["Timestamp"] = (post.css(".date ::text").get(),)
            yield articles

        # Page Crawler
        pages = response.css("div.pagination ul li")
        total_page = int(pages[len(pages) - 2].css("a ::text").get())
        next_page_url = f"https://krebsonsecurity.com/page/{self.page_count}/"
        if self.page_count <= total_page:
            self.page_count += 1
            yield response.follow(next_page_url, callback=self.parse)
