from random import randint
class Criatura():
    def __init__(self, nome, tipo, habitat, vida, forca, defesa):
        self.nome = nome
        self.tipo = tipo
        self.habitat = habitat
        self.vida = max(min(vida, 1000), 0)
        self.forca = max(min(forca, 200), 0)
        self.defesa = max(min(defesa, 100), 0)
        self.dano_total = 0

    def get_forca_total(self):
        return round(((self.forca + self.vida) / 2) * 0.4)

    def get_defesa_total(self):
        return (self.vida + self.defesa)
    
    @property
    def morreu(self):
        return self.vida <= 0

    def atacar(self, monstro_alvo):
        if not self.morreu and not monstro_alvo.morreu:
            dano = min(monstro_alvo.vida, self.get_forca_total())
            monstro_alvo.vida -= dano
            print(f"{self.nome} provocou um dano de {dano} no {monstro_alvo.nome}")
        else:
            return

    def defender(self, ataque):
        if not self.morreu and not ataque.morreu:
            if not self.desviar():
                return
            defesa = self.get_defesa_total()
            ataque_inimigo = ataque.get_forca_total()
            if ataque_inimigo >= defesa:
                dano_recebido = (ataque_inimigo - defesa)
                self.vida -= dano_recebido
                print(f"{self.nome} recebeu dano de {dano_recebido}")
                self.defesa -= 1
            else:
                self.vida += ataque_inimigo
                print(f"{self.nome} defendeu o ataque")
        else:
            print(f"{self.nome} morreu!")
            return 
    
    def desviar(self):
        # verifica se a classe possui o atributo velocidade
        if not hasattr(self, "velocidade"): 
            return
        chance = randint(0, 100)
        if chance < self.velocidade:
            print(f'{self.nome} desviou do ataque!')
            return True
        else:
            print(f"{self.nome} não conseguiu desviar do ataque!")
            return False
    
    def calcular_nivel(self):
        return (self.vida + self.forca + self.defesa) // 3 
    def imprimir(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo: {self.tipo}")
        print(f"Habitat: {self.habitat}")
        if not self.morreu:
            print(f"Vida: {self.vida}")
        else:
            print(f"Vida: morto")
        print(f"Forca: {self.forca}")
        print(f"Defesa: {self.defesa}")

