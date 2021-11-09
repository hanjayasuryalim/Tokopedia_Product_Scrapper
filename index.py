import tools
import models
import time
import pickle


def get_all_cards(target):
    total_cards = []
    driver = tools.Driver()
    paginate = 1

    while len(total_cards) != target:
        url = 'https://www.tokopedia.com/search?navsource=home&page={page}&q=handphone&st=product'.format(page=paginate)
        driver.go_to(url)

        for i in range(10):
            driver.web_driver.execute_script('window.scrollBy(0, window.innerHeight);')
            time.sleep(5)

        soup = driver.get_soup()
        body = soup.find('div', {'id': 'zeus-root'})

        cards = body.find_all('div', {'class': 'css-12sieg3'})

        for card in cards:
            if len(total_cards) != target:
                total_cards.append(card)
            else:
                break
        paginate += 1

    driver.close()
    return total_cards


def extract_to_products(elements):
    products_temp = models.Products([])

    for card_element in elements:
        image = card_element.find_all('img')[0]['src']
        name = card_element.find('div', {'data-testid': 'spnSRPProdName'}).text
        price = card_element.find('div', {'data-testid': 'spnSRPProdPrice'}).text
        store = card_element.find_all('span', {'class': 'css-qjiozs'})[-1].text
        rating = card_element.find('span', {'class': 'css-etd83i'})
        rating = rating.text if rating is not None else 'not yet rated'

        products_temp.add(models.Product(name, store, price, rating, image))

    return products_temp


def save_into_pickle(filename, data):
    picklefile = open(filename, 'wb')
    pickle.dump(data, picklefile)
    picklefile.close()


def load_pickle(filename):
    with open(filename,'rb') as picklefile:
        data = pickle.load(picklefile)
    return data


if __name__ == '__main__':
    card_elements = get_all_cards(100)
    products = extract_to_products(card_elements)
    save_into_pickle('products.pickle', products)
    products.save_to_csv()
