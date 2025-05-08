def add_greeting(cls):
    
    """
    A class decorator that adds a 'greet' method to the class.
    """

    def greet(self):

        """
        A greeting method added by the decorator.
        
        Returns:
            str: A greeting message.
        """

        return 'Hello from Decorator!'
    
    cls.greet = greet

    return cls

@add_greeting
class Person:

    """
    A simple class representing a person.
    
    Attributes:
        name (str): The name of the person.
    """

    def __init__(self, name: str):

        """
        Initializes a Person instance with a name.
        
        Args:
            name (str): The name of the person.
        """
        
        self.name = name


if __name__ == '__main__':
    # Create an instance of Person and call the greet method
    obj = Person('Tayyaba')
    print(obj.greet())