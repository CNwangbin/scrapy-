# Scrapy settings for tenholes project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import datetime

BOT_NAME = 'tenholes'

SPIDER_MODULES = ['tenholes.spiders']
NEWSPIDER_MODULE = 'tenholes.spiders'
now = datetime.datetime.now()
log_file_path = './log/scrapy{}-{}-{} {}_{}_{}.log'.format(now.year,now.month,now.day,now.hour,now.minute,now.second)
LOG_FILE = log_file_path
LOG_LEVEL = "WARNING"
# Crawl responsibly by identifying yourself (and your website) on the user-agent


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3870.400 QQBrowser/10.8.4405.400',
    "cookie":'_csrf-frontend=f37af85a7ac478f69da3a62214d68ad987cc41259250a59b74466f6cb0b8eff1a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22XWalSooZLMYDXRN_HDaYMwLljl_4Nv8n%22%3B%7D; Hm_lvt_2f7f7866ed2b0addd933476e1018bb2a=1626331672; ten_auth1=5P4Tab2eqqR6XTWbjKbKXjU1NTEzY2E3MGM4OTI3Mzk3ZTBjOTQwMGIwNGUyOTU3NzU5YjFiYjRlMzAzNTIxMWJhYzRhZDlmODdhMDNjZjnbeLUVB%2BE53LhOsyp7DiBETF1DAwrZNhDz5RDnh0GN2Pvp19sLDV0%2FX19hz3ahZNjpj31ASVADDYexrmOelS6M; 4475797num=1; Hm_lpvt_2f7f7866ed2b0addd933476e1018bb2a=1626331688'

}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tenholes.middlewares.TenholesSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tenholes.middlewares.TenholesDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'tenholes.pipelines.TenholesPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
