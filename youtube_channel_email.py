# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:22:26 2020

@author: Moin Ahmed
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

myurl = 'Enter Youtube Channel here'
uClient = Request(myurl, headers={'User-Agent':'Mozilla/5.0'})
page_html = urlopen(uClient).read()

page_soup = soup(page_html, "html.parser")

list_link=list()
for link in page_soup.find_all('a'):
    list_link.append(link.get('href'))
for link in list_link:
    if link.split('/')[1].split('?')[0] == 'watch':
        link_to_go = link
        break
    
myurl = 'https://www.youtube.com' + link_to_go
uClient = Request(myurl, headers={'User-Agent':'Mozilla/5.0'})
page_html = urlopen(uClient).read()

page_soup = soup(page_html, "html.parser")

email=list()
for div in range(len(page_soup.find_all('div'))):
    x=page_soup.find_all('div')[div]
    potential_email=list()
    for item in x.text.split():
        if (item.find('@')!=-1) and (item.find('.com')!=-1):
            potential_email.append(item)
    if potential_email:
        email.append(potential_email[0])
        break
    
def email_clean(email):
    return email.split("\\")[0]

