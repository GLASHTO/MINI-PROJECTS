from bs4 import *
import requests
import json
# модуль для установки таймера работы
import schedule

data = []


def get_url(url):
    req = requests.get(url=url)
    bs = BeautifulSoup(req.text, 'lxml')
    with open('ixbt.html', 'w') as site:
        site.write(req.text)
    title = bs.find_all('li', class_='item')
    for t in title:
        text_title = t.text
        title_link = t.find('a').get('href')
        # print(f'===\n{text_title[10:].strip()}\n'
        #       f'https://www.ixbt.com/{title_link}')
        if '#' in title_link:
            hash_ind = title_link.index('#')
            data.append({'name': f'{text_title[10:].strip()}',
                         'link': f'https://www.ixbt.com/{title_link[:hash_ind]}'})
        else:
            data.append({'name': f'{text_title[10:].strip()}',
                         'link': f'https://www.ixbt.com/{title_link}'})

        print(data)
        with open('ixbt.json', 'w', encoding='utf-8') as site_data:
            json.dump(data, site_data, ensure_ascii=False, indent=8)


def main():
    get_url('https://www.ixbt.com/news')


if __name__ == '__main__':
    schedule.every().day.at(time_str='04:22').do(main)
    while True:
        schedule.run_pending()
