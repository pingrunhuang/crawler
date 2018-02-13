# starting with a single page
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


def get_all_links():
    url='https://en.wikipedia.org/wiki/Eric_Idle'
    html=urlopen(url)
    bsObj=BeautifulSoup(html)
    # this operation, it is printing all the links 
    for link in bsObj.find_all('a'):
        if 'href' in link.attrs:
            print(link.attrs['href'])

# some technique to filter the links
# rules: any links start with /wiki/, 
# * means 0 or many, ? means 0 or 1, + means 1 or many 
def some_filer():
    url='https://en.wikipedia.org/wiki/Eric_Idle'
    html=urlopen(url)
    bsObj=BeautifulSoup(html)
    for link in bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=
        re.compile('^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs:
            print(link.attrs['href'])


random.seed(datetime.datetime.now())
def getLinks(article):
    html = urlopen('https://en.wikipedia.org'+article)
    bsObj = BeautifulSoup(html)
    return bsObj.find('div', {'id':'bodyContent'}).find_all('a', href=
    re.compile('^(/wiki/)((?!:).)*$'))

def main():
    links = getLinks('/wiki/Kevin_Bacon')
    while len(links)>0:
        # randomly pick one article from the existing page
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        links=getLinks(newArticle)

if __name__ == '__main__':
    main()