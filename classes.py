class Carros:
    def __init__(self, marca, modelo, kms):
        self.marca = marca
        self.modelo = modelo
        self.kms = kms

    def __str__(self):
        return f"{self.marca} {self.modelo} com {self.kms} kms"


class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def __str__(self):
        return f"{self.nome} - {self.idade} anos - {self.altura}m"
