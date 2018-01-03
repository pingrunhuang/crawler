from movie import Movie
from urllib import request
from bs4 import BeautifulSoup

douban_index_url = 'https://movie.douban.com/'
movie_queue = list()
url_queue = list()


def gen_soup(url, parser='html.parser'):
    dom = request.urlopen(url)
    soup = BeautifulSoup(dom, parser)
    return soup

def crawl_onshow_movie(url):
    soup = gen_soup(url)
    screening_movie = soup.find('div',class_='screening-bd')
    on_show_list = screening_movie.find_all('ul',class_='')
    for show in on_show_list:
        show_url = show.find('a',href=True)['href']
        print('Inserting {} into the queue...'.format(show_url))
        url_queue.append(show_url)

def instantiate_movie(name, rating, comments):
    return Movie(name, rating, comments)


def traverse_comment_content(comment_url):
    if comment_url == None:
        return
    
    soup = gen_soup(comment_url)
    
    comment_queue = 

def crawl_movie_detail(url=None):
    if url_queue is None:
        raise ValueError('No movie to fetch...')
    
    if url is None:
        while len(url_queue) != 0:
            movie = Movie(name=, rating=, comments=None)
            soup = gen_soup(url_queue.pop())
            comment_url = soup.find('div',id='comments-section').find('span',class_='pl').a['href']
            comment_soup = gen_soup(comment_url)
            comments = [item.string for item in soup.find_all('p',class_="")[:20]]
            next_url = comment_url.split('?')[0] + soup.find('a', class_='next')['href']
            
            # traverse the comment part


    else:
        pass
        



if __name__ == '__main__':
    crawl_onshow_movie(douban_index_url)
    