# Scrapy settings for bookcrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'bookcrawler'

SPIDER_MODULES = ['bookcrawler.spiders']
NEWSPIDER_MODULE = 'bookcrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bookcrawler (+http://www.yourdomain.com)'
