class Counter:
    """
    A class to keep track of the number of instances created.
    Attributes:
        count (int): A class-level attribute that keeps track of the total number of Counter instances.
    """
     
    count: int = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f'Total objects created: {cls.count}')

if __name__ == '__main__':
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()

    Counter.show_count()