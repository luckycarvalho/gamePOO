from criatura import Criatura
class Monstro(Criatura):
    def __init__(self, nome, tipo, habitat, vida, forca, defesa, resistencia):
        super().__init__(nome, tipo, habitat, vida, forca, defesa)
        self.resistencia = max(min(resistencia, 50), 0)
        self.bonus()

    def imprimir_monstro(self):
        super().imprimir()
        print(f"Resistencia: {self.resistencia}")

    def bonus(self):
        # bonus pela resistencia do monstro
        self.defesa += (self.resistencia * (50/100))
        
monstros = [
    Monstro("Zood", "Monstro", "Caverna", 600, 190, 90, 50),
    Monstro("Void", "Monstro", "Floresta", 500, 150, 100, 50), 
    Monstro("Drácula", "Monstro", "Caverna", 1000, 120, 60, 30),
    Monstro("Cuca", "Monstro", "Caverna", 400, 110, 100, 20), 
    Monstro("Bruxa", "Monstro", "Floresta", 700, 130, 80, 10),
    Monstro("Bronks", "Monstro", "Caverna", 200, 200, 100, 50)
]