from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv

def scrap_sponsored_products(arg):
    print("Defnie arguments")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options)

    driver.implicitly_wait(5)

    print("Open website")

    driver.get("https://shopping.google.com/?nord=1")

    #driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//*[@id=\"REsRA\"]").send_keys(arg)
    driver.find_element(By.XPATH, "/html/body/c-wiz[1]/div/div/c-wiz/form/div[2]/div[1]/button").click()

    print("Search product")

    element = driver.find_element(By.CLASS_NAME, "GhTN2e")

    print("Get column sponsored products")

    elements = element.find_elements(By.CLASS_NAME, "KZmu8e")

    print("Get list sponsored products")

    sponsored_products = []

    for inList in elements:
        product = {
            'name': '',
            'category': arg,
            'promotion': False,
            'price': '',
            'linkShop': '',
            'nameShop': ''
        }
        try:
            inList.find_element(By.CLASS_NAME, "rz2LD").text
            product['promotion'] = True
        except:
            pass
        try:
            product['name'] = inList.find_element(By.TAG_NAME,'h3').text
        except:
            pass
        try:
            product['nameShop'] = inList.find_element(By.CLASS_NAME, 'E5ocAb').text
        except:
            pass
        try:
            product['linkShop'] = inList.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except:
            pass
        try:
            product['price'] = inList.find_element(By.TAG_NAME, 'b').text
        except:
            pass
        sponsored_products.append(product)

    print(len(sponsored_products))

    driver.close()

    return sponsored_products

print("Start program.")

list_sponsored_products = scrap_sponsored_products("computador gamer")

print("End Scraping\nMake file")
if path.exists('./products.csv'):
    file = open('products.csv', 'w')
    whiter = csv.writer(file)
    whiter.writerow(['NAME','CATEGORY','PRICE','SHOP','LINK','PROMOTION','ACTIVE'])
else:
    file = open('products.csv', 'w')
    whiter = csv.writer(file)
print("Write data in file")
for element in list_sponsored_products:
    elements = [
        element['name'],
        element['category'],
        element['price'],
        element['nameShop'],
        element['linkShop'],
        element['promotion'],
        'SPONSORED'
    ]
    whiter.writerow(elements)
