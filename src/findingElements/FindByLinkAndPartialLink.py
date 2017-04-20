#Find an element on the web page by id and a name
from selenium import webdriver

class FindByLinkAndPartialLink():
    
    driver = webdriver.Firefox()
    
    def getUrl(self):
        base_url="https://letskodeit.teachable.com/p/practice"    
        self.driver.get(base_url)
    
    def findByLinkText(self):
        elementByLinkText=self.driver.find_element_by_link_text("Login")
        if elementByLinkText:
            print "%s link is found" % (elementByLinkText)
        else:
            print "%s is not found" % (elementByLinkText)
            
    def findByPartialLinkText(self):
        elementByParitalLink=self.driver.find_element_by_partial_link_text("Pract") #so if an a tag has text Practice this will match
        if elementByParitalLink:
            print "%s partial link is found" % (elementByParitalLink)
        else:
            print "%s partial link is not found" % (elementByParitalLink)
    
findInstance = FindByLinkAndPartialLink()
findInstance.getUrl()
findInstance.findByLinkText()   
findInstance.findByPartialLinkText()     
        
            