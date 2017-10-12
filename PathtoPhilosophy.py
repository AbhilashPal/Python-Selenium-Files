#   Clicking on the first link in the main text of a Wikipedia article, and then repeating the process 
#   for subsequent articles, will usually lead to the Philosophy article. As of February 2016, 97% of all 
#   articles in Wikipedia eventually lead to the article Philosophy. One major loop was found 
#   in the past: the knowledge article led to facts, facts to experience, experience back to knowledge.
#   However, as of July 7, 2017, the facts article has been changed to link to verifiability, verifiability 
#   to verificationism, and verificationism to philosophy.(https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy)

#   This Selenium Script opens chrome and navigates to given wikipedia page and then repeats the above said process
#   until the page on Philosophy is reached.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

string=raw_input("Enter item to search on google! : ")

driver = webdriver.Chrome("C:\\Python27\\selenium\\chromedriver_win32\\chromedriver.exe")         #path to chromedriver
driver.set_page_load_timeout(20)
driver.get("https://www.google.co.in/?gws_rd=ssl")
driver.maximize_window()
driver.implicitly_wait(20)
searchbar = driver.find_element_by_id("lst-ib")
searchbar.send_keys(string+" Wikipedia")
searchbar.submit()
driver.implicitly_wait(50)
driver.find_elements_by_xpath(".//*[@id='rso']//div//h3/a")[0].click()                              #click its href
driver.implicitly_wait(50)

url = driver.current_url


if url[11:20] == "wikipedia":
    print "In wikipedia domain. Starting Philosophy test . . ."
    clickat = driver.find_element_by_xpath("//*[@id='mw-content-text']/div/p[1]/a[1]")
    while url[30:len(url)]!="Philosophy":
        driver.implicitly_wait(50)
        clickat.click()
        clickat = driver.find_element_by_xpath("//*[@id='mw-content-text']/div/p[1]/a[1]")
        url = driver.current_url
        print "->",(url[30:len(url)])
else:
    driver.exit()


