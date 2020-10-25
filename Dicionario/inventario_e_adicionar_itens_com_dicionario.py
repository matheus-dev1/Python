#! python3

#inventario_e_adicionar_itens_com_dicionario

#Jogos de Fanstasia, mostrar no inventario e adicionando o loot do dragao ao inventario.

Inventory = {'Wood Sword': 1, 'Gold Coin': 1, 'Silver Coin': 54, 'Bronze Coin': 91, 'Helmet': 1}

DragonLoot = ['Gold Coin', 'Dagger', 'Shield', 'Gold Coin']

def DisplayInventory(Inventory_def):
    Tot_Items = 0
    for Items, Qtd_Items in Inventory_def.items():
        print(str(Items) + ': ' + str(Qtd_Items))
        Tot_Items += Qtd_Items
    print('Total de Items: ', end = '')
    return Tot_Items

def addToInventory(Inventory_def, AddedItems):
    for Loot in DragonLoot:
        Inventory_def.setdefault(Loot, 0)
        Inventory_def[Loot] = Inventory_def[Loot] + 1
    return Inventory_def

print('Inventory: ' )
print(DisplayInventory(Inventory))
print("\n")
print('Inventory: ')
Inventory = addToInventory(Inventory, DragonLoot)
print(DisplayInventory(Inventory))
