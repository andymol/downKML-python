from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
import threading
import os,time,csv,datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep    
import selenium.webdriver.support.ui as ui
import glob
from pykml import parser
from os import path
import os


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options, executable_path=r'/usr/bin/chromedriver')
res = driver.get("https://accounts.google.com/signin")

email_phone = driver.find_element_by_xpath("//input[@id='Email']")
email_phone.send_keys("")######### please type the specific gmail address
driver.find_element_by_id("next").click()
password = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='Passwd']"))
)
password.send_keys("")######### please type the specific gmail password
driver.find_element_by_id("signIn").click()

download_path = "/home/nature/Downloads"

# driver = webdriver.Chrome('./chromedriver', chrome_options=options)

driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_path}}
command_result = driver.execute("send_command", params)
driver.get("http://www.google.com/maps/d/u/0/kml?forcekml=1&mid=10MUd82ZM0vhNXxOYefj78uvNi_fIbbgq&lid=h2nWPIi1zcw")
# sleep(20)

print("start downloading...")

for filepath_object in glob.glob(download_path):
    if os.path.isfile(download_path + "/*.kml"):
        break
    else:
        time.sleep(1)

driver.quit()



with open(download_path + "/Untitled layer.kml") as f:
  doc = parser.parse(f).getroot()

print(doc.Document.Placemark.Point.coordinates)


