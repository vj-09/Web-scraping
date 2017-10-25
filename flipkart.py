import scrapy
import urllib
import re
import pandas as pd
# from bs4 import BeautifulSoup
from scrapy import Selector
class QuotesSpider(scrapy.spiders.Spider):
     name = "flipkart_f"

     def start_requests(self):
         urls = ['https://www.flipkart.com/sitemap?otracker=undefined_footer_navlinks'
             ]
         for url in urls:
             yield scrapy.Request(url=url, callback=self.parse)
     def parse(self, response):
         page = response.url.split("/")[-2]
         page = page[6:]
         res = response.body
         lines = res.split("\n")
         link = []
         for i,line in enumerate(lines):
             index = line.find('<h2>')
             if index != -1:
                 c = lines[i+1]
                 z = re.findall('"([^"]*)"', c)
                 link.append(z)
        #  print link
         del link[:5]

         for url in link:
             print "URl =>",
             print url
             yield scrapy.Request(url="https://www.flipkart.com"+url[0], callback=self.parse_next)

     def parse_next(self, response):
         res =  response.body
        #  #print res
        #  print "index",
        #  print res.find("_3v8VuN")
         temp = Selector(text=res).xpath('//span[@class="_3v8VuN"]/span/text()').extract()
         if len(temp) == 1:
             max_page = temp[0].split(' ')[-1]
             pages = int( "".join(max_page.split(',')))
             for i in range(1,5):
                 url = response.url + "&page="+str(i)
                #  print url
                 yield scrapy.Request(url=url, callback=self.parse_data)
            #  print max_page
        #  next_link = Selector(text=res).xpath('//div[@class="_2kUstJ"]/a/@href').extract()
        #  sub =
        #  print ################,
        #  print next_link
     def parse_data(self,response):
         res =response.body
         url = response.url
         print url,
         print '                                                  ##########'
        #  print res[1:15]
         product_name = Selector(text=res).xpath('//a[@class="_2cLu-l"]/text()').extract()
         product_rating = Selector(text=res).xpath('//div[@class="hGSR34 _2beYZw"]/text()').extract()
         product_rating = product_rating[::2]

         product_price = Selector(text=res).xpath('//div[@class="_1vC4OE"]/text()').extract()
         product_price = product_price[1::2]
        #  print len(product_name),len(product_rating)
        #  print product_name
        #  print product_price
         #
        #  print product_rating
         df = pd.DataFrame({'Name':product_name})
         df['Price'] = product_price
        #  df['Rating'] = product_rating
         print df
        #  print temp
