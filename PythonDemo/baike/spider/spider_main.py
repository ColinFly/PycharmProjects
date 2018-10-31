# coding:utf8
from baike.spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    # 初始化各种对象
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.Outputer()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s ' % (count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
                count = count + 1
            except:
                print'craw failed'
            self.outputer.output_html()


if __name__ == "__main__":
    # root_url = "https://baike.baidu.com/item/Python/407313"
    # root_url = "https://baike.baidu.com/item/中国城市新分级名单"
    root_url = "https://baike.baidu.com/item/上海/114606"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
