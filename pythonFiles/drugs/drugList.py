import ssl
import _thread
from urllib import request, parse
from bs4 import BeautifulSoup
from detail import Detail
from concurrent.futures import ThreadPoolExecutor

class List:
    def __init__(self, search_key):
        self.search_key = search_key
        self.page = 1
        self.lock = _thread.allocate_lock()

    def begin(self):
        params = parse.urlencode([
            ('sort', 'desc',),
            ('sort2', 'desc'),
            ('rule', 'CTR'),
            ('currentpage', self.page),
            ('pagesize', '40'),
            ('keywords', self.search_key),
            ('reg_no', 'CTR')
        ])

        req = request.Request('http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlist')
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
        tables = soup.select('a[onclick="getDetail(this.id)"]')
        totalPage = soup.select('a[style="color:#F00"]')

        self.page += 1

        drugObject = {}
        drusObjects = []
        executor = ThreadPoolExecutor(max_workers = 3)
        for index,value in enumerate(tables): 
            if index % 5 == 0:
                future = executor.submit(self._fetch_detail, value['id'])
        return totalPage[0].string == totalPage[1].string

    def _fetch_detail(self, valueId):
            Detail(self.search_key, valueId)
