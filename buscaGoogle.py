import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class usandotestunitario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/ricard/Documents/chromedriver")

    def test_buscar_por_Xpath(self):
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        
        buscaporXpath = driver.find_element_by_xpath("//*[@id='input']")
        time.sleep(3)
        buscaporXpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(10)

        # ruta absoluta
        # /html/body/main/div/div/div/div[1]/form/label[2]/input
        """ accederXpath = driver.find_element_by_xpath("//*[@id='login_form']/div/a/span")
        accederXpath.send_keys(Keys.ENTER) """
    
    def tearDown(self) -> None:
        self.driver.close()
        
if __name__=='__main__':
    unittest.main()
                