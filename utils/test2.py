# #coding=utf-8                                                                                                                                                                              
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# options = webdriver.ChromeOptions()
# options.headless = True
# driver = webdriver.Chrome(options=options)

# URL = 'https://pythonbasics.org'

# driver.get(URL)

# S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
# driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment                                                                                                                
# driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

# from selenium.webdriver.common.by import By
# button = driver.find_element(By.CLASS_NAME, "my_button")


# driver.quit()




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()

# Specify the path to the chromedriver executable
chromedriver_path = '/usr/bin/chromedriver'

# Create a Service object with the specified chromedriver path
service = Service(chromedriver_path)

# Use the Service object when creating the WebDriver instance
driver = webdriver.Chrome(service=service, options=options)

URL = 'https://pythonbasics.org'

driver.get(URL)

# Now, find an element on the page by tag name
element = driver.find_element('body')

# Take a screenshot of the element
element.save_screenshot('element_screenshot.png')

driver.quit()
