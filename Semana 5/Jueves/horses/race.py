class Carrera:
    def __init__(self, numero, caballos):
        self.numero = numero
        self.caballos_participantes = caballos

    def iniciar_carrera(self):
        print("PARTIDAAAAAAAAAAAAAAAAAAAAA!")
        print("Salieron los competores")
        for caballo in self.caballos_participantes:
            print(f"Caballo numero: {caballo.get_identificacion()} - {caballo.nombre}")
            caballo.nombre = "Pedrito"