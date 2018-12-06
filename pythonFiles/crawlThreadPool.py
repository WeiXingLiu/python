import os
import re
from concurrent.futures import ThreadPoolExecutor
from urllib import request, parse
from bs4 import BeautifulSoup

class CrawlThreadPool(object):
    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(max_workers = 5)

    def _request_arse_runnable(self, url, params):
        try:
            req = request.Request(url)
            req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
            req.add_header('Accept-Encoding', 'gzip, deflate')
            req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
            req.add_header('Cache-Control', 'no-cache')
            req.add_header('Connection', 'keep-alive')
            req.add_header('Content-Length', '221')
            req.add_header('Content-Type', 'application/x-www-form-urlencoded')
            req.add_header('Cookie', 'UM_distinctid=165f0dac1f763b-05e54b89f50362-1033685c-1fa400-165f0dac1f8108; JSESSIONID=0000TJ-FwSxf0paIsvWARcn7SL5:-1; CNZZDATA1256895572=486339531-1537339234-%7C1537945886')
            req.add_header('Host', 'www.chinadrugtrials.org.cn')
            req.add_header('Origin', 'http://www.chinadrugtrials.org.cn')
            req.add_header('Pragma', 'no-cache')
            req.add_header('Referer', 'http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlist')
            req.add_header('Upgrade-Insecure-Requests', '1')
            req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36')
            with request.urlopen(req, data=params.encode('utf-8')) as f:
                data = f.read()
            soup = BeautifulSoup(data.decode('utf-8'), features="html.parser")
            return soup

    def crawl(self, url, params, complete_callback):
        future = self.thread_pool.submit(self._request_parse_runnable, url, params)
        future.add_done_callback(complete_callback)


class FetchDrugList(object):
    def __init__(self):
        self.thread_pool = ThreadPoolExecutor(max_workers = 5)

    def _output_runnable(self, crawl_result):
        print('crawl_result', crawl_result)
        try:
        # file = open('dataDetail9.txt', 'a+')
        # detailSoup = BeautifulSoup(data.decode('utf-8'), features="html.parser")
        # detailList = detailSoup.select('td[align="left"] td[height="30"]')

        # objectDetail = '{id:' + str(self.listObj['id']) + ', signId:' + str(self.listObj['signId']) + ', drugName:' + str(self.listObj['drugName']) + ', symptom:' + str(self.listObj['symptom']) + ', subject:' + str(self.listObj['subject'])
        # file.write(objectDetail.replace("\r","").replace("\n","").replace("\t","").replace(" ","") + '},\n')
        # file.close()

    def save(self, craw_result):
        self.thread_pool.submit(self._output_runnable, craw_result)

class CrawManager(object):
    def __init__(self):
        self.crawl_pool = CrawlThreadPool()
        self.output_pool = OutPutThreadPool()

    def _crawl_future_callback(self, crawl_url_future):
        try:
            data = crawl_url_future.result()
            print('data', data)
            for new_url in data['new_urls']:
                self.start_runner(new_url)
            self.output_pool.save(data)
        except Exception as e:
            print('Run crawl url future thread error. '+str(e))

    def start_runner(self, url, params):
        self.crawl_pool.crawl(url,params, self._crawl_future_callback)


if __name__ == '__main__':
    params = parse.urlencode([
            ('sort', 'desc',),
            ('sort2', 'desc'),
            ('rule', 'CTR'),
            ('currentpage', self.page),
            ('pagesize', '100'),
            ('keywords', self.search_key),
            ('reg_no', 'CTR')
        ])
    url = 'http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlist'
    CrawlManager().start_runner(url, params)
