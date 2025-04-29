class Bank:
    """
    A class representing a bank with a class variable for the bank name and a class method to modify it.
    Attributes:
        bank_name (str): The name of the bank. This is a class variable shared across all instances.
    """

    bank_name: str = 'ABC Bank'

    @classmethod
    def change_bank_name(cls, name: str):
        """Changes the name of the bank by modifying the class variable `bank_name`."""
        cls.bank_name = name
        print(f'Bank name has been changed to: {cls.bank_name}')

if __name__ == '__main__':
    b1 = Bank()
    b2 = Bank()
    print(f'Intial Bank name (bank1): {b1.bank_name}')
    Bank.change_bank_name('XYZ Bank')
    print(f'Updated Bank name (bank2): {b2.bank_name}')