from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_argument()
def do_request(url):
    browse=webdriver.Chrome(
        executable_path=r'C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\Scrap\Selenium\chromedriver.exe',
        options=options
    )
    browse.get(url=url)
    browse.find_element(By.XPATH,'')
    browse.click()
    for site_name in :
        browse.get_screenshot_as_file(f"C:\Users\Admin\PycharmProjects\DONE\MINI-PROJECTS\Scrap\sites\site-screen\screens\screen {site_name}")

