from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="/home/ricard/Documents/chromedriver")
driver.get("http://gmail.com")
usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("ricard.corrales@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave = driver.find_element_by_id("password")
clave.send_keys("Mil@gma38091924")
clave.send_keys("ENTER")




# driver.close()