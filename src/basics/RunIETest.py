from selenium import webdriver

class IETest():
    
    def test(self):
        #getting the driver instance for Firefox
        driver=webdriver.Ie()
        #opening the specified URL
        driver.get("https://www.yahoo.com/")


ieTest = IETest()
ieTest.test()