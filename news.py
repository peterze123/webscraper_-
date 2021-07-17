from bs4 import BeautifulSoup
import requests
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('a.storylink')
subtext = soup.select('.subtext')

def sort(news, constant):
    return sorted(news, key = lambda x: x[constant], reverse = True)


def downloader(links, subtext):
    news = []
    for i, item in enumerate(links):
        headline = item.getText()
        link = item.get('href')
        votes = subtext[i].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            news.append({'headline': headline,'link': link, 'votes': points})
        else:
            news.append({'headline': headline,'link': link, 'votes': 0})
    return sort(news, 'votes')


pprint.pprint(downloader(links, subtext))
