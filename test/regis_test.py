import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from assets.page import elem

class TestRegist(unittest. TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_regist_success(self):
        driver = self.browser
        driver.get(elem.baseUrl) #Open URL
        self.browser.maximize_window()
        time.sleep(3)

        driver.find_element(By.ID, "signin2").click() 
        time.sleep(2)
        driver.find_element(By.ID,"sign-username").send_keys("pahe_user")
        driver.find_element(By.ID,"sign-password").send_keys("qwerty")
        driver.find_element(By.XPATH, elem.signup_btn).click()
        time.sleep(3)

        #response_data = driver.find_element(By.XPATH,elem.).text
        #self.assertIn(response_data,"Admin")


if __name__ == "__main__": 
    unittest.main()