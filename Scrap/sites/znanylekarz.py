from bs4 import *
import requests

data = []


def get_html(n=1):
    req = requests.get(f'https://www.znanylekarz.pl/psycholog/warszawa/{n}')
    resp = req.status_code
    if resp:
        print(f'Страница получена:{n}')
    else:
        print('Status: not page')
    return req.text


def get_data(response):
    soup = BeautifulSoup(response, 'lxml')
    card = soup.find_all('div',class_="card-body p-0")
    for info in card:
        photo = info.find('img', {'itemprop': "image"}).get('data-src')
        name = info.find('span', {'itemprop': "name"}).text.strip()
        data.append({'name': name,
                     'photo': f'https:{photo}'})
    return data


def main(n=1):
    for i in range(1, n + 1):
        print(get_data(get_html(i)))


if __name__ == '__main__':
    main(n=5)
