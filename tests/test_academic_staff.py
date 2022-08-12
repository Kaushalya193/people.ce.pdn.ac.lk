import unittest
import webdriver_functions
import a_config_test
import requests
from selenium.webdriver.common.by import By


class Tests(unittest.TestCase):
    def test_academic_staff_page_loads(self):
        driver = webdriver_functions.getAcademicStaff()
        if driver.page_source.find("Academic Staff") == -1:
            self.fail("Academic Staff page did not load")

    def test_every_link_in_page(self):
        driver = webdriver_functions.getAcademicStaff()
        elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
        print("Number of links: " + str(len(elems)))
        for elem in elems:
            link = elem.get_attribute("href")
            thisRequest = requests.get(link)
            self.assertTrue(thisRequest.status_code == 200, link + " is not valid")


if __name__ == '__main__':
    unittest.main()
