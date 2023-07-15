from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scrap_sponsored_products(arg):
    print("Scraping sponsored products")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options)

    driver.implicitly_wait(5)

    driver.get("https://shopping.google.com/?nord=1")

    driver.implicitly_wait(10)

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

    return sponsored_products
