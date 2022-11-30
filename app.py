from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Setting the variable `website` to the string `"https://es-la.facebook.com/"`
website="https://es-la.facebook.com/"

# Setting the variable `path` to the string `'C:\Users\toled\Downloads/chromedriver_win32/chromedriver'`
path = 'C:/Users/toled/Downloads/chromedriver_win32/chromedriver.exe'

# Creating a new instance of the Chrome webdriver.
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)