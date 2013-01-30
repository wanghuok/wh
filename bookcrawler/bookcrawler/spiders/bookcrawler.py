#encoding:utf-8
from scrapy.http import Request, Response, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector

class BookCrawler(CrawlSpider):
    name = 'sslib'
    allowed_domains = ['sslibrary.com']
    start_urls = ['http://edu.sslibrary.com/userlogon.jsp']
    
    def parse(self, response):
        #return [FormRequest.from_response(response, formdata={'send':'true', 'UserName':'zjgsdx', 'PassWord':'zjgsdx','rd':'0', 'Submit3322':'%B5%C7%C2%BC','backurl':''},callback=self.after_login)]
        return [FormRequest(url = 'http://edu.sslibrary.com/loginhl.jsp', formdata={'send':'true', 'UserName':'zjgsdx', 'PassWord':'zjgsdx','rd':'0', 'Submit3322':'%B5%C7%C2%BC','backurl':''},callback=self.after_login)]
    
    def after_login(self, response):
        return Request(url='http://edu.sslibrary.com/booksContent.jsp?searchmark=&fenleiID=0A&Pages=1&Sort=0', callback = self.parse_booklist)
    
    def parse_booklist(self, response):
        hxs = HtmlXPathSelector(response)
        print '***************'
        #得到页码数
        print hxs.select('//html/body/table[2]/tr[1]/td/font[3]/text()').extract()
        #print hxs.select('//form[0]/textarea/text()').extract()
        print hxs.select('//html/body/table[3]/tbody/tr[1]/td[3]/span/a/span/text()').extract()
#        fp = "c:/out.html"
#        f = open(fp, 'w')
#        f.write(response.body)
#        f.close()
        #print response.body