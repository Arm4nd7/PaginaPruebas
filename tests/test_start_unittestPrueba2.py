import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class TestFindElementsPart1(unittest.TestCase):
    """Parte 1: Pruebas de búsqueda por ID y NAME"""
    
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
            print("✓ [PART 1] Elemento by ID fue encontrado")
        except Exception as e:
            print(f"✗ [PART 1] Error en búsqueda por ID: {str(e)}")
            self.fail(f"No se encontró elemento por ID: {str(e)}")
    
    def test_02_find_element_by_name(self):
        """Prueba búsqueda por NAME"""
        try:
            elementos = self.driver.find_elements(By.TAG_NAME, "input")
            if elementos:
                print(f"✓ [PART 1] Se encontraron {len(elementos)} inputs por NAME/TAG")
            else:
                print("ℹ [PART 1] No se encontraron elementos por NAME")
        except Exception as e:
            print(f"✗ [PART 1] Error en búsqueda por NAME: {str(e)}")
    
    @classmethod
    def tearDownClass(cls):
        """Se ejecuta una sola vez después de las pruebas de Parte 1"""
        pass  # No cierra el driver aquí

class TestFindElementsPart2(unittest.TestCase):
    """Parte 2: Pruebas de búsqueda por atributos CSS"""
    
    @classmethod
    def setUpClass(cls):
        """Se reutiliza el mismo driver"""
        # Obtiene el driver de Part1 si existe, sino crea uno nuevo
        cls.driver = webdriver.Edge()
        cls.driver.get("https://Arm4nd7.github.io/PaginaPruebas/")
    
    def test_03_find_element_by_css_selector(self):
        """Prueba búsqueda por CSS Selector"""
        try:
            elementos = self.driver.find_elements(By.CSS_SELECTOR, "*")
            if elementos:
                print(f"✓ [PART 2] Se encontraron {len(elementos)} elementos por CSS Selector")
            else:
                print("ℹ [PART 2] No se encontraron elementos por CSS Selector")
        except Exception as e:
            print(f"✗ [PART 2] Error en búsqueda por CSS Selector: {str(e)}")
    
    def test_04_find_element_by_tag_name(self):
        """Prueba búsqueda por TAG NAME"""
        try:
            elementos = self.driver.find_elements(By.TAG_NAME, "body")
            if elementos:
                print(f"✓ [PART 2] Se encontró body tag")
            else:
                print("ℹ [PART 2] No se encontró body tag")
        except Exception as e:
            print(f"✗ [PART 2] Error en búsqueda por TAG NAME: {str(e)}")
    
    @classmethod
    def tearDownClass(cls):
        """Se ejecuta una sola vez después de las pruebas de Parte 2"""
        cls.driver.quit()

if __name__ == '__main__':
    # Ejecutar Parte 1
    print("\n" + "="*60)
    print("EJECUTANDO PARTE 1: Búsqueda por ID y NAME")
    print("="*60 + "\n")
    
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestFindElementsPart1)
    runner1 = unittest.TextTestRunner(verbosity=2)
    result1 = runner1.run(suite1)
    
    # Ejecutar Parte 2
    print("\n" + "="*60)
    print("EJECUTANDO PARTE 2: Búsqueda por CSS y TAG")
    print("="*60 + "\n")
    
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestFindElementsPart2)
    runner2 = unittest.TextTestRunner(verbosity=2)
    result2 = runner2.run(suite2)
    
    # Resumen
    print("\n" + "="*60)
    print("RESUMEN DE PRUEBAS")
    print("="*60)
    print(f"Parte 1 - Tests ejecutados: {result1.testsRun}, Errores: {len(result1.errors)}, Fallos: {len(result1.failures)}")
    print(f"Parte 2 - Tests ejecutados: {result2.testsRun}, Errores: {len(result2.errors)}, Fallos: {len(result2.failures)}")
    print("="*60 + "\n")
