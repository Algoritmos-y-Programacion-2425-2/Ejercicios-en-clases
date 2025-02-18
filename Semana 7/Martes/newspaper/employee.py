class Employee:
    def __init__(self, name, dni):
        self.name = name
        self.dni = dni

class ChiefWriter(Employee):
    def __init__(self, name, dni):
        super().__init__(name, dni)

    def supervise(self):
        print("Supervising...")

    def publish(self):
        pass

class Writer(Employee):
    def __init__(self, name, dni):
        super().__init__(name, dni)

    def write(self):
        print("Writing...")