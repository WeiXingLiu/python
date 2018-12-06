import ssl
import re
import _thread
from urllib import request, parse
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def get_ip_list():
    #获取代理IP（取当前页的ip列表，每页100条ip）
    url = "http://www.xicidaili.com/nn"
    req = request.Request(url)
    req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;")
    # req.add_header("Accept-Encoding", "gzip, deflate, sdch")
    req.add_header("Accept-Language", "zh-CN,zh;q=0.8,en;q=0.6")
    req.add_header("Referer", "http://www.xicidaili.com")
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36")
    with request.urlopen(req) as f:
            data = f.read()
            print(data)

    soup = BeautifulSoup(data.decode('utf-8'), features="html.parser")
    # soup = bs4.BeautifulSoup(r.text, 'html.parser')
    data = soup.table.find_all("td")
    # 匹配规则需要用浏览器的开发者工具进行查看
    #匹配协议
    protocol_compile = re.compile(r'<td>(http+)</td>')
    # 匹配IP：<td>61.135.217.7</td>
    ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')
    # 匹配端口：<td>80</td>
    port_compile = re.compile(r'<td>(\d+)</td>')   

    protocol = re.findall(protocol_compile,str(data))     
    # 获取所有IP，返回的是数组[]
    ip = re.findall(ip_compile,str(data))     
    # 获取所有端口：返回的是数组[]  
    port = re.findall(port_compile,str(data))   
    # 组合IP+端口，如：61.135.217.7:80
    return [":".join(i) for i in zip(ip,port)] 

print(get_ip_list())

def validIp():
    url = 'https://www.qidian.com/rank/hotsales' 
    # for value in list:
    try:
        proxy = {'http': '10.168.30.96:80'}
        proxy_support =request.ProxyHandler(proxy)
        opener=request.build_opener(proxy_support)
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
        request.install_opener(opener)
        html=request.urlopen(url).read().decode('utf-8')

        # host = {'http': '10.168.30.96'}
        # support = request.ProxyHandler(host)
        # opener = request.build_opener(support)
        # opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
        # request.install_opener(opener)
        # html = request.urlopen(url).read().decode('utf-8')
        return html
    except:
        return 'error'

print(validIp())