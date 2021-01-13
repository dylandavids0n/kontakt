import scrapy
import re
import pandas as pd
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class EmailSpider(scrapy.Spider):
    name = "emails"

    def start_requests(self):
        urls = [
            'https://www.cwthomas.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        links = LxmlLinkExtractor(allow=()).extract_links(response)
        links = [str(link.url) for link in links]
        links.append(str(response.url))
        
        for link in links:
            yield scrapy.Request(url=link, callback=self.parse_link) 
            
    def parse_link(self, response):
        
        for word in self.reject:
            if word in str(response.url):
                return
            
        html_text = str(response.text)        
        mail_list = re.findall('\w+@\w+\.{1}\w+', html_text)

        dic = {'email': mail_list, 'link': str(response.url)}
        df = pd.DataFrame(dic)
        
        df.to_csv(self.path, mode='a', header=False)
        df.to_csv(self.path, mode='a', header=False)