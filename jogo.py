from menu import Menu
class Jogo:
    def __init__(self):
        self.menu = Menu()
    
    def iniciar(self):
        self.menu.definir_personagem()
        while True:
            print(30*"=")
            print("Atributos do personagem:")
            print(30*"=")
            print(self.menu.personagem_jogador.imprimir())
            
            confirm = int(input("Deseja escolher outro personagem?\n0 - Sim\n1 - Não\n: "))
            
            while confirm < 0 or confirm > 1:
                print("Digite uma opção válida")
                confirm = int(input("Deseja escolher outro personagem?\n0 - Sim\n1 - Não\n: "))
            if confirm == 0:
                self.menu.definir_personagem()
            else:
                break
            
        self.menu.definir_inimigo()
            
jogo = Jogo()
jogo.iniciar()
    