import scrapy
import re
from Webscraper.items import Cebrennus_articles

class CebrennusSpider(scrapy.Spider):
    name = "Cebrennus"
    allowed_domains = ["krebsonsecurity.com"]
    start_urls = ["https://krebsonsecurity.com/page/1/"]
    page_count = 2

    custom_settings = {
        "FEED_EXPORT_FIELDS": ["Link", "Img_URL", "Title", "Source", "Timestamp"],
        "ITEM_PIPELINES" : {
            "Webscraper.pipelines.CebrennusPipeline": 200,
        },
    }

    def parse(self, response):
        # Extracting information from each post on the page
        posts = response.css("article.post")
        for post in posts:
            articles = Cebrennus_articles()

            # Extracting link, image URL, title, timestamp from each post and assigning values to the Cebrennus_articles item
            articles["Link"] = post.css("h2 a ::attr(href)").get()
            articles["Img_URL"] = post.css('img[decoding="async"] ::attr(src)').get()
            articles["Title"] = post.css("h2 a ::text").get()
            articles["Source"] = "KrebsonSecurity"
            # articles['Description'] = re.sub(r'<.*?>','',post.css('div p').get())
            articles["Timestamp"] = post.css(".date ::text").get()
            yield articles

        # page crawler
        # Extracting total number of pages and navigating to the next page if available
        # pages = response.css("div.pagination ul li")
        # total_page = int(pages[len(pages) - 2].css("a ::text").get())
        total_page = 2
        next_page_url = f"https://krebsonsecurity.com/page/{self.page_count}/"
        if self.page_count <= total_page:
            self.page_count += 1
            yield response.follow(next_page_url, callback=self.parse)
