#!/usr/bin/env python3
import requests
import sys
import os
from requests.api import get
from bs4 import BeautifulSoup
from wiki import utils

END = utils.END
BOLD = utils.BOLD
BLUE = utils.BLUE
YELLOW = utils.YELLOW
ALL = utils.ALL
randomColor = utils.randomColor

wikiurl = 'https://en.m.wikipedia.org/wiki/'

try:
    width,height = os.get_terminal_size()
    p = True
except OSError:
    p = False
    width = 120
    height = 80

def getHTML(query):
    # global wikiurl
    return requests.get(f'{wikiurl}{query}').text

def getSummary(term):
    final_content = []
    content = getHTML(term)
    soup = BeautifulSoup(content,'html.parser')
    content = soup.find_all('p') 
    print('\n'+(BOLD+str(term)).center(width,'-')+ '\n'+END)

    for i in content:
        if i.get_text() == '\n': pass
        else:
            if i('sup'):
                for tag in i('sup'): tag.decompose()
            data = i.get_text()
            final_content.append(data)
            if len(final_content) == 2: break

    if 'may refer to:' in str(i):
        print('Did You Mean: ')
        term = searchInfo(term)
    else:
        print(randomColor())
        print(*final_content,sep = '\n\n')
        print(END)

def getInfo(term):
    final_content = []
    content = getHTML(term)
    soup = BeautifulSoup(content,'html.parser')
    content = soup.find_all('p') 
    
    for i in content:
        if i('sup'):
            for tag in i('sup'): tag.decompose()
        data = i.get_text()
        final_content.append(data)

    if 'may refer to:' in str(final_content[0]): term = searchInfo(term)
    else:
        if p == True:
            print('\n'+(BOLD+str(term)).center(width,'-')+END+'\n')
            print(BLUE+str(wikiurl).center(width,' ')+END+'\n')

        if p == False:
            print('\n'+str(term).center(width,'-'))
            print('\n'+str(wikiurl).center(width, ' ')+'\n')

        for i in final_content:
            if i == '\n': pass
            else:
                if p == True: print(YELLOW+'[-] '+END+randomColor()+i+'\n'+END)
                else: print('[-]'+str(i))

def searchInfo(term):
    final_content = []
    content = getHTML(term)
    soup = BeautifulSoup(content,'html.parser')
    content = soup.find_all('a')
    for i in content:
        if i.get('title') == i.get_text():
            final_content.append(i.get_text())
    final_content = final_content[2:]
    print('\nSearch Results:\n\n')
    print(*final_content,sep ='\n')
