# Generated by Selenium IDE
# import pytest
import time
import unittest
import json
import selenium
from selenium import webdriver


from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestChallenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def teardown_method(self, method):
        self.driver.quit()

    def test_challenge1(self):
        # self.driver.get("https://google.com")
        # self.assertIn("Google", self.driver.title)
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.copart.com/")
        # self.driver.set_window_size(1440, 797)
        # self.driver.execute_script("window.scrollTo(0,1)")
        # self.driver.execute_script("window.scrollTo(0,476)")
        # self.driver.find_element(By.ID, "input-search").click()
        # self.driver.find_element(By.ID, "input-search").send_keys("lamborghini")
        # self.driver.find_element(By.LINK_TEXT, "lamborghini").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".btn-lightblue").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".col-md-7").click()
        # self.driver.find_element(By.ID, "input-search").send_keys("ford")
        # self.driver.find_element(By.CSS_SELECTOR, ".btn-lightblue").click()
        # element = self.driver.find_element(By.LINK_TEXT, "Support")
        # actions = ActionChains(self.driver)
        # actions.move_to_element(element).perform()


if __name__ == '__main__':
    unittest.main()
