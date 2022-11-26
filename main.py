from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files\chromedriver_win32\chromedriver.exe"
chrome_options = Options()
options2 = Options()
options2.add_argument("--disable-notifications")
driver = webdriver.Chrome(PATH, options=options2)
driver.get("https://facebook.com")
user = driver.find_element(By.ID, "email")
user.send_keys("user")  # enter username
password = driver.find_element(By.ID, "pass")
password.send_keys("password")  # enter password
login = driver.find_element(By.NAME, "login")
login.click()
driver.implicitly_wait(8)
driver.get("https://www.facebook.com/marketplace/category/vehicles?minPrice=9000&maxPrice=20000&maxMileage=80000&minYear=2012&exact=false")
time.sleep(20)
