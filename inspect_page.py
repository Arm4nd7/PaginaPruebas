from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https://Arm4nd7.github.io/PaginaPruebas/')
time.sleep(2)

# Ver todos los IDs
ids = driver.find_elements(By.XPATH, '//*[@id]')
print('Elementos con ID:')
for elem in ids[:10]:
    print(f'  - ID: {elem.get_attribute("id")} | TAG: {elem.tag_name}')

# Ver todos los links
links = driver.find_elements(By.TAG_NAME, 'a')
print(f'\nTotal de links: {len(links)}')
for link in links[:5]:
    href = link.get_attribute('href')
    text = link.text
    print(f'  - Href: {href} | Texto: {text}')

# Ver elementos con class
classes = driver.find_elements(By.XPATH, '//*[@class]')
print(f'\nTotal de elementos con class: {len(classes)}')
for elem in classes[:5]:
    print(f'  - Class: {elem.get_attribute("class")} | TAG: {elem.tag_name}')

driver.quit()
