# -*- coding:utf-8 -*-
'''
This is a rought implementation, results are not stored in the database.


TODO:
store the result as a structured dataset
'''

import requests
import json
from bs4 import BeautifulSoup
import time

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
    print(response.text)
    result = json.loads(response.text)
    totalCount = result['content']['positionResult']['totalCount']
    positions_per_page = result['content']['positionResult']['resultSize']
    return int(totalCount)//int(positions_per_page) + 1


def search(keywords, city='全国'):
    params = {
        'city':city,
        'cl':'false',
        'fromSearch':'true',
        'labelWords':'',
        'suginput':''
    }
    res = session.get('https://www.lagou.com/jobs/list_%s'%keywords, params=params, headers=headers)
    if res.status_code==200:
        return res
    else:
        return None

def fetch_position_details(positionId):
    url = 'https://www.lagou.com/jobs/%s.html'%positionId
    res = session.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    
    try:
        print(soup.find('dd', {'class':'job_bt'}).get_text())
        print(soup.find('dd', {'class':'job_request'}).get_text())
    except:
        return print('No job request')
    



def fetch_all_positions(response, mode=1):
    payloads={
        'first':'false',
        'pn':'1',
        'kd':'python'
    }
    headers['Referer']=response.url
    res = session.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0', data=payloads, headers=headers)
    if mode==1:
        result = json.loads(res.text)['content']['positionResult']['result']
        for item in result:
            time.sleep(20)
            headers['Referer']=response.url
            positionId = item['positionId']
            print(positionId)
            fetch_position_details(positionId)
    
    elif mode==2:
        total_pages = get_total_page(res)
        for page in range(1,total_pages+1):
            print('Processing the page %s'%page)
            payloads['pn']=str(page)
            res = session.post('https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0', data=payloads, headers=headers)
            json_response=json.loads(res.text)
            try:
                result=json_response['content']['positionResult']['result'])
                for item in result:
                    # it is found that each fetching request should have some pause in order to get data back
                    time.sleep(20)
                    headers['Referer']=response.url
                    positionId = item['positionId']
                    print(positionId)
                    fetch_position_details(positionId)
            except:
                continue

if __name__=='__main__':
    print('start crawling')
    response = search('python')
    if response:
        fetch_all_positions(response,1)