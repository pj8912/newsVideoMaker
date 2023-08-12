from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://www.news18.com/tech/elon-musk-changes-rules-that-can-get-you-paid-thousands-on-x-all-details-8532479.html')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...") 
