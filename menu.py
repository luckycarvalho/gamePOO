from monstro import monstros, Monstro
from animal import animais, Animal
class Menu:
    def __init__(self):
        self.personagens = {"Animal": animais, "Monstro": monstros}
        self.cenarios = ["Floresta", "Caverna"]
        
    def escolher_personagem(self):
        # essa função exibe a lista de personagens disponíveis    
        def personagens(tipo):
            # O parâmetro "tipo" armazena a chave/key do dicionário em self.personagens
            print(f"Escolha um {tipo}")
            # essa variável armazena os valores da chave/key do dicionário
            personagens_disponiveis = self.personagens[tipo]
            
            for i in range(len(personagens_disponiveis)):
                print(f"{i} - {personagens_disponiveis[i].nome}")
            
            num_personagem = int(input(f"Digite o número do {tipo}: "))
            
            if num_personagem < 0 or num_personagem >= len(personagens_disponiveis):
                raise ValueError("Digite um número válido")
            
            return personagens_disponiveis[num_personagem] 
        # define o tipo de criatura: Animal ou Monstro
        print("Escolha uma criatura para jogar")
        for key in self.personagens.keys():
            print(key)
        
        tipo_criatura = input("Digite o tipo da criatura: ")
        
        if tipo_criatura not in self.personagens:
            raise ValueError("Digite um tipo válido")
        
        return personagens(tipo_criatura)
             
    def definir_habitat(self):
        
        print("Escolha um cenário para a batalha")
        
        for key, value in enumerate(self.cenarios):
           print(f"{key} - {value}")
           
        num = int(input("Digite o número do cenário: "))
        #validação
        while num < 0 or num > (len(self.cenarios) - 1):
            print("Digite um número válido")
            num = int(input("Digite o número do cenário: "))
        return self.cenarios[num]
        
    
   