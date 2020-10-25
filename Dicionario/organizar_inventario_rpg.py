#! python3

#organizar_inventario_rpg

#O programa exibe um iventorio, da forma em que usuario dizer.

Itens = {'Sword': 1, 'Head': 2, 'Scroll': 32, 'Shield': 1, 'Pet (Dragonete)': 1, 'Gold': 3, 'Silver': 1, 'Bronze': 98}

def InventoryShow(ItensOrg, EsquerdaOrg, DireitaOrg):
    print('Your Bag'.center(EsquerdaOrg + DireitaOrg))
    for ItensOrg, Qtd in ItensOrg.items():
        print(ItensOrg.ljust(EsquerdaOrg) + str(Qtd).rjust(DireitaOrg))

while True:
    Esquerda = int(input('Espacos a Esquerda: '))
    Direita = int(input('Espacos a Direita: '))

    InventoryShow(Itens, Esquerda, Direita)
    
    Exit = input('Deseja sair? [S/N]: ')
    if Exit.lower() == 's':
        break
    else:
        continue
