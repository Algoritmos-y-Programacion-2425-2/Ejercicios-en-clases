class Caballo:
    def __init__(self, numero, nombre):
        self.__identificacion = numero
        self.nombre = nombre

    def run(self):
        pass

    def get_identificacion(self):
        return self.__identificacion
    
    def set_identificacion(self, new_identificacion):
        self.__identificacion = new_identificacion