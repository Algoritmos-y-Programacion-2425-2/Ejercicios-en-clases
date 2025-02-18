class Employee:
    def __init__(self,name,dni):
        self.name = name
        self.identification = dni

    def work(self):
        print("I'm working...")

class Writer(Employee):
    def __init__(self, name, dni):
        super().__init__(name, dni)
    
    def work(self):
        print("Writing...")

class Boss(Employee):
    def __init__(self, name, dni):
        super().__init__(name, dni)

    def work(self):
        print("Soy el jefe")

boss = Boss("Antonio",123)
boss.work()