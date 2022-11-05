from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random, csv, winsound


def csv_create():
    with open('data.csv', 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow((
            "Data",
            "URL",
            "Page"
        ))
    print('Csv created')


def get_data(url: str, data):
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36    ")
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    try:
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\Scrap\Selenium\chromedriver.exe",
            options=options)
        driver.get(url=url)
        time.sleep(5)
        with open('data.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            for repeat in range(1, 101):
                # with open(f'site{repeat}.html', 'w', encoding='utf-8') as s:
                #     s.write(driver.page_source)
                #     print(f'сохранен {repeat}')
                print('start parsing')
                pretexts = driver.find_elements(By.XPATH,
                                                f"//*[@id='__next']/div[1]/div[4]/div/div/div[1]/div[1]/div[@role='button']")

                for i, pre in enumerate(pretexts, 1):
                    pre.click()
                    link = driver.find_element(By.XPATH,
                                               '//*[@id="__next"]/div[1]/div[4]/div/div/div[2]/div/div/div[3]/div[1]/div[5]/div/a').get_attribute(
                        'href')
                    time.sleep(0.5)
                    text = driver.find_element(By.XPATH,
                                               '//*[@id="__next"]/div[1]/div[4]/div/div/div[2]/div/div/p').text

                    writer.writerow([text, link, i])
                button = driver.find_element(By.XPATH,
                                             '//*[@id="__next"]/div[1]/div[4]/div/div/div[1]/div[2]/nav/ul/li[9]/button')
                button.click()
                print(f'Парсинг {repeat} закончен')
                print(f'Переход с {repeat} на {repeat + 1}')
                time.sleep(random.randint(3, 7))




    except Exception as ex:
        print(ex)
    finally:
        print('Finish parsing')
        winsound.Beep(250, 2000)
        driver.close()
        driver.quit()
        exit()


def main():
    data = []
    csv_create()
    get_data("https://www.hattiesburgamerican.com/public-notices", data)


if __name__ == '__main__':
    main()
