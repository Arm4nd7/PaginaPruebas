import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class TestFindByIdName(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Se ejecuta una sola vez antes de todas las pruebas"""
        cls.driver = webdriver.Edge()
        cls.driver.get("https://Arm4nd7.github.io/PaginaPruebas/")
    
    def test_01_find_element_by_id(self):
        """Prueba búsqueda por ID"""
        try:
            elemento = self.driver.find_element(By.ID, "suggestions")
            self.assertIsNotNone(elemento)
            print("✓ El elemento by ID fue encontrado")
        except Exception as e:
            print(f"✗ Error en búsqueda por ID: {str(e)}")
            self.fail(f"No se encontró elemento por ID: {str(e)}")
    
    def test_02_find_element_by_name(self):
        """Prueba búsqueda por Name"""
        try:
            # Intenta encontrar un elemento por atributo name
            elemento = self.driver.find_elements(By.NAME, "*")
            if elemento:
                print(f"✓ Se encontraron {len(elemento)} elementos por NAME")
            else:
                print("ℹ No se encontraron elementos por NAME")
        except Exception as e:
            print(f"✗ Error en búsqueda por NAME: {str(e)}")
    
    @classmethod
    def tearDownClass(cls):
        """Se ejecuta una sola vez después de todas las pruebas"""
        cls.driver.quit()

if __name__ == '__main__':
    # Configurar verbosidad y ejecutar tests
    unittest.main(verbosity=2)
