# coding:utf8
import urlparse
from bs4 import BeautifulSoup

import re


class HtmlParser(object):
    def parse2(self, sub_html_content):
        if sub_html_content is None:
            return
        soup = BeautifulSoup(sub_html_content, 'html.parser', from_encoding='utf-8')
        new_data = self._get_new_data(soup)
        return new_data

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls

    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = set()
        # < a href = "big.php?i=367839" title = "Video Game Minecraft HD Wallpaper | Background Image" >
        links = soup.find_all('a', href=re.compile(r"big\.php\?"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            print "new_full_url: " + new_full_url
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    def _get_new_data(soup):
        # 字典存储信息(键值对)
        res_url = set()
        # url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        class_attr = soup.find('span', class_="btn btn-success btn-custom download-button")
        data_id = class_attr['data-id']
        data_type = class_attr['data-type']
        data_server = class_attr['data-server']
        data_user_id = class_attr['data-user-id']
        base_url = "https://initiate.alphacoders.com/download/"
        dir = "wallpaper"
        random = "655222636164078"
        params = dir + '/' + data_id + '/' + data_server + '/' + data_type + '/' + random + '/' + data_user_id
        full_url = urlparse.urljoin(base_url, params)
        print full_url
        res_url.add(full_url)
        return full_url
