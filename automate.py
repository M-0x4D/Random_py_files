import selenium

driver = webdriver.chrome()
driver.get('website link')
element = driver.find_element_by_id('element id')
#click on element 
element.click()
driver.quit()