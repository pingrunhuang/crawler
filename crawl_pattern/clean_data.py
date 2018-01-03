import re
from bs4 import BeautifulSoup
import string
from urllib.request import urlopen

url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'

def ngrams(input, n=2):
    input = input.split(' ')
    
    
if __name__ == '__main__':
    html = urlopen(url)

