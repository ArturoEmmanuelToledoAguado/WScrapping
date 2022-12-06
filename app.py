from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setting the variable `website` to the string `"https://es-la.facebook.com/"`
website="https://es-la.facebook.com/"

# Setting the variable `path` to the string `'C:\Users\toled\Downloads/chromedriver_win32/chromedriver'`
path = 'C:/Users/toled/Downloads/chromedriver_win32/chromedriver.exe'

# Creating a new instance of the Chrome webdriver.
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
driver.maximize_window()
email = driver.find_element(by=By.ID,value='email')
email.send_keys('jaames11@hotmail.com')
password = driver.find_element(by=By.ID, value='pass')
password.send_keys('Wellneverdie.201')
login = driver.find_element(by= By.NAME, value='login')
login.click()
time.sleep(100)
#input()