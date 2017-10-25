import scrapy
import urllib
import datetime


class QuotesSpider(scrapy.spiders.Spider):
     name = "flikr_f"

     def start_requests(self):
         now = datetime.datetime.now()
         url_format = 'https://www.flickr.com/explore/{}/{}/{}'

         for i in range(1,2000):
             new_date = now - datetime.timedelta(days=i)
             new_date = datetime.date.isoformat(new_date).split('-')
             print new_date
            #  print url_format.format(new_date.day)
             if new_date[1]<10 and new_datep[2]<10:
                url = url_format.format(new_date[0], '0'+ new_date[1], '0'+ new_date[2])
             elif new_date[1]<10:
                url = url_format.format(new_date[0], '0'+ new_date[1], new_date[2])
             elif new_date[2]<10:
                url = url_format.format(new_date[0], new_date[1], '0'+new_date[2])
             else:
                url = url_format.format(new_date[0], new_date[1], new_date[2])

             print url
             yield scrapy.Request(url=url, callback=self.parse, errback=self.errorCallback)
     def errorCallback(self, err):
         print "Error"
         print err
     def parse(self, response):

         page = response.url.split("/")[-1]
        #
        #  print "url :"+response.url
         print page
         res = response.body

         lines = res.split("\n")
        #  print len(lines)
         imgs = []
         for line in lines :
             index = line.find("img.src='")
             if index != -1:
                 imgs.append(line[index+11:-2])
        #  print len(imgs)

         for img in imgs:
             filename = "imgs/"+img.split('/')[-1]
            #  print filename
             self.log("saving image %s"%filename)
             urllib.urlretrieve("http://"+img, filename)
