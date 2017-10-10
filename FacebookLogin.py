from selenium import webdriver


email     = raw_input("Enter your email : ")
password  = raw_input("Enter your password : ")


driver = webdriver.Chrome("C:\\Python27\\selenium\\chromedriver_win32\\chromedriver.exe")  #place chromedriver at this location or 
driver.set_page_load_timeout(20)                                                           #change the location to the location of driver
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_name('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()
