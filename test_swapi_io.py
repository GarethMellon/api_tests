import unittest
from selenium import webdriver

class swapiTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("driver/chromedriver.exe")
        self.driver.get("https://swapi.co/")

    def test_webpage(self):
        self.assertEqual(self.driver.title, "SWAPI - The Star Wars API")

    def tearDown(self):
        self.driver.quit()