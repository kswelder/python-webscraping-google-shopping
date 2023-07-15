from scrap_sponsored_products import scrap_sponsored_products
from scrap_no_sponsored_products import scrap_no_sponsored_products
from make_file import make_file

def scrap():
    print('Wellcome to scraping products to Google shopping')
    product = input('Search product: ')
    size_list_sponsored = int(input('Size list sponsored products: '))
    size_list_no_sponsored = int(input('Size list no sponsored products: '))

    sponsored = scrap_sponsored_products({
        'name': product,
        'size': size_list_sponsored
    })
    no_sponsored = scrap_no_sponsored_products({
        'name': product,
        'size': size_list_no_sponsored
    })

    print('Save products in csv file ?\nY, n')
    save = input()

    if save in ['Y', 'y']:
        make_file(sponsored, no_sponsored)
    else:
        print('Print list products ?\nY, n')
        listPrint = input()
        if listPrint in ['Y', 'y']:
            listPrint = input('Are you sure you want to print ', len(sponsored) + len(no_sponsored), ' results to the screen?\nY, n')
            if listPrint in ['Y', 'y']:
                for element in products:
                    print(element)
            else:
                save = input('You want save in csv file?\nY, n\n')
                if save in ['Y', 'y']:
                    make_file(sponsored, no_sponsored)

if __name__ == '__main__':
    scrap()
