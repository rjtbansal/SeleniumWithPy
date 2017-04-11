#locating links and partial links on a page 

from selenium import webdriver
import pdb #to debug..python debugger

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com")

pdb.set_trace() #will halt program execution here..c to continue
learn_html=driver.find_element_by_link_text("Learn HTML") #look for link called Learn HTML
learn_html.click() #click the link 

pdb.set_trace()
html_elements=driver.find_element_by_partial_link_text("HTML Elem") #will match partial text..here on the page its HTML Element and that is what clicks on
html_elements.click()