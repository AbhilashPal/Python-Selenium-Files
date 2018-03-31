from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\Python35\selenium\webdriver\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("http://care.srmuniv.ac.in/ktrcsejava2/")
driver.maximize_window()
driver.implicitly_wait(20)

reg = driver.find_element_by_id("username")
pas = driver.find_element_by_id("password")
reg.send_keys("REPLACE BY YOUR ROLL NO ")
pas.send_keys("REPLACE BY PASSWORD ")
driver.implicitly_wait(20)
sub = driver.find_element_by_id("button")
sub.click()
driver.implicitly_wait(50)
sub = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div/div[1]")
sub.click()
driver.implicitly_wait(50)
time.sleep(2)
for i in range(100):
	driver.get("http://care.srmuniv.ac.in/ktrcsejava2/login/student/code/java/java.code.php?id=1&value="+str(i))
	time.sleep(4)
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'evaluateButton')))
	btn = driver.find_element_by_id("evaluateButton")
	btn.click()
	try:
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'printMsg')))	
		time.sleep(2)	
		driver.implicitly_wait(50)
		btn2 = driver.find_element_by_id("printMsg")
		driver.implicitly_wait(50)
		btn2.click()
		driver.implicitly_wait(50)
	except TimeoutException:
		print("Skipped ",i)

driver.quit()


