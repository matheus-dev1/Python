#! python3

#function_aoQuadrado

vetor = []

def aoQuadradoVetor(vetor, tamVetor):
    for i in range(tamVetor):
        vetor[i] = vetor[i] ** 2
        print(vetor[i])

for i in range(8):
    vetor.append(i)
    print(vetor[i] )

aoQuadradoVetor(vetor, len(vetor))
