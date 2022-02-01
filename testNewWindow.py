import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class usandotestunitario(unittest.TestCase):

    #inicializa el driver chrome y lo levanta
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/ricard/Documents/chromedriver")

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get("https://www.condisline.com/login")
        time.sleep(3)

        self.assertIn("Condisline", driver.title)
        
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://stackoverflow.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

        
        usuarioXpath = driver.find_element_by_xpath("//*[@id='userlogin']")
        usuarioXpath.send_keys("ricard.corrales@gmail.com")
        usuarioXpath.send_keys(Keys.ENTER)
        time.sleep(3)
        assert "NO se encontro el elemento" not in driver.page_source
    
        claveXpath = driver.find_element_by_xpath("//*[@id='password']")
        claveXpath.send_keys("Mil@38091924")
        claveXpath.send_keys(Keys.ENTER)
        time.sleep(3)
        ''' claveXpath.send_keys(Keys.ARROW_LEFT)
        time.sleep(3) '''


        ''' pestañaXpath = driver.find_element_by_xpath("//*[@id='mainHeader']/nav/ul/li[2]/span/a")
            pestañaXpath.send_keys(Keys.ENTER)
            time.sleep(3) '''

        # ruta absoluta
        # /html/body/main/div/div/div/div[1]/form/label[2]/input
        """ accederXpath = driver.find_element_by_xpath("//*[@id='login_form']/div/a/span")
        accederXpath.send_keys(Keys.ENTER) """
    
    def tearDown(self) -> None:
        self.driver.close()
        
if __name__=='__main__':
    unittest.main()
                