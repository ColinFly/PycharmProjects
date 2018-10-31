# coding:utf8
import urllib2
import os
import sys


class Outputer(object):
    def __init__(self):
        # 收集的数据是一个列表
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<head>")
        fout.write("<meta charset=\"UTF-8\">")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table border=\"1\">")
        # ascii
        for data in self.datas:
            fout.write("<tr>")
            # fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    @staticmethod
    def collect_data2(url):
        if url is None:
            return
        os.chdir("/home/colin/Desktop/WallPaper")
        os.getcwd()
        f = urllib2.urlopen(url)
        name = url.split('/')[-5]
        file_type = url.split('/')[-3]
        file_name = name + "." + file_type
        print file_name
        with open(file_name, "wb") as code:
            code.write(f.read())
            code.close()
