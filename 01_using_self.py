class Student:
    """
    A class to represent a student and their exam performance.
    Attributes:
        name (str): The name of the student.
        marks (int): The marks obtained by the student in the exam.            
    """
    
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def display(self):
        """Prints the student's name and their marks in a formatted string."""
        print(f'{self.name.title()} got {self.marks} in exam.')

if __name__ == '__main__':

    s1 = Student('Tayyaba', 89.5)
    s1.display()

    s2 = Student('Najma', 90)
    s2.display()