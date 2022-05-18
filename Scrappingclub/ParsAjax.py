#импортируем библиотеки
import requests
from bs4 import BeautifulSoup
#заголовок отправляемый сайту
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
#список в который будет ложится вся информация
info = []
#функция принимаюшая адрес и номер страницы с которой начнется парсинг
def soupy(url, page=1):
    #обработчик ошибок 
    try:
        while True:
          #если это не первая стр. задаем в параметры ссылки новый параметр
            if page != 1:
                params = {'page': page}
                req = requests.get(url=url, headers=headers, params=params)
                page += 1
                print(page)
#тут будет изменение : если в главном списке есть этот список то код останавливается
                if page == 7:
                    return 'done'
#иначе если это первая страница делаем запрос и переходим на следующюю
            else:
                req = requests.get(url=url, headers=headers)
                page += 1
                print(page)

            #сохраняем первоначальную стр.
            with open('jopa.html', 'w', encoding='utf-8') as f:
                f.write(req.text)
            #читаем файл и сохраняем данные в переменную src
            with open('jopa.html', encoding='utf-8') as f:
                src = f.read()
            #даем обработать BeautifulSoup , с помощью парсера lxml
            soup = BeautifulSoup(src, 'lxml')
            #ищем ссылку для захода в карточку 
            href = soup.find_all('div', class_='card')

            #функцию чтобы обработать и вывести данные с json файла
            def rylka():

#цикл с окончательным поискаом ссылки захода и получения необходимых данных
                for link in href:
                    click = link.find('a').get('href')
                    json_file = click.split('/')
                    page_of_card = json_file[-2]

                    req2 = requests.get(
                        f'https://scrapingclub.com/exercise/list_detail_ajax_infinite_scroll/{page_of_card}/',
                        headers=headers)
#если данные кончились то выводим список и выходии функции возвращая значение 'done'
                    if req2.status_code == 500:
                        print(req2.status_code)
                        print(info)
                        return 'done'
#получаемые данные в формате json
                    content = req2.json()
                    # print(content)
#необходимые данные 
                    img_path = f"https://scrapingclub.com{content['img_path']}"
                    price = content['price']
                    title = content['title']

                    #
#добавляем данные во второстепенный 
                    info.append({'title': title,
                                     'price': price,
                                     'image': img_path
                                     })
                    



#вызываем функицю для парсинга с открываемой ссылки
            rylka()
#либо при ошибке , либо при "done"
    except Exception as ex:
        print('Парсинг всё')
        print(ex)
        #при окончании функции 
    finally:
        print('Аллилуя)))')

#главная функция
def main():
  soupy(f'https://scrapingclub.com/exercise/list_infinite_scroll/')
  #точка входа 
if name=='__main__':
  main() 