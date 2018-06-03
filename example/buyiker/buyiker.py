#coding=utf-8

from xspider.spider.spider import BaseSpider
from xspider.filters import UrlFilter
from xspider.processor import PageProcessor
from xspider.selector import XPathSelector
from xspider.filters.CrawledFilter import SimpleCrawledFilter
from xspider import model
from b2 import system2
system2.reload_utf8()


class BuYiKr(PageProcessor.PageProcessor):
    def __init__(self):
        super(BuYiKr, self).__init__()
        self.title_extractor = XPathSelector.XpathSelector(
            path="//title/text()")

    def process(self, page, spider):
        items = model.fileds.Fileds()
        items["title"] = self.title_extractor.find(page)
        items["url"] = page.url
        yield items


if __name__ == "__main__":
    spider = BaseSpider(
        name="buyikr",
        crawled_filter=SimpleCrawledFilter(),
        page_processor=BuYiKr(),
        allow_site=["buyikr.com"],
        start_urls=["http://buyikr.com/"])
    spider.start()
