
from selenium import webdriver

driver = webdriver.Chrome()

# save the url to navigate to in a variable
url = 'http://localhost/iframe-demo.html'

# navigate to the url
driver.get(url)

# find the paragraph outside the iframe
p = driver.find_element_by_id('p-out')
paragraph = p.text
print paragraph

# find the iframe element and switch focus to the iframe
first_frame = driver.find_element('id', 'login-frame')
driver.switch_to.frame(first_frame) #first switch to the frame and then look for elements within that frame

# find username element within the iframe
username = driver.find_element('id','username')
username.send_keys('testuser')

# witch focus back to the main page
driver.switch_to.default_content()
heading = driver.find_element('id', 'hh')
print heading.text

# find the second frame and switch focus to it
second_frame = driver.find_element('id', 'ad-frame')
driver.switch_to.frame(second_frame)
image_link = driver.find_element('id', 'ad_image')
print(image_link.get_attribute('src'))