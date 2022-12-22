# from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

import time, requests, random, pickle
from bs4 import *

options = uc.ChromeOptions()
# options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument(
    'user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
# options.add_argument("--disable-gpu")
# options.add_argument(r"user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\chromeprofile")
# options.add_argument("--enable-automation")
# options.add_argument("--remote-debugging-port=9222")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--no-sandbox")
# options.add_argument('--disable-extensions')
# options.add_argument("--incognito")
# options.add_argument("--disable-plugins-discovery")
# options.add_argument("window-size=1980,1080")


#  options.add_argument('--always-enable-hdcp')
# options.add_argument('--enable-cloud-print-proxy')
# options.add_argument('--always-enable-hdcp')

# #options.add_argument("--headless")

# options.add_argument('')
# options.add_argument('')
# cock="mts_id=b987d57b-40c6-47cf-9622-9cf99a843c98; dspid=e77db940-3e7f-4100-9136-ce35af5ba6fa; MTS_LOCATION_CODE=77000000000000000000000000; PHPSESSID=df559rkrfmhcssj483j2ppefll; catalog_list_mode=grid; _gid=GA1.2.1817984693.1668012561; i18n_redirected=ru; MTS_ABTEST_s1=120|B; api_token=dccff84c56771e8963bf6ada4540e43231322e3131322e3132322e323231302e31313832363030302031363638303132353632; _userGUID=0:la9vm3p1:OvxvBb2K6LU2REvRcyYO2qBthLvOQCZ1; _dvs=0:la9vm3p1:2oKuTiH9UMNgcCFZTYoBmXSiQu0MqQXA; clientInnerWidth=1920; _ga=GA1.1.2119886319.1668012561; qrator_jsr=1668015324.710.SZx5X0lbofr8J23E-kns0tnf5se4u6cri1s1vhmrva7som9mo-00; _ga_34B604LFFQ=GS1.1.1668012560.1.1.1668015325.60.0.0; qrator_jsid=1668015324.710.SZx5X0lbofr8J23E-712ekd1q3v1m36u46g5c5dsdt6gq0bp6"

# pickle.dump(cock ,open('mts_cookies.pkl','wb'))
# print('cookies get')
# time.sleep(1)
# done_cock=pickle.load(open('mts_cookies.pkl','rb'))
# print(done_cock)

def do_request(url: str):
    try:
        options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        # browse = webdriver.Chrome(
        #     executable_path=r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\Scrap\Selenium\chromedriver.exe',
        #     options=options
        # )
        browse = uc.Chrome(
            executable_path=r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\Scrap\Selenium\chromedriver.exe',
            options=options
        )
        # browse.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": """
        #           const newProto = navigator.__proto__
        #           delete newProto.webdriver
        #           navigator.__proto__ = newProto
        #           """
        # })

        browse.get(url=url)
        time.sleep(100)
        # browse.switch_to.window(browse.window_handles[1])
        # time.sleep(2)
        pickle.dump(browse.get_cookies() ,open('mts_cookies.pkl','wb'))
        print(browse.get_cookies(),browse.page_source)

        # for cok in done_cock:
        #     browse.add_cookie(cok)
        #     time.sleep(5)

        # browse.refresh()
        # WebDriverWait(browse, 1000).until(EC.title_contains("Index"))
        # print(pickle.load(open('mts_cookies','rb')))
        # pickle.dump(browse.get_cookies(), open('mts_cookies', 'wb'))
        time.sleep(random.randint(5, 10))
        browse.close()
        browse.quit()
        exit()
        # browse.find_element(By.XPATH,'')
        # browse.click()
    except Exception as ex:
        print(ex)


def main():
    do_request(
        'https://sbermegamarket.ru/'
        '')


if __name__ == '__main__':
    main()

# def do_request(url):
#     browse=webdriver.Chrome(
#         executable_path=r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\Scrap\Selenium\chromedriver.exe',
#         options=options
#     )
#     browse.get(url=url)
#     browse.find_element(By.XPATH,'')
#     browse.click()
#     for site_name in :
#         browse.get_screenshot_as_file(f"C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\Scrap\sites\site-screen\screens\screen {site_name}")


# params = {
#     ':authority': 'shop.mts.ru',
#     ':method': 'GET',
#     ':path': '/api/v1/products/prices?id=591282&id=608256&id=612384&id=447246&id=393210&id=573954&id=580632&id=607872',
#     ':scheme': 'https',
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'authorization': 'Basic',
#     'cookie': " mts_id=b987d57b-40c6-47cf-9622-9cf99a843c98; dspid=e77db940-3e7f-4100-9136-ce35af5ba6fa; mts_id_last_sync=1667598662; qrator_jsr=1668003782.500.rdq4ZCJwl2x6yikg-ctvp4ji4c8vl03tfr76a1gl6v39p1vu0-00; qrator_jsid=1668003782.500.rdq4ZCJwl2x6yikg-s021rtg5ce35t5e5c3et2befok8id8o6; MTS_ABTEST_s1=120|B; qrator_ssid=1668003783.478.A0VWYJbJTpoz22hq-tehv2til7vr6bna4nf1dkr86jf5c0h20; _gid=GA1.2.2136202710.1668003784; i18n_redirected=ru; MTS_LOCATION_CODE=77000000000000000000000000; api_token=91e360794e370f20172bd0fa7b763e3231322e3131322e3132322e323231302e36383635353830302031363638303033373836; PHPSESSID=df559rkrfmhcssj483j2ppefll; clientInnerWidth=1920; _userGUID=0:la9qe14f:zp6ZzzGK165GGSdJnoNlmYFNZ9N2zk17; dSesn=e77a5360-4dc0-dab3-9b26-68522349846e; _dvs=0:la9qe14f:Gbm2FXBCqDFIWyEEenJfVPbcmCWHhrcs; catalog_list_mode=grid; _gat=1; _ga_34B604LFFQ=GS1.1.1668003784.1.1.1668003960.60.0.0; _ga=GA1.1.1512976385.1668003784",
#     'dnt': "1'",
#     'referer': 'https://shop.mts.ru/',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': "Windows",
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
# }
# resp = requests.get(
#     'https://shop.mts.ru/api/v1/products/prices?id=591282&id=608256&id=612384&id=447246&id=393210&id=573954&id=580632&id=607872',
#     params=params)
# print(resp.status_code)
# with open('site.html', 'w') as file:
#     file.write(resp.text)
