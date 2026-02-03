import unittest
import sys
import os
from io import StringIO

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_test_file(test_module_name, description):
    """Ejecuta un archivo de prueba específico y retorna resultados"""
    print("\n" + "="*80)
    print(f"EJECUTANDO: {description}")
    print(f"Archivo: {test_module_name}")
    print("="*80 + "\n")
    
    try:
        # Importa el módulo de prueba
        if test_module_name == 'test_start_unittestPrueba':
            from test_start_unittestPrueba import TestFindByIdName
            suite = unittest.TestLoader().loadTestsFromTestCase(TestFindByIdName)
        
        elif test_module_name == 'test_start_unittestPrueba2':
            from test_start_unittestPrueba2 import TestFindElementsPart1, TestFindElementsPart2
            suite = unittest.TestSuite()
            suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFindElementsPart1))
            suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFindElementsPart2))
        
        elif test_module_name == 'test_start_unittestPrueba3':
            from test_start_unittestPrueba3 import TestSearchByClassPartial, TestSearchByFullLink
            suite = unittest.TestSuite()
            suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSearchByClassPartial))
            suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSearchByFullLink))
        
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        return result
    
    except Exception as e:
        print(f"✗ Error ejecutando {test_module_name}: {str(e)}")
        return None

if __name__ == '__main__':
    print("\n" + "#"*80)
    print("# SUITE COMPLETA DE PRUEBAS UNITARIAS")
    print("#"*80)
    
    results = []
    
    # Ejecutar prueba 1
    result1 = run_test_file('test_start_unittestPrueba', 
                            'Prueba Básica: Búsqueda por ID y NAME')
    if result1:
        results.append(('test_start_unittestPrueba', result1))
    
    # Ejecutar prueba 2
    result2 = run_test_file('test_start_unittestPrueba2', 
                            'Prueba en 2 Partes: ID/NAME + CSS/TAG')
    if result2:
        results.append(('test_start_unittestPrueba2', result2))
    
    # Ejecutar prueba 3
    result3 = run_test_file('test_start_unittestPrueba3', 
                            'Prueba en 2 Partes: CLASS/LINK PARCIAL + LINK COMPLETO/XPATH')
    if result3:
        results.append(('test_start_unittestPrueba3', result3))
    
    # Mostrar resumen
    print("\n" + "#"*80)
    print("# RESUMEN FINAL DE TODAS LAS PRUEBAS")
    print("#"*80 + "\n")
    
    total_tests = 0
    total_errors = 0
    total_failures = 0
    
    for test_name, result in results:
        print(f"{'─'*80}")
        print(f"Archivo: {test_name}")
        print(f"  ✓ Tests ejecutados: {result.testsRun}")
        print(f"  ✗ Errores: {len(result.errors)}")
        print(f"  ✗ Fallos: {len(result.failures)}")
        
        total_tests += result.testsRun
        total_errors += len(result.errors)
        total_failures += len(result.failures)
    
    print(f"\n{'─'*80}")
    print(f"TOTAL GENERAL:")
    print(f"  ✓ Tests ejecutados: {total_tests}")
    print(f"  ✗ Errores totales: {total_errors}")
    print(f"  ✗ Fallos totales: {total_failures}")
    print(f"  ✓ Tests exitosos: {total_tests - total_errors - total_failures}")
    
    if total_errors == 0 and total_failures == 0:
        print(f"\n✓ TODAS LAS PRUEBAS PASARON CORRECTAMENTE")
    else:
        print(f"\n✗ HAY {total_errors + total_failures} PRUEBAS CON PROBLEMAS")
    
    print("#"*80 + "\n")
