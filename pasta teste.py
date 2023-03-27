def conf(a, b, c):
    if (a > 0) and (c > 0) and (c > (a + b)):
        return 1 
    else:
        print('Dados invalidos, tente novamente')
        return 0
    
j = 0
while j == 0:
    tam, min, max = (input("entrada: ").split())
    tam = int(tam)
    min = int(min)
    max = int(max)

    j = conf(tam,min,max)

vetor = []

for i in range(tam):
    vetor.append(min + i)

print(vetor)
