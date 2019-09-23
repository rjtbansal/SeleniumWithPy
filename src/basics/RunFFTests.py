from selenium import webdriver

class FFTest():
    
    def test(self):
        #getting the driver instance for Firefox
        driver=webdriver.Firefox(executable_path="C:\\Users\\rjtba\\Downloads\\BrowserDrivers\\geckodriver.exe")
        #opening the specified URL
        driver.get("https://www.yahoo.com/")


ffTest = FFTest()
ffTest.test()