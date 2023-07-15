from scrap_sponsored_products import scrap_sponsored_products
from scrap_no_sponsored_products import scrap_no_sponsored_products
from make_file import make_file

def scrap():
    print('Wellcome to scraping products to Google shopping')
    product = input('Search product: ')

    products = [
        scrap_sponsored_products(product),
        scrap_no_sponsored_products(product)
    ]

    print('Save products in csv file ?\nY, n')
    save = input()

    if save in ['Y', 'y']:
        make_file(products)
    else:
        print('Print list products ?\nY, n')
        listPrint = input()
        if listPrint in ['Y', 'y']:
            listPrint = input('Are you sure you want to print ', len(products[0]) + len(products[1]), ' results to the screen?\nY, n')
            if listPrint in ['Y', 'y']:
                for element in products:
                    print(element)
            else:
                save = input('You want save in csv file?\nY, n\n')
                if save in ['Y', 'y']:
                    make_file(products)

if __name__ == '__main__':
    scrap()
