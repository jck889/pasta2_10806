class Carros:
    def __init__(self, marca, modelo, kms):
        self.marca = marca
        self.modelo = modelo
        self.kms = kms

    def __str__(self):
        return f"{self.marca} {self.modelo} com {self.kms} kms"
