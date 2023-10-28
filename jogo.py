from menu import Menu
from random import randint
from time import sleep
class Jogo:
    def __init__(self):
        self.__menu = Menu()
        self.__jogador = object
        self.__inimigo = object
        
    @property
    def jogador(self):
        return self.__jogador
    
    @property
    def inimigo(self):
        return self.__inimigo
          
    def __definir_personagens(self):
        
        def escolher_jogador():
            print(30 * "=")
            print(5 * " ", "Definindo jogador")
            print(30 * "=")
            self.__jogador = self.__menu.escolher_personagem()
            
        def escolher_inimigo():
            print(30 * "=")
            print(5 * " ", "Definindo inimigo:")
            print(30 * "=")
            self.__inimigo = self.__menu.escolher_personagem()
            
        #imprime os atributos do personagem e valida a escolha do jogador    
        def confirmar(personagem):
            while True:
                print(30 * "=")
                print(5 * " ", "Dados do personagem")
                print(30 * "=")
                personagem.imprimir()
                confirm = input("Deseja escolher outro personagem?").lower().strip()
                if confirm in ["sim", "s"]:
                    print()
                    if personagem == self.__jogador:
                        escolher_jogador()
                    else:
                        escolher_inimigo()
                else:
                    break
                
        escolher_jogador()
        confirmar(self.__jogador)
        
        escolher_inimigo()
        confirmar(self.__inimigo) 
               
        self.__verificar_nivel(self.__jogador, self.__inimigo)
        
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
                    #Exibe uma mensagem da decisão do personagem
                    if criatura == self.jogador:
                        print()
                        print("Você decidiu atacar!")
                        sleep(1)
                    else:
                        print()
                        print("O inimigo decidiu atacar!")
                        sleep(1)
                        
                    criatura.atacar(adversario)
                    sleep(1)
                elif movimento == "d":
                    if criatura == self.jogador:
                        print()
                        print("Você decidiu defender!")
                        sleep(1)
                    else:
                        print()
                        print("O inimigo decidiu defender!")
                        sleep(1)
                        
                    criatura.defender(adversario)
                    sleep(1)
            else:
                return False
            return True
        # laço para que o jogador controle a luta
        while True:
            print()
            movimento_jogador = input("Digite 'A' para atacar ou 'D' para defender: ").lower().strip()
            
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
            
    def __verificar_nivel(self, jogador, inimigo):
        # Verifica se o inimigo é 2x mais forte que o jogador
        if (jogador.calcular_nivel() * 2) <= inimigo.calcular_nivel():
            continar = input("Seu inimigo é muito forte, deseja continuar? ").lower().strip()
            if continar in ["não", "nao", "n"]:
                self.__inimigo = self.__menu.escolher_personagem()  
        # verifica se o jogador é 2x mais forte que o inimigo              
        elif (inimigo.calcular_nivel() * 2) <= jogador.calcular_nivel():
            continar = input("Seu inimigo é muito fraco, deseja continuar? ").lower().strip()
            if continar in ["não", "nao", "n"]:
                self.__inimigo = self.__menu.escolher_personagem()  
                
    def iniciar(self):
       self.__definir_personagens()
       self.__definir_cenario()
       self.__lutar()