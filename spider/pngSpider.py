# coding =utf-8
import re
import urllib.request

from elasticsearch import Elasticsearch


def get_html(url):
    # 打开页面
    page = urllib.request.urlopen(url)
    # 获取目标页面的源码
    html = page.read()
    return html

def get_img(html):
    reg = 'data-original="(.+?\.jpg)"'
    reg_name = '<span class="name">([^<>]+)</span>'
    img = re.compile(reg)
    name = re.compile(reg_name)
    html = html.decode('utf-8')
    img_list = re.findall(img, html)
    name_list = re.findall(name, html)
    if len(name_list) > 0:
        es = Elasticsearch("119.29.175.113:9200")

        for i in range(len(name_list)):
            tmp_img = img_list[i]
            tmp_name = name_list[i]
            print(tmp_name+" ===>  "+tmp_img)
            es.index(index="house", doc_type="img", body={"hosueName": tmp_name, "imgUrl": tmp_img}, id=None)
