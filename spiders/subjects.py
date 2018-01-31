# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request


class SubjectsSpider(Spider):
    name = 'subjects'
    allowed_domains = ['class-central.com']
    start_urls = ['http://class-central.com/subjects']

    def __init__(self, subject=None):
    	self.subject = subject

    def parse(self, response):
        if self.subject:
        	subject_url = response.xpath('//*[contains(@title, "'+ self.subject +'")]/@href').extract_first()
        	yield Request(response.urljoin(subject_url), callback=self.class_parse)

        else:
        	all_subject_urls = response.xpath('//*[@class="show-all-subjects view-all-courses"]/@href').extract()
        	for sub in all_subject_urls:
        		yield Request(response.urljoin(sub), callback=self.class_parse)

    def class_parse(self, response):
    	subject_name = response.xpath('//title/text()').extract_first()
    	subject_name = subject_name.split(' | ')
    	subject_name = subject_name[0]

    	courses = response.xpath('//*[@class="text--charcoal text-2 medium-up-text-1 block course-name"]')
    	for course in courses:
    		course_name = course.xpath('.//@title').extract_first()
    		course_url = course.xpath('.//@href').extract_first()
    		absolute_course_url = response.urljoin(course_url)

    		yield{
    			'subject_name': subject_name,
    			'course_name' : course_name ,
    			'course_url' : absolute_course_url
    		}

    	next_page_url = response.xpath('//*[@rel="next"]/@href').extract_first()
    	absolute_next_page_url = response.urljoin(next_page_url)
    	yield Request(absolute_next_page_url, callback=self.class_parse)