from bs4 import BeautifulSoup
import logging


class Product:
    def __init__(self, SKU, Serial, Condition, Price):
        self.SKU = SKU
        self.serial = Serial
        self.condition = Condition
        self.price = Price

    def get_price(self):
        return self.price

    def get_serial(self):
        return self.serial

    def get_condition(self):
        return self.condition

    def get_sku(self):
        return self.SKU

    def get_price_int(self):
        nodollar = self.price.replace("$", "")
        nocomma = nodollar.replace(",","")
        decimal = float(nocomma)
        return decimal

    def __repr__(self):
        return f'SKU: {self.SKU}, Serial: {self.serial}, Condition: {self.condition}, Price: {self.price}'

    def __str__(self):
        return f'{self.SKU}   {self.serial}         {self.condition}        {self.price}'

class Store:
    def __init__(self, Name):
        self.name = Name
        self.products = []

    def get_name(self):
        return self.name

    def add_product(self, product):
        self.products.append(product)
    
    def get_products(self):
        return self.products
    
    def set_products(self, products):
        self.products = products

    def __str__(self):
        output = """"""
        output += self.name
        output += "\nSKU      serial        condition       price\n"
        for product in self.products:
            output += str(product) + '\n'
        return output

class StoreProduct(Product):
    def __init__(self, SKU, serial, condition, price, store_name):
        Product.__init__(self, SKU, serial, condition, price)
        self.store_name = store_name
    
    def __str__(self):
        return f"{self.price}   {self.SKU}   {self.serial}      {self.condition}     {self.store_name}"
        


def insertsort(arr):
    for i in range(1, len(arr)):
        a = arr[i]
        j = i -1

        while j >= 0 and a.get_price_int() < arr[j].get_price_int():
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = a

    return arr



def sort_products_ascending(all_stores):
    unordered_products = []
    for store in all_stores:
        for product in store.get_products():
            unordered_products.append(StoreProduct(product.get_sku(), product.get_serial(), product.get_condition(), product.get_price(), store.get_name()))
    logging.debug(len(unordered_products))

    ordered = insertsort(unordered_products)

    return ordered

def find_products(file_name):
    logging.basicConfig(level=logging.INFO)
    f = open(file_name, "r")
    index = f.read()
    S = BeautifulSoup(index, 'lxml')

    logging.debug(S.prettify())

    tables = S.find_all('table')
    divs = S.find_all('div')
    stock = []
    for tbl in tables:
        logging.debug(f"""**********
{str(tbl)}
*************************

        """)
        if 'demo' in tbl['class']:
            arr_prd = []
            rows = tbl.find_all('tr')
            for row in rows[1:]:
                    lchild = list(row.children)
                    condition = list(lchild[5].children)[2].strip()
                    prd = Product(lchild[1].string, lchild[3].string, condition, lchild[7].string)
                    arr_prd.append(prd)
                    logging.debug(f"""
******
{prd}
********
""")
            # getting store names
            divs = tbl.parent.parent.parent.parent.parent
            if len(divs) == 2:
                i = 0
                for div in divs:
                    spans = div.find_all('span')
                    if len(spans) == 1:
                        store_name = spans[0].text
                        store = Store(store_name)
                        logging.debug(store_name)
                        store.set_products(arr_prd)
                        stock.append(store)

    for store in stock:
        logging.debug(f"""
******
{store}
********
""")
    logging.info(f"number of stores: {len(stock)}")
    ordered = sort_products_ascending(stock)

    return ordered

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    f = open("sm57 uni_2025-01-27.txt", "r")
    index = f.read()
    S = BeautifulSoup(index, 'lxml')

    logging.debug(S.prettify())

    tables = S.find_all('table')
    divs = S.find_all('div')
    stock = []
    for tbl in tables:
        logging.debug(f"""**********
{str(tbl)}
*************************

        """)
        if 'demo' in tbl['class']:
            arr_prd = []
            rows = tbl.find_all('tr')
            for row in rows[1:]:
                    lchild = list(row.children)
                    condition = list(lchild[5].children)[2].strip()
                    prd = Product(lchild[1].string, lchild[3].string, condition, lchild[7].string)
                    arr_prd.append(prd)
                    logging.debug(f"""
******
{prd}
********
""")
            # getting store names
            divs = tbl.parent.parent.parent.parent.parent
            if len(divs) == 2:
                i = 0
                for div in divs:
                    spans = div.find_all('span')
                    if len(spans) == 1:
                        store_name = spans[0].text
                        store = Store(store_name)
                        logging.debug(store_name)
                        store.set_products(arr_prd)
                        stock.append(store)

    for store in stock:
        logging.debug(f"""
******
{store}
********
""")
    logging.info(f"number of stores: {len(stock)}")


    ordered = sort_products_ascending(stock)



"""         
Need to do sorting with lowest prices~
spreadsheet export
commandline search query and options
combining functionality of main and summarize in one program

Data structure goals -- create a spreadsheet
print lowest price with location
default ordering is by stock at location.

Location    Price   Condition   SKU     Serial





"""
