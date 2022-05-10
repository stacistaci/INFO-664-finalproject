# scrape newyorker.com poems for w.s. merwin
# NOTE: most of his poems here are from before 2005 and are only available as scanned magazine pages.
# this only scrapes his 19 more recent poems from 2007-2019.

import json
import requests
from bs4 import BeautifulSoup
import re
import csv


url_list = []
item_counter = 1

# there are 20 pages of search results for "w.s. merwin," but only *2 pages* with actual scrapable text
while item_counter <= 2:

    url = f'https://www.newyorker.com/contributors/w-s-merwin/page/{item_counter}'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='html.parser')

    object_li = soup.find_all('li', {'class': 'River__riverItem___3huWr'})

    for each_object in object_li:
        title = each_object.find('h4', {'class' : 'River__hed___re6RP'})
        try:
            a_link = each_object.find('a', {'aria-label' : title.text})
            url = a_link['href']
            full_url = 'https://www.newyorker.com/' + url
            url_list.append(full_url)
            titles.append(title.text)
        except:
            continue

    item_counter = item_counter + 1

# save list of urls of poems
with open('newyorker_urls.json', 'w') as out:
    json.dump(url_list, out, indent=2)

    
# scrape text from each urls, if possible
with open('newyorker_urls.json', 'r') as f:
    urls = json.load(f)

text_list = []

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='html.parser')
    try:
        divs = soup.find_all('div', {'class': re.compile('body__inner-container|ArticleBody__articleBody___1GSGP')})

        for div in divs:
            text = div.find_all('p')
            text_list.append(text)

    except:
        continue


# couldn't save text_list as a text file, so saved as a csv ¯\_(ツ)_/¯
with open("newyorker_text.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(text_list)
    
    
# converting to a text file
with open('newyorker_text.txt', 'w') as out:
    with open('newyorker_text.csv', 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            out.write(' '.join(row)+'\n')
    f.close()


# cleaning it up. i'm sure there's a more elegant way to do this!
with open('newyorker_text.txt', 'r') as f:
    with open('newyorker_text_clean.txt', 'w') as w:
        for line in f:
            w.write(line.replace('<p>', '').replace('</p>', '').replace('<br/>', '\n').replace('		', '').replace('				', ''))
