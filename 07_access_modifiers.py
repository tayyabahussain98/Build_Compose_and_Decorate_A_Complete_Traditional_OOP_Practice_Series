class Employee:
    """
    Employee class represents an employee with a name, salary, and social security number (SSN).
    Attributes:
        name (str): The name of the employee.
        _salary (int): The salary of the employee (protected).
        __ssn (str): The social security number of the employee (private).
    """
    
    def __init__(self, name: str, salary: int, ssn: str):
        self.name = name    # Public Variable
        self._salary = salary   # Protected Variable
        self.__ssn = ssn    # Private Variable

if __name__ == '__main__':
    employee = Employee('Jhon', 50000, '123-45-6789')

    print(f'Name (Public): {employee.name}')
    print(f'Salary (Protected): {employee._salary}')

    try:
        print(f'SSN (Private): {employee.__ssn}')

    except AttributeError as e:
        print(f'Error accessing private variable: {e}')