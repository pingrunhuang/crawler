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

session = requests.Session()
headers={
    'Referer':'https://www.lagou.com/',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en,zh-CN;q=0.9,zh;q=0.8,zh-TW;q=0.7',
    'Host':'www.lagou.com',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def get_total_page(response):
    result = json.loads(response.text)
    totalCount = result['content']['positionResult']['totalCount']
    positions_per_page = result['content']['positionResult']['resultSize']
    return int(totalCount)//int(positions_per_page) + 1

def fetch_position_details(positionId):
    url = 'https://www.lagou.com/jobs/%s.html'%positionId
    res = session.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    
    try:
        print(soup.find('dd', {'class':'job_bt'}).get_text())
        print(soup.find('dd', {'class':'job_request'}).get_text())
    except:
        return print('No job request')
    

def get_pages(keywords, city='全国'):
    '''
    type: keywords: the keyword you want to search
    rtype: totla_pages:int 
    '''
    params = {
        'city':city,
        'cl':'false',
        'fromSearch':'true',
        'labelWords':'',
        'suginput':''
    }
    payloads={
        'first':'false',
        'pn':'1',
        'kd':keywords
    }
    # replace the space with %20
    new_keywords = keywords
    if len(keywords.split(' '))!=1:
        new_keywords=keywords.replace(' ', '%20')

    url='https://www.lagou.com/jobs/list_%s'%new_keywords
    response = session.get(url, params=params, headers=headers)

    if response.status_code!=200:
        print("Error for fetching data...")
        return None
    
    res = session.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0', data=payloads, headers=headers)
    total_pages = get_total_page(res)
    # set the global referer url after getting all the pages num
    headers['Referer']=res.url
    return total_pages

def worker_fetcher(keywords, page):
    payloads={
        'first':'false',
        'pn':str(page),
        'kd':keywords
    }
    print('Processing the page %s'%page)
    res = session.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0', data=payloads, headers=headers)
    json_response=json.loads(res.text)
    try:
        result=json_response['content']['positionResult']['result']
        for item in result:
            try:
                # it is found that each fetching request should have some pause in order to get data back
                time.sleep(20)
                headers['Referer']=response.url
                positionId = item['positionId']
                print(positionId)
                fetch_position_details(positionId)
            except:
                continue
    except:
        print("Error parsing data")

if __name__=='__main__':
    print('start crawling')
    keyword="python"
    pages = get_pages(keyword)
    threads=[]
    for page in range(1,pages+1):
        threads.append(threading.Thread("Worker thread %s"%str(page), target=worker_fetcher, args=(keyword, page)))

    response = fetch_all_positions(keywords='python', mode=1)