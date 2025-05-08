class Product:

    """A class to manage product price with property decorators.
    Attributes:
        name (str) : The Name of the product
        price (float) : Price of the product
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price


    @property
    def price(self):
        
        """Get the price of the product."""

        return self._price
    
    @price.setter
    def price(self, price: float):

        """Set the price of the product. Raises ValueError if price is non-positive."""

        if price <= 0:
            raise ValueError('Price cannot be negative or zero')
        self._price = price

    @price.deleter
    def price(self):

        """Delete the price of the product."""

        print('Price deleted!')

        del self._price


if __name__ == '__main__':
    product = Product('Dress', 1000)
    print(f'Current Price: {product.price}')

    product.price = 2000
    print(f'Updated Price: {product.price}')

    del product.price

    # print(product.price)      # Raise AttributeError