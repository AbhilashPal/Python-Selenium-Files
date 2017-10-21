from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

a = int(raw_input("Enter 1 for German, 2 for French and 3 for Bengali : "))
if a == 1:
    k="German"
elif a==2:
    k=="French"
else:
    k="Bengali"
string=raw_input("Enter Text to Translate  : ")

driver = webdriver.Chrome("C:\\Python27\\selenium\\chromedriver_win32\\chromedriver.exe")         #path to chromedriver
driver.set_page_load_timeout(20)
driver.get("https://www.google.co.in/?gws_rd=ssl")
driver.maximize_window()
driver.implicitly_wait(20)
searchbar = driver.find_element_by_id("lst-ib")
searchbar.send_keys("English to "+k)
searchbar.submit()
driver.implicitly_wait(50)

elem1 = driver.find_element_by_xpath('//*[@id="tw-source-text-ta"]')
elem1.send_keys(string)
elem2 = driver.find_element_by_xpath('//*[@id="tw-target-text"]/span')
time.sleep(3)

print (elem2.text)
