#Find an element on the web page by id and a name
from selenium import webdriver

class FindByClassAndTag():
    
    driver = webdriver.Firefox()
    
    def getUrl(self):
        base_url="https://letskodeit.teachable.com/p/practice"    
        self.driver.get(base_url)
    
    def findByClass(self):
        elementByClass=self.driver.find_element_by_class_name("displayed-class") #careful with class names and we cant club names together like in css
        if elementByClass:
            print " class is found"
            elementByClass.send_keys("found the class")
        else:
            print "%s is not found" % (elementByClass)
            
    def findByTag(self):
        elementByTag=self.driver.find_element_by_tag_name("h1") #rarely used because high possibility of duplicate tag names(can be used for a title or an h1 since they might be only one in whole page)
        if elementByTag:
            print "%s tag is found" % (elementByTag)
        else:
            print "%s tag is not found" % (elementByTag)
    
findInstance = FindByClassAndTag()
findInstance.getUrl()
findInstance.findByClass()   
findInstance.findByTag()     
        
            