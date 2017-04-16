from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
#driver.implicitly_wait(30) #implicit weight waits for 30 sec before the item is ready..for example slow loading of image..it weights for the life of webdriver object


#save the url to navigate to in a variable
url = 'http://localhost:63342/PythonSelenium%20Course/Test_Site/test_site.html'

#Navigate to the url
driver.get(url)

my_btn = driver.find_element_by_id('slow_btn')
my_btn.click()

#explicitely waiting for 10 secs..if it doesnt find the expected result..it will throw timeout exception
my_mage = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(('id', 'the_slow_image')))
print ('I explicitly waited and I finally found the element')
