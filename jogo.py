from menu import Menu
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
        while jogador.vida > 0 and inimigo.vida > 0:
            jogador.atacar(inimigo)
            inimigo.defender(jogador)
            inimigo.atacar(jogador)
            jogador.defender(inimigo)
        if jogador.vida == 0:
            print("Você perdeu!")
        elif inimigo.vida == 0:
            print(f"{inimigo.nome} perdeu!") 
    