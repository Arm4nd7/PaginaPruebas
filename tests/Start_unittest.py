import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class FindbyIdName(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://Arm4nd7.github.io/PaginaPruebas/")

    def test_find_elements_by_id(self):
        elemento = self.driver.find_element(By.ID, "noImportante")
        if elemento is not None:
            print("El elemento by ID fue encontrado")
            self.assertIsNotNone(elemento)

    def tearDown(self):
        self.driver.quit()
