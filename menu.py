from monstro import monstros, Monstro
from animal import animais, Animal
class Menu:
    def __init__(self):
        self.personagens = ["Animal", "Monstro"]
        self.cenarios = ["Floresta", "Caverna"]
        self._personagem_jogador = str
        self._personagem_inimigo = str
        
    @property
    def personagem_jogador(self):
        return self._personagem_jogador
    
    @property
    def personagem_inimigo(self):
        return self._personagem_inimigo
    
    @property
    def habitat_batalha(self):
        return self._habitat_batalha
    
    def definir_personagem(self):
        print("Escolha uma criatura para jogar")
        for key, value in enumerate(self.personagens):
           print(f"{key} - {value}")
                   
        num_criatura = int(input("Digite o número da criatura: "))
        
        while num_criatura < 0 or num_criatura > (len(self.personagens) - 1):
            print("Digite um número válido")
            num_criatura = int(input("Digite o número da criatura: "))
            
        if self.personagens[num_criatura] == "Animal": 
            
            for i in range(len(animais)):
                print(f"{i} - {animais[i].nome}")
        
            num_personagem = int(input("Digite o número do personagem: "))
            
            while num_personagem < 0 or num_personagem > (len(animais) - 1):
                 print("Digite um número válido")
                 num_personagem = int(input("Digite o número do personagem: "))
         
            self._personagem_jogador = animais[num_personagem]     
            
        elif self.personagens[num_criatura] == "Monstro":
            
            for i in range(len(monstros)):
                print(f"{i} - {monstros[i].nome}")
                
            num_personagem = int(input("Digite o número do personagem: "))
            
            while num_personagem < 0 or num_personagem > (len(animais) - 1):
                 print("Digite um número válido")
                 num_personagem = int(input("Digite o número do personagem: "))
                 
            self._personagem_jogador = monstros[num_personagem]
        
    def definir_inimigo(self):
        print("Escolha uma criatura como inimigo: ")
        
        for key, value in enumerate(self.personagens):
            print(f"{key} - {value}")
        
        criatura_inimiga = int(input("Digite o número da criatura: "))
        
        while criatura_inimiga < 0 or criatura_inimiga > (len(self.personagens) - 1):
            print("Digite um número válido")
            criatura_inimiga = int(input("Digite o número da criatura: "))
        
        if self.personagens[criatura_inimiga] == "Animal":
            personagem_impresso = False
            for i in range(len(animais)):
                if animais[i] != self._personagem_jogador:
                    # Verifica se os inimigos são 2x mais fortes que o jogador
                    if (self.personagem_jogador.calcular_nivel() * 2) >= animais[i].calcular_nivel():  
                        print(f"{i} - {animais[i].nome}")
                        personagem_impresso = True
            if not personagem_impresso:
                print("Todos os animais são muito fortes!")
            else:
                num_inimigo = int(input("Digite o número do personagem inimigo: "))
                self._personagem_inimigo = animais[num_inimigo]
            
        elif self.personagens[criatura_inimiga] == "Monstro":
            personagem_impresso = False
            for i in range(len(monstros)):
                if monstros[i] != self._personagem_jogador:
                    if (self.personagem_jogador.calcular_nivel() * 2) >= monstros[i].calcular_nivel(): 
                        print(f"{i} - {monstros[i].nome}") 
                        personagem_impresso = True
            if not personagem_impresso:
                print("Todos os monstros são muito fortes!")
            else:
                num_inimigo = int(input("Digite o número do personagem inimigo: "))      
                self._personagem_inimigo = monstros[num_inimigo]
                
    def definir_habitat(self):
        
        print("Escolha um cenário para a batalha")
        
        for key, value in enumerate(self.cenarios):
           print(f"{key} - {value}")
           
        num = int(input("Digite o número do cenário: "))
        
        while num < 0 or num > (len(self.cenarios) - 1):
            print("Digite um número válido")
            num = int(input("Digite o número do cenário: "))
        self._habitat_batalha = self.cenarios[num]
        self.__verificar_habitat()
    
    def __verificar_habitat(self):
        if self.personagem_jogador.habitat == self.habitat_batalha:
            self._personagem_jogador.vida += 10
            self._personagem_jogador.forca += 5
            self._personagem_jogador.defesa += 10
        elif self.personagem_inimigo == self.habitat_batalha: 
            self._personagem_inimigo.vida += 10
            self._personagem_inimigo.forca += 5   
            self._personagem_inimigo.defesa += 10
            