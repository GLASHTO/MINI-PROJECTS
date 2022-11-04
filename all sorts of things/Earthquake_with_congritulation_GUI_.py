# первая работа с API
# графический интерфейс
from tkinter import *

# для запросов в браузер
import requests


# функция для того чтобы проще было получать аргументы
def info_about_earthquake(par):
    request_on_api = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query', params=par).json()
    # выводим статус кода
    # print(request_on_api.status_code)
    # разкомментирова при работе с терминалом и убрать с первоначального вызова request json()
    # request_on_api = request_on_api.json()
    # генератор ,выводящий данные,чтобы не занимать лишнюю память,разкомментировать при работе с терминалом
    # request_on_api_text = [print(f'{key} : {value}') if key != 'title' else print(f'{key} : {value}\n')
    #                        for info in request_on_api['features'] for key, value in info['properties'].items()]
    # список который выводится в окне new_window
    data = []
    # Генератор переписанный под функцию
    for info in request_on_api['features']:
        for key, value in info['properties'].items():
            if key != 'title':
                data.append(f'{key}:{value}')
            else:
                data.append(f'''{key}:{value}
''')
    # новое окно с данными
    new_window_(data)


# функция начального окна
def monitor(width=500, height=500):
    global start_time, end_time
    # инициализация холста
    Monik = Canvas(tk, width=width, height=height)
    Monik.pack()
    # ширина текстового поля
    width_text_field = 20
    # получаем даты с какого ==>
    start_time = Entry(Monik, width=width_text_field)
    start_time.insert(0, 'С:')
    start_time.place(rely=0, relx=0)
    # ==> по какое и настройка вида текстового поля
    end_time = Entry(Monik, width=width_text_field)
    end_time.insert(0, "по:")
    end_time.place(relx=0.2)

    # функция для удаления надписи на виджете start_time
    def del_s(event):
        global press
        start_time.delete(0, END)
        # отмена привязки после первого очищения
        start_time.unbind('<Button-1>')

    # функция для удаления надписи на виджете end_time
    def del_e(event):
        global press
        end_time.delete(0, END)
        # отмена привязки после первого очищения
        end_time.unbind('<Button-1>')

    # привязка двух вышенаписанных функций к виджетам
    start_time.bind('<Button-1>', del_s)
    end_time.bind('<Button-1>', del_e)
    # кнопка поиска,которая вызывает функцию сбора данных
    btn = Button(Monik, text='Поиск', command=get_info_from_GUI)
    btn.place(relx=0.5, rely=0.5)


# функция вызова нового окна
def new_window_(text, width=500, height=500):
    root = Tk()
    new_window = Canvas(root, width=width, height=height, background='black')
    new_window.pack()
    # настройки текста
    label = Text(new_window,
                 wrap=WORD, background='black', foreground='green', font='Courier 14',
                 width=width, height=height)
    label.insert(1.0, text)
    label.pack()


def get_info_from_GUI():
    global start_time, end_time
    # получаем введенные данные попутно удаляя лишний пробелы
    start_time_text = start_time.get().strip()
    end_time_text = end_time.get().strip()
    # обработчик ошибок
    try:
        # условие работы сборщика инфы
        condition = True
        # обход полученных данных и обработка на ошибки
        for index in range(len(start_time_text)):
            if start_time_text[index].isalpha():
                # print("Введите дату такого вида: 2014-12-25")
                new_window_("Введите дату такого вида: 2014-12-25")
                end_time.delete(0, END)
                condition = False
                break
            if not start_time_text[index].isdigit() and start_time_text[index] != '-':
                start_time = start_time_text.replace(start_time[index], '-')
            for index in range(len(end_time_text)):
                if end_time_text[index].isalpha():
                    # print("Введите дату такого вида: 2014-12-25")
                    end_time.delete(0, END)
                    condition = False
                    new_window_("Введите дату такого вида: 2014-12-25")
                    break
                if not end_time_text[index].isdigit() and end_time_text[index] != '-':
                    start_time = end_time_text.replace(end_time_text[index], '-')
        # если условия соблюдены, то выполняется работа с API
        if condition:
            # задаем параметры запроса к API
            query_params = {'format': 'geojson',
                            'starttime': start_time_text,
                            'endtime': end_time_text}
            info_about_earthquake(par=query_params)
    except Exception as ex:
        # print('Попробуйте снова, программёр, следуя вышеуказанным инструкциям')
        new_window_('Попробуйте снова, программёр, следуя вышеуказанным инструкциям')
        # print(ex)


# главная функция
def main():
    monitor()


# точка входа
if __name__ == '__main__':
    # инициализация класса Тк
    tk = Tk()
    main()
    tk.mainloop()
