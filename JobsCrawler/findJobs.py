# -*- coding:utf-8 -*-
'''
This is a rought implementation, results are not stored in the database.


TODO:
1. store the result as a structured dataset
2. multiprocessing: each page could be processed by one thread
'''

import requests
import json
from bs4 import BeautifulSoup
import time
import threading
import uuid

session = requests.Session()
def get_uuid():
    return str(uuid.uuid4())

cookie = "JSESSIONID=" + get_uuid() + ";" \
    "user_trace_token=" + get_uuid() + "; LGUID=" + get_uuid() + ";" \
    "SEARCH_ID=" + get_uuid() + '; _gid=GA1.2.717841549.1514043316; ' '_ga=GA1.2.952298646.1514043316; ' \
    'LGSID=' + get_uuid() + "; " + "LGRID=" + get_uuid() + "; "

headers = {
    'cookie': cookie,
    'origin': "https://www.lagou.com",
    'x-anit-forge-code': "0",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'referer': "https://www.lagou.com/jobs/list_python?px=new&city=%E6%88%90%E9%83%BD",
    'x-requested-with': "XMLHttpRequest",
    'connection': "keep-alive",
    'x-anit-forge-token': "None",
    'cache-control': "no-cache",
    'postman-token': "91beb456-8dd9-0390-a3a5-64ff3936fa63"
}    

def fetch_position_details(positionId):
    url = 'https://www.lagou.com/jobs/%s.html'%positionId
    res = session.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    try:
        # TODO: add your requirement for the job to the following 
        print(positionId)
        print(soup.find('dd', {'class':'job_bt'}).get_text())
        print(soup.find('dd', {'class':'job_request'}).get_text())
    except:
        return print('No job request')
    

def get_pages(keywords, city="全国"):
    '''
    type: keywords: the keyword you want to search
    rtype: totla_pages:int
    if the result is wired, the headers could be wrong
    '''
    url = "https://www.lagou.com/jobs/positionAjax.json"
    params = {"px": "new", "city": city, "needAddtionalResult": "false", "isSchoolJob": "0"}
    payload = "first=false&pn=1&kd=" +keywords
    res = session.post(url,params=params, data=payload, headers=headers)
    result = json.loads(res.text)
    totalCount = result['content']['positionResult']['totalCount']
    positions_per_page = result['content']['positionResult']['resultSize']
    return int(totalCount)//int(positions_per_page) + 1

def worker_fetcher(keywords, page, city="全国"):
    time.sleep(20)
    print('Processing the page %s'%page)
    url = "https://www.lagou.com/jobs/positionAjax.json"
    params = {"px": "new", "city": city, "needAddtionalResult": "false", "isSchoolJob": "0"}
    payloads={'first':'false','pn':str(page),'kd':keywords}

    res = session.post(url, data=payloads, headers=headers)
    json_response=json.loads(res.text)
    try:
        result=json_response['content']['positionResult']['result']
        for item in result:
            try:
                positionId = item['positionId']
                fetch_position_details(positionId)
            except:
                continue
    except:
        print("Error parsing data")

def parallell_fetching(keyword, city, pages):
    threads=[]
    for page in range(1,pages+1):
        t = threading.Thread(target=worker_fetcher, args=(keyword, page, city))
        threads.append(t)
        t.start()

def single_fetch(keyword, city, pages):
    for page in range(1, pages+1):
        worker_fetcher(keyword, page, city=city)

if __name__=='__main__':
    print('start crawling')
    keyword="python"
    city="全国"
    
    pages = get_pages(keyword)
    print("Processing %s pages"%pages)
    single_fetch(keyword, city, pages)