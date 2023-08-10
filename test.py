from selenium import webdriver
from selenium.webdriver.edge.options import Options
from PIL import Image
from selenium.webdriver.common.by import By

options = Options()
driver = webdriver.Edge(options=options)

url = 'https://blog.daliansky.net/'
driver.get(url)

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

element = driver.find_element(By.TAG_NAME, 'main')
location = element.location
size = element.size

driver.save_screenshot('page.png')

x = location['x']
y = location['y']
width = location['x'] + size['width']
height = location['y'] + size['height']
im = Image.open('page.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('element.png')

driver.quit()
