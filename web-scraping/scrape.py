import requests
from bs4 import BeautifulSoup
import pprint


# IMPORTANT there is redundant code that can be improved on

def create_custon_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[i].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


res = requests.get('https://news.ycombinator.com/')
res_2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res.content.decode('utf-8'))
parsed_object = BeautifulSoup(res.text, 'html.parser')
parsed_object_2 = BeautifulSoup(res_2.text, 'html.parser')
links = parsed_object.select('.storylink')
links_2 = parsed_object_2.select('.storylink')
subtext = parsed_object.select('.subtext')
subtext_2 = parsed_object_2.select('.subtext')
# print(links)
# print(votes)

mega_links = links + links_2
mega_subtext = subtext + subtext_2

new_list = create_custon_hn(mega_links, mega_subtext)

for item in new_list:
    print(item)
