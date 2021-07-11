import requests
from bs4 import BeautifulSoup
import time
import random

def get_file(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    book_list = soup.div(id = 'list')
    return book_list

def downloader(book_list):
    title = './' + book_list[0].dl.dt.string
    with open(title + '.txt','w') as file:
        for chapter in book_list[0].find_all('dd'):
            url = 'https://www.biqugee.com' + chapter.a.get('href')
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            title = soup.h1.string
            text = soup.div(id = 'content')[0].get_text().replace('\xa0','\n')
            text = '\n'.join(filter(None, text.split('\n')))
            text = title + '\n' + '\n'  + text + '\n' + '\n' + '\n' + '\n' + '\n' + '\n'
            file.write(text)
            print('ok')
        print('done ')
if __name__ == '__main__':
    downloader(get_file('https://www.biqugee.com/book/30887/'))


