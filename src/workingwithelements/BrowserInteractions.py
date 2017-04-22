from selenium import webdriver

class BrowserInteractions():
    
    driver=webdriver.Firefox()
    
    def getUrl(self):
        base_url="https://letskodeit.teachable.com/p/practice"
        self.driver.get(base_url)
        
    def interactions(self):
        
        #maximize window
        self.driver.maximize_window()
        
        #open url
        self.getUrl()
        
        #get title of current page
        title = self.driver.title
        print("Title of current page: "+title)
        
        #current url
        current_url = self.driver.current_url
        print("Current url: "+current_url)
        
        #browser refresh - first time
        self.driver.refresh()
        current_url = self.driver.current_url
        print("Browser refreshed 1st time: "+current_url)
        
        #browser refresh - 2nd time
        self.driver.get(current_url)
        current_url = self.driver.current_url
        print("Browser refereshed 2nd time:"+current_url)
        
        #open another url
        self.driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')
        current_url = self.driver.current_url 
        print("Browser opened: "+current_url)
        
        #Go back 1 page
        self.driver.back()
        current_url = self.driver.current_url 
        print("Went back one page: "+current_url)
        
        #Go forward
        self.driver.forward()
        current_url = self.driver.current_url 
        print("Moved forward one page: "+current_url)
        
        #Get the page src
        pageSource = self.driver.page_source
        print(pageSource.encode('utf-8')) #to guard against unicode errors: src: http://stackoverflow.com/questions/16823086/selenium-webdriver-and-unicode
        
        #Browser close/quit
        self.driver.quit()
        
browser_interaction = BrowserInteractions()
browser_interaction.interactions()