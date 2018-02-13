import requests
import random
import datetime
import re
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
To varify if the link map is right, use the following link
https://oracleofbacon.org/
'''


pages = set()
random.seed(datetime.datetime.now())

def getAllLinksFromSingleLink(url):
    result=[]
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    # filter out some unecessary links
    for link in bsObj.find("a", attrs={'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            if link.attrs['href'] not in result:
                result.append(link.attrs['href'])
    return result

def getRandomLink(articleUrl):
    url = 'http://en.wikipedia.org'+articleUrl
    links = getAllLinksFromSingleLink(url)
    while len(links)>0:
        newArticle = links[random.randint(0, len(links)-1)]
        print(newArticle)
        links=getRandomLink(newArticle)

def 

def getInternalLinks(bsObj, includeURL):
    # Parse a URL into 6 components
    includeURL = urlparse(includeURL).scheme+"://"+urlparse(includeURL).netloc
    internalLinks = []
    # find all links start with "/" or ". The "|" means or and you have to put a "()" to wrap up the url
    for link in bsObj.findAll('a', href=re.compile("^(/|.*"+includeURL+")")):
        if link.attrs['href'] != None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startswith('/'):
                    internalLinks.append(includeURL+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks



def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll('a'):
        pass

if __name__=='__main__':
    all_links = getAllLinksFromSingleLink("http://en.wikipedia.org/wiki/Kevin_Bacon")
    [print(link) for link in all_links]