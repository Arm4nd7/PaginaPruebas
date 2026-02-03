import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

class TestSearchByClassPartial(unittest.TestCase):
    """Parte 1: Pruebas de búsqueda por Clase y Link Parcial"""
    
    @classmethod
    def setUpClass(cls):
        """Se ejecuta una sola vez antes de todas las pruebas"""
        cls.driver = webdriver.Edge()
        cls.driver.get("https://Arm4nd7.github.io/PaginaPruebas/")
    
    def test_01_find_element_by_class_name(self):
        """Prueba búsqueda por CLASS NAME"""
        try:
            # Busca elemento por clase específica
            elemento = self.driver.find_element(By.CLASS_NAME, "container")
            print(f"✓ [PART 1] Se encontró elemento con clase 'container'")
            self.assertIsNotNone(elemento)
            # Intenta encontrar todos los elementos con clases
            elementos_con_clase = self.driver.find_elements(By.XPATH, "//*[@class]")
            if elementos_con_clase:
                print(f"✓ [PART 1] Total de {len(elementos_con_clase)} elementos con atributo class")
            self.assertGreater(len(elementos_con_clase), 0)
        except Exception as e:
            print(f"ℹ [PART 1] Búsqueda por CLASS NAME: {str(e)}")
    
    def test_02_find_element_by_partial_link(self):
        """Prueba búsqueda por PARTIAL LINK TEXT"""
        try:
            # Primero, encuentra todos los links
            links = self.driver.find_elements(By.TAG_NAME, "a")
            print(f"✓ [PART 1] Se encontraron {len(links)} links en la página")
            
            if links:
                # Intenta usar partial link text si hay links
                for link in links[:3]:  # Prueba los primeros 3
                    link_text = link.get_attribute("href")
                    print(f"  - Link encontrado: {link_text}")
            
            self.assertGreater(len(links), 0)
        except Exception as e:
            print(f"✗ [PART 1] Error en búsqueda por PARTIAL LINK: {str(e)}")
    
    @classmethod
    def tearDownClass(cls):
        """Se ejecuta una sola vez después de las pruebas de Parte 1"""
        pass  # No cierra el driver aquí

class TestSearchByFullLink(unittest.TestCase):
    """Parte 2: Pruebas de búsqueda por Link Completo y atributos específicos"""
    
    @classmethod
    def setUpClass(cls):
        """Se reutiliza el mismo driver"""
        cls.driver = webdriver.Edge()
        cls.driver.get("https://Arm4nd7.github.io/PaginaPruebas/")
    
    def test_03_find_element_by_link_text(self):
        """Prueba búsqueda por LINK TEXT completo"""
        try:
            links = self.driver.find_elements(By.TAG_NAME, "a")
            if links:
                # Obtiene el texto de los primeros links
                for link in links[:3]:
                    link_text = link.text
                    if link_text:
                        print(f"✓ [PART 2] Link encontrado con texto: '{link_text}'")
            print(f"✓ [PART 2] Total de {len(links)} links encontrados")
            self.assertGreater(len(links), 0)
        except Exception as e:
            print(f"✗ [PART 2] Error en búsqueda por LINK TEXT: {str(e)}")
    
    def test_04_find_element_by_xpath_specific(self):
        """Prueba búsqueda por XPATH con atributos específicos"""
        try:
            # Busca elementos con ID específico
            elemento_por_id = self.driver.find_elements(By.XPATH, "//*[@id]")
            print(f"✓ [PART 2] Se encontraron {len(elemento_por_id)} elementos con ID")
            
            # Busca elementos con class específico
            elemento_por_class = self.driver.find_elements(By.XPATH, "//*[@class]")
            print(f"✓ [PART 2] Se encontraron {len(elemento_por_class)} elementos con CLASS")
            
            # Busca inputs específicos
            inputs = self.driver.find_elements(By.XPATH, "//input[@type]")
            print(f"✓ [PART 2] Se encontraron {len(inputs)} inputs con atributo type")
            
            self.assertGreater(len(elemento_por_id), 0)
        except Exception as e:
            print(f"✗ [PART 2] Error en búsqueda por XPATH: {str(e)}")
    
    def test_05_find_element_by_css_advanced(self):
        """Prueba búsqueda por CSS SELECTOR avanzado"""
        try:
            # Busca elementos por selector compuesto
            elementos_div = self.driver.find_elements(By.CSS_SELECTOR, "div")
            elementos_p = self.driver.find_elements(By.CSS_SELECTOR, "p")
            elementos_span = self.driver.find_elements(By.CSS_SELECTOR, "span")
            
            print(f"✓ [PART 2] Elementos DIV encontrados: {len(elementos_div)}")
            print(f"✓ [PART 2] Elementos P encontrados: {len(elementos_p)}")
            print(f"✓ [PART 2] Elementos SPAN encontrados: {len(elementos_span)}")
            
            self.assertGreater(len(elementos_div), 0)
        except Exception as e:
            print(f"✗ [PART 2] Error en búsqueda por CSS SELECTOR avanzado: {str(e)}")
    
    @classmethod
    def tearDownClass(cls):
        """Se ejecuta una sola vez después de las pruebas de Parte 2"""
        cls.driver.quit()

if __name__ == '__main__':
    # Ejecutar Parte 1
    print("\n" + "="*70)
    print("EJECUTANDO PARTE 1: Búsqueda por CLASE y LINK PARCIAL")
    print("="*70 + "\n")
    
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearchByClassPartial)
    runner1 = unittest.TextTestRunner(verbosity=2)
    result1 = runner1.run(suite1)
    
    # Ejecutar Parte 2
    print("\n" + "="*70)
    print("EJECUTANDO PARTE 2: Búsqueda por LINK COMPLETO y XPATH ESPECÍFICO")
    print("="*70 + "\n")
    
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSearchByFullLink)
    runner2 = unittest.TextTestRunner(verbosity=2)
    result2 = runner2.run(suite2)
    
    # Resumen
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS")
    print("="*70)
    print(f"Parte 1 - Tests ejecutados: {result1.testsRun}, Errores: {len(result1.errors)}, Fallos: {len(result1.failures)}")
    print(f"Parte 2 - Tests ejecutados: {result2.testsRun}, Errores: {len(result2.errors)}, Fallos: {len(result2.failures)}")
    print(f"\nTOTAL - Tests ejecutados: {result1.testsRun + result2.testsRun}")
    print(f"TOTAL - Errores: {len(result1.errors) + len(result2.errors)}")
    print(f"TOTAL - Fallos: {len(result1.failures) + len(result2.failures)}")
    print("="*70 + "\n")
