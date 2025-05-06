class Employee:
    
    """Represents an employee with a name and an ID.
    Attributes:
        name (str): The name of the employee.
        emp_id (int): ID of the employee.
    """

    def __init__(self, emp_name: str, emp_id: int):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def __repr__(self):
        return f'Employee(Emp_Name: {self.emp_name}, ID: {self.emp_id})'
    
class Department:

    """Represents a department that aggregates an Employee object.
    Attributes:
        dept_name (str): The name of the Department.
        employee (Employee): An instance of the Employee class associated with the department.
    """

    def __init__(self, dept_name: str, employee: Employee):
        self.dept_name = dept_name
        self.employee = employee

    def __repr__(self):
        return f'Department(Dept_Name: {self.dept_name}, Employee: {self.employee})'
    
if __name__ == '__main__':
     emp_1 = Employee('Jhon', 101)
     dept_1 = Department('HR', emp_1)
     print(dept_1)