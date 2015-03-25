from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.yelp.com/search?find_desc=&find_loc=Venice%2C+CA&ns=1&ls=71baa56a7602cc86')
print driver.html
driver.quit()
