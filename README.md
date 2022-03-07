# scrapy_assigment

This is the scrapy assignment . Please follow the below steps to generate csv file
1. pip3 install -r requirements.txt
2. docker run -p 8050:8050 scrapinghub/splash
3. scrapy crawl myspider -O items.csv -t csv
