from urllib import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'html.parser')

for  child in bsObj.find("table",{"id":"giftList"}).children:
    print child

two_attrs_tag = bsObj.findAll(lambda tag: len(tag.attrs)==2)
print 1
for tag in two_attrs_tag:
    print tag
