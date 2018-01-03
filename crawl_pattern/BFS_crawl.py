from urllib.request import urlopen
from bs4 import BeautifulSoup



class Page:
    def __init__(self, url, title):
        self.ID = id(self)
        self.url = url
        self.title = title
        
class PageFound(RuntimeError):
    def __init__(self, message):
        self.message = message

# a dictionary with current page link as the key and a list of links inside the current page
from_url="http://pythonscraping.com/files/inaugurationSpeech.txt")

def breadthSearch(targetPage, fromPage, linkTree, depth):
    '''
    This method takes in 3 arguments. 
    The depth specify how deep you want the crawler to crawl.
    Imagine how you wanna return for each layer of search.
    '''
    if depth==0:
        # means iterate till the final layer
        return linkTree

    if not linkTree:
        linkTree=