import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

class usandotestunitario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/ricard/Documents/chromedriver")

    def test_buscar_por_Xpath(self):
        # browser = webdriver.Firefox()

        driver = self.driver
        url = 'https://www.condisline.com/login'
        driver.get(url)
        
        self.assertIn("Condisline", driver.title)
        timeout = 3

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
        
        quenecesitasXpath = driver.find_element_by_xpath("//*[@id='quickListContent']")
        quenecesitasXpath.send_keys("Vino")
        try:
            # myElem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'bt')))
            elem = driver.find_element_by_xpath("//*[@id='notebook_container']/div/a[1]")
            driver.execute_script("arguments[0].click();", elem)
            # elem.click()
        except TimeoutException:
            print("Se vencio el timeout")
        
        time.sleep(5)
        
        try:
            # myElem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'bt')))
            elem = driver.find_element_by_xpath("//*[@id='notebook_container']/div/a[1]")
            driver.execute_script("arguments[0].click();", elem)
            # elem.click()
        except TimeoutException:
            print("Se vencio el timeout")
        
        time.sleep(5)
        
        quenecesitasXpath = driver.find_element_by_xpath("//*[@id='quickListContent']")
        quenecesitasXpath.send_keys("Galletas")
        try:
            # myElem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'bt')))
            elem = driver.find_element_by_xpath("//*[@id='notebook_container']/div/a[1]")
            driver.execute_script("arguments[0].click();", elem)
            # elem.click()
        except TimeoutException:
            print("Se vencio el timeout")
        
        time.sleep(5)
   
                
        '''    try:
                myElem = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'bt')))
                elem = driver.find_element_by_xpath("//*[@id='mainHeader']/nav/ul/li[2]/span/a")
                elem.click()
            except TimeoutException:
                print("Se vencio el timeout") '''
        
    def tearDown(self) -> None:
        self.driver.close()
        
if __name__=='__main__':
    unittest.main()
                