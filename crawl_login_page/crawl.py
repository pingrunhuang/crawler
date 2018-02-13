import requests
from lxml import html
import logging

logger = logging.getLogger()
'''
The key is corresponding to the value of the 'name' attribute of your html element. 
In the bitbucket case, it is username (could be user) ,password (could be passwd) and csrfmiddlewaretoken (could be csrftoken or authenticationtoken)
Therefore the payload will be different according to different web pages.
the csrfmiddlewaretoken is hidden.
'''
logger.level = logging.NOTSET
payload = {
    'username':'pingrunhuang@126.com',
    'password':'huangrunping0608',
    'csrfmiddlewaretoken':''
}



session_requests = requests.session()
login_url = 'https://bitbucket.org/account/signin/'
logging.info("testing the network is fine...")
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
# get the token
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]
payload['csrfmiddlewaretoken']=authenticity_token

logging.info('start logging...')
result = session_requests.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
)

logging.info('logging successfully...')

logging.info('start crawling the dashboard...')
url = 'https://bitbucket.org/dashboard/overview'
result = session_requests.get(
    url,
    headers = dict(
        referer = url
    )
)

tree = html.fromstring(result.content)
# have to checkout the lxml dock
# bucket_elems = tree.findall('.//span[@class="testing_repo"]/@value')
# bucket_names = [bucket.text_content.replace("n","").strip() for bucket in bucket_elems]
# print(bucket_names)