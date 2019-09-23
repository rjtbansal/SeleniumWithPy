from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():   
    driver=webdriver.Chrome(executable_path="C:\\Users\\rjtba\\Downloads\\BrowserDrivers\\chromedriver.exe")
    #driver = webdriver.Firefox() #somehow the firefox version I had didnt support send_keys and I ended up getting string undefined error
    
    def getUrl(self, base_url):
        self.driver.get(base_url)
        self.driver.maximize_window() #safer to maximize the window..sometimes the elements we want to work on arent visible and we get an exception Element Not Visible
        
    def test(self):
        #click on login         
        login_button = self.driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_button.click() #finding element and then clicking
        
        self.driver.implicitly_wait(5) #waiting 5 seconds for the next page to load..applies to all elements that will take time to load
        
        time.sleep(5) #sleeping for 5 seconds..just to see the automated typing
        email_field=self.driver.find_element(By.ID, "user_email")
        email_field.send_keys("rjtbansal") #sending the keys in input field email
        
        password_field=self.driver.find_element(By.ID, "user_password")
        password_field.send_keys("rajat")
        
        email_field.clear() #clearing the input field
        time.sleep(5)
        email_field.send_keys('rjtbansal')
        
clickSend = ClickAndSendKeys()
clickSend.getUrl("https://letskodeit.teachable.com/p/practice")
clickSend.test()        
        
        
