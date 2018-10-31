# coding:utf8
from wallpaper.spider import url_manager, html_downloader, html_parser, html_outputer

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
        # while self.urls.has_new_url():
        try:
            new_url = self.urls.get_new_url()
            print 'craw %d : %s ' % (count, new_url)
            html_content = self.downloader.download(new_url)
            new_urls = self.parser.parse(new_url, html_content)
            for sub_new_url in new_urls:
                sub_html_content = self.downloader.download(sub_new_url)
                download_url = self.parser.parse2(sub_html_content)
                self.outputer.collect_data2(download_url)
        except:
            print'craw failed'


if __name__ == "__main__":
    root_url = "https://wall.alphacoders.com/highest_rated.php"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
