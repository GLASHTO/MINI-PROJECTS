#импортируем библиотеки
import requests
import json
#Копируем заголовки сайта, отправляющего запрос на API
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

#создаем функцию
def soupy(url):
    #инициализируем requests, в аргументы задаем URL-адрес и заголовок,ответ принимаем в виде json
    req = requests.get(url=url, headers=headers).json()
    #
    #(с помощью оператора  with сохраняем файл, чтобы не делать большое кол-во запросов
    # with open('scrap.json', 'w', encoding='utf-8') as f:
    #     json.dump(req, f, indent=4, ensure_ascii=False)
    # with open('scrap.json', encoding='utf-8') as f:
    #     src = json.load(f)
    #)
    #если включить в скрипт создание доп файла чтобы не нагружать запросами сервер req ==> src
    fil = {"img_path": f'https://scrapingclub.com{req["img_path"]}', "price": req['price'], "description": req['description']}
    #сохранение полученного словаря данных в json файл req ==> src
    with open(f'{req["title"]}.json', 'w', encoding='utf-8') as f:
        json.dump(fil, f, indent=4, ensure_ascii=False)
#главная функция
def main():
    soupy('https://scrapingclub.com/exercise/ajaxdetail_header/')
#точка входа
if __name__=='__main__':
    main()