# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 18:17:42 2018

@author: Noah Data
"""
import scrapy
import requests
#import urllib2
#from scrapy import Selector
class CCN(scrapy.Spider):
    name="ccn"
    def start_requests(self):
        
        headers={"content-type":"application/x-www-form-urlencoded; charset=UTF-8","user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}


        for page in range(1,100000):
            data={"action":"loadmore","page":page}
            url="https://www.ccn.com/wp-admin/admin-ajax.php"
            req=requests.post(url,data=data,headers=headers)
            yield scrapy.Request(req.content,callback=self.parse)


            
            
            
    def parse(self,response):
       for new in response.css("h4.entry-title font-weight-bold"):
            link=str(new.css(" a::attr(href)").extract_first())
            print(link)
            
#            yield scrapy.Request(link,callback=self.parse_content) 
#            
#    def parse_content(self,response):
#        res=response.body
#        url=response.url
#      
#        title=Selector(text=res).xpath("//h1[@class='entry-title'/text()").extract_first()
#       # print(title)
#        
#        
#        author=response.xpath("//div[@class='hero-date']/a[position()=2]/text() ").extract()
#        str1 = ""
#        for a in author:
#            str1 = a.strip()
#
#        
#        content =response.xpath("//div[@class='entry-content']/p/text()").extract()
#        if content:
#            para=("").join(content).replace('\n',' ').replace(',','').encode('utf-8').strip()
#            #print(para)
#           
#        df = pd.DataFrame({'TITLE':title,"AUTHOR":str1,"CONTENT":para,"LINKS":url},index=[0])
##        print(df.head())
#        
#        df.to_csv('p.csv',mode='a', encoding='utf-8',header=False)
#    
#if __name__=="__main__":
#    process=CrawlerProcess({
#            'mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#            })
#    process.crawl(NewsSpider)
#    process.start()
#            
#
#
