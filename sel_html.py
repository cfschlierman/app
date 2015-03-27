from selenium import webdriver

driver = webdriver.Firefox() 
driver.get ('http://www.yelp.com/search?find_desc=&find_loc=Venice%2C+CA&ns=1&l\ s=71baa56a7602cc86') 
print str(driver.page_source) 
driver.quit()
 
with open ('myfile', 'a') as f: f.write ('hi there\n')
 
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup ("<html>data</html>") 




