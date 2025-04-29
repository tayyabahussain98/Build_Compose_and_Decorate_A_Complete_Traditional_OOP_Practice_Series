class Car:
    """
    A class to represent a Car with a public variable and method.
    Attributes:
        brand (str): The brand of the car.
    """

    def __init__(self, brand: str):
        self.brand = brand

    def start(self):
        """Public method to simulate starting the car."""
        print(f'The {self.brand} car has started..')

if __name__ == '__main__':
    car_1 = Car('Toyota')
    print(car_1.brand)
    car_1.start()