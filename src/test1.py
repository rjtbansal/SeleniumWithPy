#first test script
from selenium import webdriver
#need to specify path to Chrome
driver=webdriver.Chrome("C:\Python27\Scripts\chromedriver")
#opening facebook.com in browser to test
driver.get("http://www.facebook.com")
#end