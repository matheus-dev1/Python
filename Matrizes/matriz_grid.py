#! python3

#matriz_grid

#O programa fazer uma grade com as listas para representar uma matrix de 6 x 9.

Grid = [
['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

#Temos uma Matriz de 9 por 6!
#..OO.OO..
#.OOOOOOO.
#.OOOOOOO.
#..OOOOO..
#...OOO...
#....O....

print('Temos uma Matriz de:',len(Grid[0][:]) * len(Grid),'[6 x 9]')

for Linha in range(0, 6):
    for Coluna in range(0, 9):
        print(Grid[Coluna][Linha], end = '')
    print()
