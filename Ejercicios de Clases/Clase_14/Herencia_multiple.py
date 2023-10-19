class Cetaceo:
    def __init__(self, notas, viveEn, peso):
        self.notas = notas
        self.viveEn = viveEn
        self.peso = peso
    
    def nacer():
        return "Ha nacido"
    
    def nadar():
        return "Puede nadar"
    
class Mamifero(Cetaceo):
    def __init__(self, cantMamas, espereranzaDeVida):
        super().__init__(self, notas, viveEn, peso)
        self.cantMamas = cantMamas
        self.esperanzaDeVida = espereranzaDeVida
        
    def mamar():
        return "Puede mamar"
    
        
class AnimalMarino(Cetaceo):
    def __init__(self, tieneBranqueas, especie):
        super().__init__(self, notas, viveEn, peso)
        self.tieneBranqueas = tieneBranqueas
        self.especie = especie

ballena_azul = Mamifero("Animal mas grande de todos", "Oceano", 110000, 2, 100)
