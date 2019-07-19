from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Ie()

driver.set_page_load_timeout(10)

print("Hello World")