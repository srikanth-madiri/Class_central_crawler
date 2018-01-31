# Class_central_crawler
This crawler points to the "https://www.class-central.com/subjects"  page which has departments and domains and it in turn goes to each of these departments. Then finds the domains of each department and further crawls to each of the courses that a domain provides and also gets you the url for each course and stores the department along with course name and respective url into in CSV file or into a json format file.     


How to run ?

$ scrapy crawl subjects 

--gets you the output right on the terminal

$ scrapy crawl subjects -o file_name.csv

--the complete scrapped data is written into "file_name.csv" file which makes to appear pretty human readable

$ scrapy crawl subjects -o file_name.json

--the complete scrapped data is written into "file_name.json" file which which gives you a json formatted data
