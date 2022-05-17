import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'scrapingclub.com',
    'method': 'GET',
    'path': '/exercise/ajaxdetail_header/',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga=GA1.2.2031305897.1650819285; _gid=GA1.2.1966642537.1652089877; googtrans=/en/ru; googtrans=/en/ru; csrftoken=sYBHN3jLdMYLivP4rHliQua0dpN34GyV8IJVvnMq5JDk56F5wSGUKJGD3FYIDaSc; _gat_gtag_UA_39890589_8=1; _gat=1',
    'dnt': '1',
    'referer': 'https://scrapingclub.com/exercise/detail_header/',
    'sec-ch-ua': 'Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

info = []
#
def soupy(url, page=1):
    #
    try:
        while True:
            if page != 1:
                params = {'page': page}
                req = requests.get(url=url, headers=headers, params=params)
                page += 1
                print(page)
                if page == 7:
                    return 'done'

            else:
                req = requests.get(url=url, headers=headers)
                page += 1
                print(page)

            #
            with open('jopa.html', 'w', encoding='utf-8') as f:
                f.write(req.text)
            #
            with open('jopa.html', encoding='utf-8') as f:
                src = f.read()
            #
            soup = BeautifulSoup(src, 'lxml')
            #
            href = soup.find_all('div', class_='card')

            #
            def rylka():


                for link in href:
                    click = link.find('a').get('href')
                    json_file = click.split('/')
                    page_of_card = json_file[-2]

                    req2 = requests.get(
                        f'https://scrapingclub.com/exercise/list_detail_ajax_infinite_scroll/{page_of_card}/',
                        headers=headers)
                    if req2.status_code == 500:
                        print(req2.status_code)
                        print(info)
                        return 'done'
                    content = req2.json()
                    # print(content)
                    img_path = f"https://scrapingclub.com{content['img_path']}"
                    price = content['price']
                    title = content['title']

                    #

                    info.append({'title': title,
                                     'price': price,
                                     'image': img_path
                                     })
                    




            rylka()

    # except Exception as ex:
    #     print('Парсинг всё')
    #     print(ex)
    finally:
        print('А это просто принт)))')


#
soupy(f'https://scrapingclub.com/exercise/list_infinite_scroll/')
