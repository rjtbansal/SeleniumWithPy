from selenium import webdriver

class ChromeTest():
    
    def test(self):
        #getting the driver instance for Firefox
        driver=webdriver.Chrome(executable_path="C:\\Users\\rjtba\\Downloads\\BrowserDrivers\\chromedriver.exe")
        #opening the specified URL
        driver.get("https://www.yahoo.com/")


chromeTest = ChromeTest()
chromeTest.test()