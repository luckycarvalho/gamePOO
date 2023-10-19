from criatura import Criatura
from random import randint
class Animal(Criatura):
    def __init__(self, nome, tipo, habitat, vida, forca, defesa, tamanho, velocidade):
        super().__init__(nome, tipo, habitat, vida, forca, defesa)
        self.tamanho = tamanho
        self.velocidade = max(min(velocidade, 50), 1)
        self.bonus()

    def imprimir_animal(self):
        super().imprimir()
        print(f"Tamanho: {self.tamanho}")
        print(f"Velocidade: {self.velocidade}")

    def get_tipo_completo(self):
        return f"{self.tipo} ({self.habitat})"
    
    def bonus(self):
        # Bonus de velocidade e forca de acordo com o tamanho do animal
        if self.tamanho == "Grande":
            self.forca += 10
            self.velocidade -= 10
        elif self.tamanho == "Pequeno":
            self.forca -= 10
            self.velocidade += 10
    
    def desviar(self):
        #Bonus de velocidade de acordo com o tamanho do animal
        if self.tamanho == "Pequeno":
            chance = randint(0, 75)
        else: 
            chance = randint(0, 100)
            
        if chance <= self.velocidade:
            print(f'{self.nome} desviou do ataque!')
            return True
        else:
            print(f"{self.nome} não conseguiu desviar do ataque!")
            return False

animais = [
    Animal("Tigre", "Animal", "Floresta", 550, 190, 40, "Medio", 40),
    Animal("Macaco", "Animal", "Floresta", 150, 100, 20, "Pequeno", 50),
    Animal("Gorila", "Animal", "Floresta", 600, 180, 100, "Grande", 20),
    Animal("Seno", "Animal", "Caverna", 420, 140, 100, "Medio", 50),
    Animal("Zezinho", "Animal", "Floresta", 1000, 200, 20, "Medio", 50),
]