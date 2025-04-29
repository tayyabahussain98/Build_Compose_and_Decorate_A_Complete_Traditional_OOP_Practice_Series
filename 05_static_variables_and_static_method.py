class MathUtils:
    """
    A utility class for performing basic mathematical operations.
    """

    @staticmethod
    def add(a: int, b: int)-> int:
        """Return sum of `a` and `b`"""
        return a + b

if __name__ == '__main__':
    result = MathUtils.add(20, 50)
    print(f'The sum of 20 and 50 is: {result}')