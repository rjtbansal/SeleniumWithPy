#using find_element from By class
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindBy():
    
    driver = webdriver.Firefox()
    
    def getUrl(self):
        base_url="https://letskodeit.teachable.com/p/practice"    
        self.driver.get(base_url)
    
    def findElement(self):
        elementById=self.driver.find_element(By.ID, "name") 
        if elementById:
            print "%s id is found" % (elementById)
        else:
            print "%s is not found" % (elementById)
            
        elementByXpath=self.driver.find_element(By.XPATH, '//*[@id="product"]');
        if elementByXpath:
            print "Xpath found"
        else:
            print "xpath not found"  
            
        elementByLink = self.driver.find_element(By.LINK_TEXT, "Login") 
        if elementByLink:
            print "Link found"
        else:
            print "Link not found" 
    
findInstance = FindBy()
findInstance.getUrl()
findInstance.findElement()
  
        
            