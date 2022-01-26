from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/ricard/Documents/chromedriver")
driver.get("http://python.org")
driver.close()