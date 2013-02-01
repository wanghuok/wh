#encoding:utf-8
from scrapy.http import Request, Response, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.shell import inspect_response
from scrapy.contrib.closespider import CloseSpider
from bookcrawler.items import BookcrawlerItem
import sys

class BookCrawler(CrawlSpider):
    name = 'sslib'
    allowed_domains = ['sslibrary.com']
    start_urls = ['http://edu.sslibrary.com/userlogon.jsp']
    
    def __init__(self):
        self.num = 1
        self.urlp = 'http://edu.sslibrary.com/booksContent.jsp?searchmark=&fenleiID=0A&Pages='
        self.urls = '&Sort=0'
        self.fp = open('/home/wh/work/wh/bookcrawler/a', 'a') 
    
    
    def parse(self, response):
        return [FormRequest(url = 'http://edu.sslibrary.com/loginhl.jsp', formdata={'send':'true', 'UserName':'zjgsdx', 'PassWord':'zjgsdx','rd':'0', 'Submit3322':'%B5%C7%C2%BC','backurl':''},callback=self.after_login)]
    
    def after_login(self, response):
        turl='%s%d%s' % (self.urlp, self.num, self.urls)
        print turl
        #return Request(url='http://edu.sslibrary.com/booksContent.jsp?searchmark=&fenleiID=0A&Pages=1&Sort=0', callback = self.parse_booklist)
        return Request(url=turl, callback = self.parse_booklist)
    
    def parse_booklist(self, response):
        myitems = []
        hxs = HtmlXPathSelector(response)
#        inspect_response(response)
        #得到页码数
#        print hxs.select('//html/body/table[2]/tr[1]/td/font[3]/text()').extract()
        cont = hxs.select('//form/textarea/div/text()').extract_unquoted()
        src = hxs.select('//*[@id="bb"]/a/img/@src').extract()
#        print 'size=%d\n' % (len(tmp),)
#        self.fp.writelines(tmp[0].encode('utf-8'))

        for x in src:
            myitem = BookcrawlerItem()
            t = []
            t.append(x)
            myitem['image_urls'] = t
            yield myitem

#        self.fp.writelines([line.encode('utf-8')+'\n' for line in tmp])

        if self.num < 10:
            self.num += 1
            #raise CloseSpider(reason='***********enough*********')
            turl='%s%d%s' % (self.urlp, self.num, self.urls)
            yield Request(url=turl, callback = self.parse_booklist)