#first test script
from selenium import webdriver
#need to specify path to Chrome
driver_chrome=webdriver.Chrome("C:\Python27\Scripts\chromedriver")

#using firefox..notice geckodriver path is specified..here unlike chromedriver we dont have to specify the whole path for firefox
#so a path like C:\Python27\Scripts\geckodriver will throw not found error
driver_firefox=webdriver.Firefox("C:\Python27\Scripts")
#opening facebook.com in browser to test
driver_chrome.get("http://www.facebook.com") #opening facebook in chrome
driver_firefox.get("http://www.cricinfo.com") #opening cricinfo in firefox

#end