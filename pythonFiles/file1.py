from urllib import request, parse
import ssl
import _thread
from bs4 import BeautifulSoup
import _thread
import time
from helper import removeAdditionString, writeDataToDB

class Detail():
    def __init__(self, search_key, valueId):
        self.search_key = search_key
        self.valueId = valueId
        self.lock = _thread.allocate_lock()
        self.fetchData()
        # _thread.start_new_thread(self.fetchData, ())
        
    def fetchData(self):
        self.lock.acquire()
        file = open('data2.txt', 'a+')
        detailParams = parse.urlencode([
            ('ckm_id', self.valueId),
            ('ckm_index', '1'),
            ('sort', 'desc',),
            ('sort2', 'desc'),
            ('rule', 'CTR'),
            ('currentpage', '1'),
            ('pagesize', '20'),
            ('keywords', self.search_key),
            ('reg_no', 'CTR')
        ])
        detailReq = request.Request('http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlistdetail')
        detailReq.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
        detailReq.add_header('Accept-Encoding', 'gzip, deflate')
        detailReq.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
        detailReq.add_header('Cache-Control', 'no-cache')
        detailReq.add_header('Connection', 'keep-alive')
        detailReq.add_header('Content-Length', '221')
        detailReq.add_header('Content-Type', 'application/x-www-form-urlencoded')
        detailReq.add_header('Cookie', 'UM_distinctid=165f0dac1f763b-05e54b89f50362-1033685c-1fa400-165f0dac1f8108; JSESSIONID=0000TJ-FwSxf0paIsvWARcn7SL5:-1; CNZZDATA1256895572=486339531-1537339234-%7C1537945886')
        detailReq.add_header('Host', 'www.chinadrugtrials.org.cn')
        detailReq.add_header('Origin', 'http://www.chinadrugtrials.org.cn')
        detailReq.add_header('Pragma', 'no-cache')
        detailReq.add_header('Referer', 'http://www.chinadrugtrials.org.cn/eap/clinicaltrials.searchlist')
        detailReq.add_header('Upgrade-Insecure-Requests', '1')
        detailReq.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36')

        with request.urlopen(detailReq, data=detailParams.encode('utf-8')) as f:
            data = f.read()

        detailSoup = BeautifulSoup(data.decode('utf-8'), features="html.parser")

        marginAutoList = detailSoup.select('table[style="margin:auto"]')
        marginAutotList = detailSoup.select('table[style="margin:auto;"]')
        contactInfoList = detailSoup.select('td[bgcolor="#FFFFFF"]')
        organizationList = detailSoup.select('table[id="hspTable"]')
        standardList = detailSoup.select('table[id="stTable"]')
        detail = {}
        detail['id'] = '7f0d60c4f0424d679127f918b4be7388'
        for index,value in enumerate(marginAutoList):
            for detailIndex,detailObject in enumerate(value.find_all('td')):
                if index == 0:
                    if detailIndex == 1:
                        file.write(str(removeAdditionString(detailObject.string)))
                    if detailIndex == 3:
                        detail['indication'] = removeAdditionString(detailObject.string)
                    if detailIndex == 5:
                        detail['test_popular_title'] = removeAdditionString(detailObject.string)
                    if detailIndex == 7:
                        detail['test_profession_title'] = removeAdditionString(detailObject.string)
                    if detailIndex == 9:
                        detail['scheme_number'] = removeAdditionString(detailObject.string)
                    if detailIndex == 13:
                        detail['drug_name'] = removeAdditionString(detailObject.string)
                    if detailIndex == 15:
                        detail['drug_type'] = removeAdditionString(detailObject.string)

                if index == 2:
                    #试验终止日期
                    detail['test_end_date'] = removeAdditionString(detailObject.string)
        for index,value in enumerate(marginAutotList):
            if index == 3:
                for detailIndex,detailObject in enumerate(value.find_all('td')):
                    if index == 3:
                        #试验状态
                        detail['test_status'] = removeAdditionString(detailObject.string)
                        break
        for index,value in enumerate(contactInfoList):
            #申办者信息
            if index == 13:
                detail['contact'] = removeAdditionString(value.string)
            if index == 15:
                detail['contact_phone'] = removeAdditionString(value.string)
                break

        organizationLists = []
        enterStandrdLists = []
        defuseStandardLists = []
        organizationInfo = {}
        for index,value in enumerate(organizationList[0].find_all('td')):
            if index > 5:
                if index % 6 == 0:
                    organizationInfo['num'] = removeAdditionString(value.string)
                if index % 6 == 1:
                    organizationInfo['organization_name'] = removeAdditionString(value.string)
                if index % 6 == 4:
                    organizationInfo['province'] = removeAdditionString(value.string)
                if index % 6 == 5:
                    organizationInfo['city'] = removeAdditionString(value.string)
                    organizationLists.append(organizationInfo)
                    organizationInfo = {}

        file.write('哈哈哈1')
        for index,value in enumerate(standardList):
            standard = {}
            print('2')
            for detailIndex,listDetail in enumerate(value.find_all('td')):
                print('1' + str(detailIndex) + '\n' + str(listDetail))
                if detailIndex % 2 == 0:
                    standard['num'] = removeAdditionString(listDetail.string)
                if detailIndex % 2 == 1:
                    standard['content'] = removeAdditionString(listDetail.string)
                    if index == 0 :
                        enterStandrdLists.append(standard)
                    else:
                        defuseStandardLists.append(standard)
                    standard ={}
        file.write('哈哈哈2')
        # detail['search_content_type'] = self.search_key
        # detail['organizationLists'] = organizationLists 
        # detail['enterStandrdLists'] = enterStandrdLists   
        # detail['defuseStandardLists'] = defuseStandardLists  
        # file.write(str(detail))
        # file.close()

        # writeDataToDB(detail)
        # #各参加机构信息
        # self.lock.release()


detail = Detail('糖尿病', '7f0d60c4f0424d679127f918b4be7388')
