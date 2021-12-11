from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
driver = webdriver.Firefox(executable_path='/home/mahdi/Downloads/geckodriver')
driver.get('https://www.instagram.com/mahdi_f__p')
print(f"site title: {driver.title}")