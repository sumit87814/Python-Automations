from selenium import webdriver
# install chromedriver

driver = webdriver.Chrome()
driver.get('https://youtube.com/')

searchbox = driver.find_element_by_name('search_query')
searchbox.send_keys('sumit rai') 
# searchbox

searchButtton = driver.find_element_by_id('search-icon-legacy')
searchButtton.click()

#searchbutton