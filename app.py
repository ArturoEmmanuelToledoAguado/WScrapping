from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import requests
import pyautogui

# Setting the variable `website` to the string `"https://es-la.facebook.com/"`
website="https://repositorio.unam.mx/contenidos?f=883.%23.%23.a_lit:Repositorio%20de%20la%20Direcci%C3%B3n%20General%20de%20Bibliotecas%20y%20Servicios%20Digitales%20de%20Informaci%C3%B3n"

# Setting the variable `path` to the string `'C:\Users\toled\Downloads/chromedriver_win32/chromedriver'`
path = 'C:/Users/toled/Downloads/chromedriver_win32/chromedriver.exe'

# Creating a new instance of the Chrome webdriver.
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

def OpenWebSite():
    driver.get(website)
    driver.maximize_window()
    
def Search():
    search = driver.find_element(by=By.ID,value='input-search')
    search.send_keys('PNL')
    find = driver.find_element(by= By.ID, value='btn-general-buscar')
    find.click()
    driver.minimize_window()
    driver.maximize_window()
    document = driver.find_element(by= By.CLASS_NAME , value='element-ing-data-record' and 'img-portada')
    document.click()
    driver.minimize_window()
    driver.maximize_window()
    driver.minimize_window()
    driver.maximize_window()
    download = driver.find_element(by= By.ID, value='cont-completo')
    download.click()
    driver.implicitly_wait(20.20)
    desc =driver.find_element(by= By.XPATH, value='//*[@id="icon"]/iron-icon')
    desc.click()
    driver.implicitly_wait(20.20)
    time.sleep(200)


OpenWebSite()
Search()
print("Holi")