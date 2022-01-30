import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class usandotestunitario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/ricard/Documents/chromedriver")

    def test_buscar(self):
        driver = self.driver
        driver.get("https://www.condisline.com/login")
        self.assertIn("Condisline", driver.title)
        usuario = driver.find_element_by_id("userlogin")
        usuario.send_keys("ricard.corrales@gmail.com")
        usuario.send_keys(Keys.ENTER)
        time.sleep(1)
        assert "NO se encontro el elemento" not in driver.page_source
    
        clave = driver.find_element_by_id("password")
        clave.send_keys("Mil@38091924")
        # clave.send_keys("ENTER")

        usuario.send_keys(Keys.ENTER)
        usuario.send_keys(Keys.ENTER)
        ActionChains(driver).click(driver.find_element_by_class_name('access_button')).perform()
    
    def tearDown(self) -> None:
        return super().tearDown()        
        self.driver.close()
        
if __name__=='__main__':
    unittest.main()
                