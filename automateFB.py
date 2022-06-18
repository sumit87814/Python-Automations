from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver
from getpass import getpass

username=input("enter your username: ")
password=getpass("enter your password: ")
#input password hidden function

driver=webdriver.Chrome()
driver.get("https://facebook.com")

username_text = driver.find_element_by_id('email')
username_text.send_keys(username)


password_text = driver.find_element_by_id("pass")
password_text.send_keys(password)


login_button=driver.find_element_by_class_name('_6ltg')
login_button.click()

