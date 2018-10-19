from spider.pngSpider import get_html
from spider.pngSpider import get_img

if __name__ == "__main__":
    html = get_html("https://cd.fang.ke.com/loupan/tianfuxinqunanqu")
    get_img(html)
