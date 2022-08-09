# импортируем библиотеки:
# библиотека для работы с картой
import folium
# для дизайна логотипа
from pyfiglet import Figlet
# для совершения запросов и обработки ошибки подключения
from requests import get
from requests.exceptions import ConnectionError


def get_all_info_by_ip(ip='212.112.122.221'):
    try:
        # полученный IP вставляем URL с подходящей ссылкой, обрабатываем все в формате JSON
        request = get(url=f'http://ip-api.com/json/{ip}').json()
        # получаем необходимые данные из JSON данных сайта
        data = {
            '[IP]': request.get('query'),
            '[Country]': request.get('country'),
            '[int prov]': request.get('isp'),
            '[Org]': request.get('org'),
            '[Region]': request.get('regionName'),
            '[City]': request.get('city'),
            '[ZIP]': request.get('zip'),
            '[lat]': request.get('lat'),
            '[lon]': request.get('lon'),
        }
        # перебираем весь словарь с данными, методом ITEMS() получаем ключь и значение
        for k, v in data.items():
            # если же данных не будет пишем,что в доступе отказано)))
            if v == '':
                v = 'Permission denied'
            print(f'{k} : {v}')
        # находим необходимую область по широте и долготе, после сохраняя файл
        area = folium.Map(location=[data['[lat]'], data['[lon]']])
        area.save(f"{data['[City]']}_{data['[IP]']}.html ")
    # при не выполнении верхней части кода просим проверить подключение к сети
    except ConnectionError:
        print("[!] Please check your connection")


def main():
    # выставляем стиль шрифта лого и выводим его раньше чем опрашиваем IP
    preview_text = Figlet(font='starwars')
    print(preview_text.renderText('INFO BY IP'))
    # получаем IP и даем на съедение функции get_all_info_by_ip
    ip = input('please enter a target IP: ')
    get_all_info_by_ip(ip=ip)


# точка входа или та часть кода откуда начинается выполнение и обработка
if __name__ == '__main__':
    main()
# в дальнейшем подключаем это чудо к телеграмм боту на aiogram )
