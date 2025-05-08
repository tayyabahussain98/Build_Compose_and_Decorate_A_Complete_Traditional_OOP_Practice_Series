class Multiplier:

    """
    A callable class that multiplies a given number by a predefined factor.            
    """

    def __init__(self, factor: int):
        self.factor = factor

    def __call__(self, num: int):

        """Multiplies the input number by the factor and returns the result."""

        return self.factor * num
    
if __name__ == '__main__':
    object = Multiplier(5)

    print(f'5 multiply by 4 is {object(4)}')
    print(f'5 multiply by 7 is {object(7)}')
    print(f'Object is callable {callable(object)}')