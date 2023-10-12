from monstro import Monstro
from animal import Animal
def teste():
    monstro = Monstro("Zood", "Monstro", "Caverna", 600, 190, 90, 50)
    animal = Animal("Tigre", "Animal", "Floresta", 550, 190, 40, "Medio", 40)
    
    print("Monstro é uma instância de Monstro:", isinstance(monstro, Monstro))
    print("Animal é uma instância de Animal:", isinstance(animal, Animal))

    print("\nInformações do Monstro:")
    monstro.imprimir()

    print("\nInformações do Animal:")
    animal.imprimir()

    print("\n----------------BATALHA---------------")
    for _ in range(10):
        monstro.atacar(animal)
        animal.defender(monstro)
        animal.atacar(monstro)
        monstro.defender(animal)
        if monstro.morreu == True or animal.morreu == True:
            break 

    print("\nInformações do Monstro após a batalha:")
    monstro.imprimir()

    print("\nInformações do Animal após a batalha:")
    animal.imprimir()

teste()
