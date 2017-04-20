#Find an element on the web page by id and a name
from selenium import webdriver

class FindByClassAndTag():
    
    driver = webdriver.Firefox()
    
    def getUrl(self):
        base_url="https://letskodeit.teachable.com/p/practice"    
        self.driver.get(base_url)
    
    def findByClass(self):
        elementByXpath=self.driver.find_element_by_xpath("//input[@id='name']")
        if elementByXpath:
            print "%s xpath is found" % (elementByXpath)
        else:
            print "%s is not found" % (elementByXpath)
            
    def findByTag(self):
        elementByCss=self.driver.find_element_by_css_selector("#displayed-text")
        if elementByCss:
            print "%s css is found" % (elementByCss)
        else:
            print "%s css is not found" % (elementByCss)
    
findInstance = FindByClassAndTag()
findInstance.getUrl()
findInstance.findByClass()   
findInstance.findByTag()     
        
            