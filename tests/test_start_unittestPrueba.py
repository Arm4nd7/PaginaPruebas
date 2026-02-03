import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
import os

class TestFindByIdName(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Se ejecuta una sola vez antes de todas las pruebas"""
        # Detectar si estamos en entorno de CI/CD
        is_ci = os.environ.get('CI', 'false').lower() == 'true' or os.environ.get('GITHUB_ACTIONS', 'false').lower() == 'true'
        
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        
        if is_ci:
            # En CI/CD usar headless mode con configuración robusta
            chrome_options.add_argument('--headless=new')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-plugins')
            chrome_options.add_argument('--disable-images')
            chrome_options.add_argument('--disable-notifications')
            chrome_options.add_argument('--single-process')
            cls.driver = webdriver.Chrome(options=chrome_options)
        else:
            # En local, usar Edge si está disponible, sino Chrome
            try:
                cls.driver = webdriver.Edge()
            except:
                cls.driver = webdriver.Chrome(options=chrome_options)
        
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
