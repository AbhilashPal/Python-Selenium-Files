from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("C:\\Python27\\selenium\\chromedriver_win32\\chromedriver.exe")
driver.set_page_load_timeout(50)
browser = driver.get("https://academia.srmuniv.ac.in/")

frame = driver.find_element_by_name('zohoiam')
driver.switch_to.frame(frame)
driver.maximize_window()

driver.implicitly_wait(50)
email = driver.find_element_by_xpath("//*[@id='Email']")
email.send_keys("REPLACEBYYOUREMAIL")
password = driver.find_element_by_name("password")
password.send_keys("REPLACEBYYOURPASSWORD")
driver.find_elements_by_xpath("//*[@id='signinForm']/div[5]/input")[0].click()
driver.implicitly_wait(50)

time.sleep(5)

driver.get("https://academia.srmuniv.ac.in/#View:My_Attendance")
time.sleep(3)
element  = driver.find_element_by_xpath('//*[@id="zc-viewcontainer_My_Attendance"]/div/div[4]/div[1]/table[2]/tbody/tr[1]/td[4]/strong')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.get_screenshot_as_file("AttendanceReport.png")

