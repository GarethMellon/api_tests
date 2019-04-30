import unittest
from selenium import webdriver


class swapiTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome("driver/chromedriver.exe", options=chrome_options)
        self.driver.get("https://swapi.co/")

    def test_webpage(self):
        try:
            self.assertEqual(self.driver.title, "SWAPI - The Star Wars API")
            self.assertEqual(self.driver.current_url, "https://swapi.co/")

            """ drill down and check that links exist in nav bar"""
            nav_elem = self.driver.find_element_by_class_name("navbar-nav").find_elements_by_tag_name("li")
            for elem in nav_elem:
                self.assertTrue(elem.find_element_by_tag_name("a").get_attribute("href"))

            """ Check that nav bar link clicks open pages """
            self.driver.find_element_by_link_text("About").click()
            self.assertEqual(self.driver.current_url, "https://swapi.co/about")

            self.driver.find_element_by_link_text("Documentation").click()
            self.assertEqual(self.driver.current_url, "https://swapi.co/documentation")

            self.driver.find_element_by_link_text("Home").click()
            self.assertEqual(self.driver.current_url, "https://swapi.co/")
        except AssertionError:
            raise AssertionError

    def tearDown(self):
        self.driver.quit()
