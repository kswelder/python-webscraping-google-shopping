from os import path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv

def scrap(arg):
    print("Scraping sponsored products\nDefnie arguments")
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

    print("==============================================================\n")
    print("Scraping no sponsored products\nDefnie arguments")

    print("Get Grid element")

    element = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div")
    elements = element.find_elements(By.CLASS_NAME, "sh-dgr__gr-auto sh-dgr__grid-result")

    no_sponsored_products = []

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
            inList.find_element(By.CLASS_NAME, "Ib8pOd")
            product['promotion'] = True
        except:
            pass
        try:
            product['name'] = inList.find_element(By.TAG_NAME, "h3").text
        except:
            pass
        try:
            product['linkShop'] = inList.find_element(By.CLASS_NAME, "Lq5OHe eaGTj translate-content").get_attribute("href")
        except:
            pass
        try:
            product['price'] = inList.find_element(By.CLASS_NAME, "a8Pemb OFFNJ").text
        except:
            pass
        try:
            product['nameShop'] = inList.find_element(By.CLASS_NAME, "aULzUe IuHnof").text
        except:
            pass
        no_sponsored_products.append(product)

    result_elements = {
        'sponsored': sponsored_products,
        'no_sponsored': no_sponsored_products
    }
    return result_elements

print("Start program.")

print("Scraping Data")
results = scrap('computador gamer')

if path.exists('./products.csv'):
    file = open('products.csv', 'w')
    whiter = csv.writer(file)
    whiter.writerow(['NAME','CATEGORY','PRICE','SHOP','LINK','PROMOTION','ACTIVE'])
else:
    file = open('products.csv', 'w')
    whiter = csv.writer(file)
print("Write data in file")

list_sponsored_products = results['sponsored']

if len(list_sponsored_products) > 0:
    print("Write Sponsored products")
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

list_no_sponsored_products = results['no_sponsored']

if len(list_no_sponsored_products) > 0:
    print("Write no sponsored products")
    for element in list_no_sponsored_products:
        elements = [
            element['name'],
            element['category'],
            element['price'],
            element['nameShop'],
            element['linkShop'],
            element['promotion'],
            'NO_SPONSORED'
        ]
        whiter.writerow(elements)

file.close()

print("End program")
