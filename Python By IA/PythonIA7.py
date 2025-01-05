class Coche:
    def __init__(self, modelo, marca, año):
        self.modelo = modelo
        self.marca = marca
        self.año = año

    def describir(self):
        print(f"El coche es un {self.modelo} de la marca {self.marca} del año {self.año}")

class CocheElectrico(Coche):
    def __init__(self, modelo, marca, año, autonomia):
        super().__init__(modelo, marca, año)  # Llama al constructor de la clase base
        self.autonomia = autonomia

    def mostrar_autonomia(self):
        print(f"La autonomía del coche es de {self.autonomia} km")

mi_coche_electrico = CocheElectrico("Modelo 3", "Tesla", 2022, 500)
mi_coche_electrico.describir()
mi_coche_electrico.mostrar_autonomia()



   


















