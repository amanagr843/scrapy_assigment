# scrapy_assigment

This is the scrapy assignment . Please follow the below steps to generate csv file
1. python3 -m venv newenv
2. source newenv/bin/activate
3. pip3 install -r requirements.txt
4. docker run -p 8050:8050 scrapinghub/splash
5. scrapy crawl myspider -O items.csv -t csv
