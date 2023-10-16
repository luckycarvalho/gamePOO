from menu import Menu
from random import randint
from time import sleep
class Jogo:
    def __init__(self):
        self.__menu = Menu()
        
    def escolher_personagens(self):
        # Escolhendo personagens
        self.__menu.definir_personagem()
        while True:
            print(30*"=")
            print("Atributos do personagem:")
            print(30*"=")
            self.__menu.personagem_jogador.imprimir()
            print("\n0 - (SIM)\n1 - (NÃO)")
            confirm = int(input("Deseja escolher outro personagem? "))
            
            while confirm < 0 or confirm > 1:
                print("Digite uma opção válida")
                print("0 - (SIM)\n1 - (NÃO)")
                confirm = int(input("Deseja escolher outro personagem? "))
            if confirm == 0:
                self.__menu.definir_personagem()
            else:
                break
            
        print()    
        self.__menu.definir_inimigo()
        while True:
            print(30*"=")
            print("Atributos do inimigo:")
            print(30*"=")
            self.__menu.personagem_inimigo.imprimir()
            print("\n0 - (SIM)\n1 - (NÃO)")
            confirm = int(input("Deseja escolher outro inimigo? "))
            
            while confirm < 0 or confirm > 1:
                print("Digite uma opção válida")
                print("0 - (SIM)\n1 - (NÃO)")
                confirm = int(input("Deseja escolher outro inimigo? "))
            if confirm == 0:
                self.__menu.definir_inimigo()
            else:
                break
        
    def escolher_cenarios(self):
        print()
        self.__menu.definir_habitat()
    
    def lutar(self):
        jogador = self.__menu.personagem_jogador
        inimigo = self.__menu.personagem_inimigo
        print()
        print(10 * "=", "BATALHA", 10 * "=")
        # teste de batalha
        while True:
            print("iniciando...")
            sleep(.5)
            print("Agora é a sua vez!")
            print()
            print("Digite 'A' para atacar...")
            
            while jogador.vida > 0 and inimigo.vida > 0:
                movimento_inimigo = randint(0, 1)
                movimento_jogador = input("...").lower()
                   
                if movimento_jogador == 'd':
                    print("Você decidiu defender!")
                    sleep(1)
                    jogador.defender(inimigo) 
                    print("...")
                    sleep(1) 
                elif movimento_jogador == 'a': 
                    print("Você decidiu atacar!")
                    sleep(1) 
                    jogador.atacar(inimigo)
                    print("...")
                    sleep(1)
                else:
                    while True:
                        print("Opção inválida!")
                        movimento_jogador = input("...").lower()
                        if movimento_jogador == 'a' or movimento_jogador == 'd':
                            break
                    
                print("...")
        
                if movimento_inimigo == 0:
                    print(f"{inimigo.nome} decidiu atacar!")
                    sleep(1)
                    inimigo.atacar(jogador)
                    print("...")
                    sleep(1)
                else:
                    print(f"{inimigo.nome} decidiu defender!")
                    sleep(1)
                    inimigo.defender(jogador)
                    print("...")
                    sleep(1)
                    
                print("Digite 'A' para atacar ou 'D' para defender...")
                       
            break  
        
        if jogador.vida == 0:
            print()
            sleep(1)
            print("Você perdeu!")
            print()
            sleep(1)
        elif inimigo.vida == 0:
            print()
            sleep(1)
            print(f"{inimigo.nome} perdeu!")
            print()
            sleep(1)
            
        print(f"Informações do jogador:")
        jogador.imprimir()
        print()
        print("Informações do inimigo:") 
        inimigo.imprimir()
    