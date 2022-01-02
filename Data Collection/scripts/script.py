import requests
from scrapy import Selector

url='https://en.wikipedia.org/wiki/Web_scraping'
html_doc=requests.get(url).content

sel=Selector(text=html_doc)

for p in sel.xpath("//p"):
    print(p.xpath("text()").extract())