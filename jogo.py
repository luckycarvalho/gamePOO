from menu import Menu
from random import randint
class Jogo:
    def __init__(self):
        self.__menu = Menu()
        
    @property
    def jogador(self):
        return self.__jogador
    
    @property
    def inimigo(self):
        return self.__inimigo
          
    def __definir_personagens(self):
        print(30 * "=")
        print(5 * " ", "Definindo jogador")
        print(30 * "=")
        self.__jogador = self.__menu.escolher_personagem()
        print(30 * "=")
        print(5 * " ", "Definindo inimigo:")
        print(30 * "=")
        self.__inimigo = self.__menu.escolher_personagem()
        
    def __definir_cenario(self):
        print()
        self.__habitat_batalha = self.__menu.definir_habitat()
        self.__verificar_habitat()
    
    def __lutar(self):
        print(20 * "=")
        print(5 * " ", "BATALHA")
        print(20 * "=")
        # Função que procede a luta caso os personagens estejam vivos, retorna True ou False
        def lutar_criatura(criatura, adversario, movimento):
            if criatura.vida > 0:
                if movimento == "a":
                    criatura.atacar(adversario)
                elif movimento == "d":
                    criatura.defender(adversario)
            else:
                return False
            return True
        # laço para que o jogador controle a luta
        while True:
            movimento_jogador = input("Digite 'A' para atacar ou 'D' para defender: ").lower()
            if movimento_jogador in ["a", "d"]:
                jogador_vivo = lutar_criatura(self.jogador, self.inimigo, movimento_jogador)
            else:
                raise ValueError("Digite um valor válido.")

            movimento_inimigo = "a" if randint(0, 1) == 0 else "d"
            inimigo_vivo = lutar_criatura(self.inimigo, self.jogador, movimento_inimigo)

            if not jogador_vivo:
                print("Você perdeu!")
                break
            elif not inimigo_vivo:
                print("O inimigo perdeu!")
                break
     
    def __verificar_habitat(self):
        #Aumenta os pontos caso o habitat de algum dos personagens seja igual ao do cenário de batalha
        if self.jogador.habitat == self.__habitat_batalha:
            self.jogador.vida += 10
            self.jogador.forca += 5
            self.jogador.defesa += 10
        elif self.inimigo == self.__habitat_batalha: 
            self.inimigo.vida += 10
            self.inimigo.forca += 5   
            self.inimigo.defesa += 10
                
                  
    def iniciar(self):
       self.__definir_personagens()
       self.__definir_cenario()
       self.__lutar()