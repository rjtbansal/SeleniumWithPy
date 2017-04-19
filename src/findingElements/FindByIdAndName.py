#Find an element on the web page by id and a name
from selenium import webdriver

class FindByIdName():
    
    driver = webdriver.Firefox()
    
    def getUrl(self):
        base_url="https://letskodeit.teachable.com/p/practice"    
        self.driver.get(base_url)
    
    def findById(self):
        elementById=self.driver.find_element_by_id("namehhhh")
        if elementById:
            print "%s id is found" % (elementById)
        else:
            print "%s is not found" % (elementById)
            
    def findByName(self):
        elementByName=self.driver.find_element_by_name("show-hide")
        if elementByName:
            print "%s name is found" % (elementByName)
        else:
            print "%s name is not found" % (elementByName)
    
findInstance = FindByIdName()
findInstance.getUrl()
findInstance.findById()   
findInstance.findByName()     
        
            