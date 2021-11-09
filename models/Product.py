import csv


class Products:
    def __init__(self, products):
        self.products = products

    def add(self, product):
        self.products.append(product)

    def save_to_csv(self):
        fieldnames = ['name', 'price', 'rating', 'store', 'image']
        rows = [product.dictionarize() for product in self.products]

        with open('products.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        print('csv created')


class Product:
    def __init__(self, name, store, price, rating, image):
        self.name = name
        self.store = store
        self.price = price
        self.rating = rating
        self.image = image

    def print_out(self):
        print("[\n" +
              "\tname:" + self.name + "\n" +
              "\tprice:" + self.price + ",\n" +
              "\tstore:" + self.store + ",\n" +
              "\timage:" + self.image + ",\n" +
              "\trating:" + self.rating + "\n" +
              "]"
              )

    def dictionarize(self):
        obj = {'name': self.name, 'price': self.price, 'rating': self.rating, 'store': self.store, 'image': self.image}

        return obj
