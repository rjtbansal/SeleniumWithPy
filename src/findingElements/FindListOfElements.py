#using find_elements from By class : finds multiple
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindListOfElements():
    
    driver = webdriver.Firefox()
    
    def getUrl(self):
        base_url="https://letskodeit.teachable.com/p/practice"    
        self.driver.get(base_url)
    
    def findElements(self):
        elements_list_by_class=self.driver.find_elements(By.CLASS_NAME, "left-align") 
        if elements_list_by_class:
            print("Class list has: "+str(len(elements_list_by_class)))
            
        elements_list_by_tag=self.driver.find_elements(By.TAG_NAME, "a")
        if elements_list_by_tag:
            print("Tag list has: "+str(len(elements_list_by_tag)))
        
    
findInstance = FindListOfElements()
findInstance.getUrl()
findInstance.findElements()
  
        
            