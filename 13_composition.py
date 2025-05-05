class Engine:

    """Represents an engine with basic functionality."""

    def start(self):

        """Simulates starting the engine."""

        print('Engine has started!')

    def stop(self):

        """Simulates stopping the engine."""

        print('Engine has stopped!')

class Car:

    """Represents a car that uses an Engine object.
    Attributes:
        engine (Engine): The engine of the car.
    """
    
    def __init__(self, engine: Engine):
        self.engine = engine

    def start_car(self):

        """Starts the car by starting the engine."""

        return self.engine.start()

    def stop_car(self):

        """Stops the car by stopping the engine."""

        return self.engine.stop()

if __name__ == '__main__':
    my_engine = Engine()
    my_car = Car(my_engine)
    
    my_car.start_car()
    my_car.stop_car()