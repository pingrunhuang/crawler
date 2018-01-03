
# coding: utf-8

# In[1]:

from urllib import request
from bs4 import BeautifulSoup


# In[2]:

# BeautifulSoup lib note 
url = 'https://movie.douban.com/'
html_page = request.urlopen(url)


# In[3]:

# can try out some other parser such as html.parser, lxml for normal html doc. lxml-xml for parsing html to xml
soup = BeautifulSoup(html_page, 'lxml')
soup


# In[4]:

# four kinds of object in bs: tag, navigablestring, BeautifulSoup and Comment
tag = soup.a
tag


# In[5]:

# each attribute has a name which could also be modified
print(tag.name)
tag.name = "p"
print(tag)


# In[6]:

# accessing the attributes
tag['class']


# In[7]:

# get the attributes as a dictionary which also means you can modify the attributes the way you modify a dictionary 
tag.attrs


# In[8]:

del tag['rel']
tag.attrs


# In[9]:

# NavigableString: basically, it is the content inside the tag 
print(tag.string)
type(tag.string)


# In[10]:

# modification
tag.string.replace_with("Log in")
tag


# In[11]:

# BeautifulSoup
soup.name


# In[12]:

# navigating a tree: note that these operation could be done in the types described above
soup.head


# In[13]:

soup.title


# In[14]:

# get the first <a> tag
print(soup.a)
# get all the <a> tag
print(soup.find_all('a'))


# In[15]:

# .contents to get the list of sub node 
soup.body.contents


# In[16]:

# .children to get the list generator of the sub node
for child in soup.body.children:
    print(child)


# In[17]:

# use descendants to get all the nested nodes
print(len(list(soup.children))) # get the direct children
print(len(list(soup.descendants)))


# In[18]:

# .strings or stripped_strings to view things inside tags
for string in soup.stripped_strings:
    print(string)


# In[19]:

# going up from the current node by using .parent
title_tag = soup.title
print(title_tag)
print(title_tag.parent)


# In[20]:

# .parents to get all the parents 
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)


# In[21]:

# get the next tag which has the same parent of the current node 
soup.div.next_sibling


# In[22]:

soup.div.next_sibling.next_sibling


# In[23]:

# to get the right next to the current element 
soup.div.next_element


# In[24]:

# same goes to previous_siblings
for e in soup.div.next_siblings:
    print(e)


# In[26]:

# Searching a tree
# string filter
soup.find_all('a')


# In[29]:

# regex filter
import re
for tag in soup.find_all(re.compile('^b')):
    print(tag.name)


# In[31]:

# list filter
# match every element in the list
soup.find_all(['a','div'])


# In[41]:

# define customized function with True filter
def has_id_but_no_class(tag):
    return tag.has_attr('id') and not tag.has_attr('class')
soup.div.find_all(has_id_but_no_class)


# In[43]:

# argument of find_all method
soup.find_all(id='top-nav-appintro')


# In[44]:

soup.find_all(id=True)


# In[47]:

soup.find_all(href=re.compile('douban'), id=True)


# In[50]:

soup.find_all(href=re.compile('douban'), attrs={'data-moreurl-dict':'{"from":"top-nav-click-market","uid":"0"}'})


# In[ ]:

# css selector



# urlparse: parse a url into a formated url
from urllib.parse import urlparse

parsed_url = urlparse(url)
# returns ParseResult(scheme='https', netloc='movie.douban.com', path='', params='', query='', fragment='')
