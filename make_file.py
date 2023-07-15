from os import path
import csv

def make_file(args):
    list_sponsored_products = args['sponsored']
    list_no_sponsored_products = args['no_sponsored']

    print('Verify file exists')
    if path.exists('./products.csv'):
        file = open('products.csv', 'w')
        whiter = csv.writer(file)
        whiter.writerow(['NAME','CATEGORY','PRICE','SHOP','LINK','PROMOTION','ACTIVE'])
        print('Make new file')
    else:
        file = open('products.csv', 'w')
        whiter = csv.writer(file)
        print('Write file')

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
    print('Done')
