from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scrap_no_sponsored_products(args):
    print("Scraping no sponsored products")

    list_no_sponsored_products = []
    size_list = 0

    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options)

    driver.get("https://shopping.google.com/?nord=1")

    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//*[@id=\"REsRA\"]").send_keys(args['name'])
    driver.find_element(By.XPATH, "/html/body/c-wiz[1]/div/div/c-wiz/form/div[2]/div[1]/button").click()

    print("Search product")

    element = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[4]/div[3]/div/div[3]/div[2]/div[2]/div')
    elements = element.find_elements(By.TAG_NAME, 'div')

    for inList in elements:
        product = {
            'name': '',
            'category': args['name'],
            'promotion': False,
            'price': '',
            'linkShop': '',
            'nameShop': ''
        }
        try:
            product['name'] = inList.find_element(By.TAG_NAME, 'h3').text
        except:
            pass
        try:
            product['price'] = inList.find_element(By.CLASS_NAME, 'kHxwFf').find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME, 'span').text
        except:
            pass
        try:
            product['nameShop'] = inList.find_element(By.CLASS_NAME, 'aULzUe IuHnof').text
        except:
            pass
        try:
            product['linkShop'] = inList.find_element(By.CLASS_NAME, 'xCpuod').get_attribute('href')
        except:
            pass
        try:
            inList.find_element(By.CLASS_NAME, 'Ib8pOd').text
            product['promotion'] = True
        except:
            pass
        try:
            if size_list >= args['size']:
                break
        except:
            if size_list >= 100:
                break
        if product['name'] != '' and product['price'] != '' and product['nameShop'] != '' and product['linkShop'] != '':
            list_no_sponsored_products.append(product)
            size_list += 1

    driver.close()

    return list_no_sponsored_products
