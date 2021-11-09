from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs


class Driver:
    def __init__(self):
        s = Service(executable_path=r'./utility/chrome/chromedriver')
        self.web_driver = webdriver.Chrome(service=s)

    def go_to(self,url):
        self.web_driver.get(url)

    def get_soup(self):
        soup = bs(self.web_driver.page_source, 'lxml')
        return soup

    def close(self):
        self.web_driver.quit()
