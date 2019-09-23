from selenium import webdriver

class ElementState():
    driver = webdriver.Firefox(executable_path="C:\\Users\\rjtba\\Downloads\\BrowserDrivers\\geckodriver.exe")
    
    def getUrl(self, base_url):
        self.driver.get(base_url)
        self.driver.maximize_window()
    
    def testState(self):
        self.driver.implicitly_wait(5)
        #many times there are elements pointing to the same location and some are disabled..so in that scenario we wont be able to
        #do normal operations like send_keys for input type element
        search_elem = self.driver.find_element_by_id("gs_htif0")
        search_elem_state = search_elem.is_enabled() #checking if element is enabled
        if search_elem_state: #if it is only then send_keys
            search_elem.send_keys("angularjs tutorial  --- 1")
        
        search_elem = self.driver.find_element_by_id("gs_taif0")
        search_elem_state = search_elem.is_enabled()
        if search_elem_state:
            search_elem.send_keys("angularjs tutorial --- 2")
            
        search_elem = self.driver.find_element_by_id("lst-ib")
        search_elem_state = search_elem.is_enabled()
        if search_elem_state:
            search_elem.send_keys("angularjs tutorial --- 3")
        
es = ElementState()
es.getUrl("http://www.google.com")
es.testState()
