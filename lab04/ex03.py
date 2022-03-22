class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Calculator:
    __rand = 0.3
    _EUR = 4.60
    _USD = 4.20

    def getPriceInUSD(self, product):
        return round(product.price / Calculator._USD, 2)

    def getPriceInEuro(self, product):
        return round(product.price / Calculator._EUR, 2)

    def getPriceInUSDWithRand(self, product):
        return self.getPriceInUSD(product) + self.getPriceInUSD(product) * Calculator.__rand

    def getPriceInEuroWithRand(self, product):
        return self.getPriceInEuro(product) + self.getPriceInEuro(product) * Calculator.__rand

products = []
products.append(Product("sianokiszonka", 123))
products.append(Product("nawoz", 32))
products.append(Product("kurczak", 500))

calculator = Calculator()
for product in products:
    print(product.name)
    print(calculator.getPriceInUSD(product), "$")
    print(calculator.getPriceInUSDWithRand(product), "$ (with rand)")
    print()