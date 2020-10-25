#! python3

#ordenar_numeros

#Ordenar quatro numeros em de forma decrescente.

primeiro = int(input('Primeiro numero: '))
segundo = int(input('Segundo numero: '))
terceiro = int(input('Terceiro numero: '))
quarto = int(input('Quarto numero: '))

print ('Ordem Digitada: ', primeiro, ',', segundo, ', ', terceiro, ',', quarto)

if primeiro < segundo:
   aux = primeiro
   primeiro = segundo
   segundo = aux
   
elif primeiro < terceiro:
   aux = primeiro
   primeiro = terceiro
   terceiro = aux
   
elif primeiro < quarto:
   aux = primeiro
   primeiro = quarto
   quarto = aux
 
if segundo < terceiro:
   aux = segundo
   segundo = terceiro
   terceiro = aux
   
elif segundo < quarto:
   aux = segundo
   segundo = quarto
   quarto = aux

if terceiro < quarto:
   aux = terceiro
   terceiro = quarto
   quarto = aux

print ('Ordem Decrescente: ', primeiro, ',', segundo, ',', terceiro, ',', quarto)
