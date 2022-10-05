i = []
alt = []
for i in range(1, 6):
    print('%dº Pessoa' %i)
    i = int(input('Digite a idade: '))
    alt = float(input('Digite a altura: '))
    i.append(i)
    alt.append(alt)

print('Ordem inversa')
print('Alturas')
print(alt[::-1])

print('Idades')
print(i[::-1])