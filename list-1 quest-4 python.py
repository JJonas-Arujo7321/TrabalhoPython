t = float(input("Informe em Metros Quadrados:"))

li = t / 3.0
la = int(li / 18.0)

if li % 18 != 0:
    la += 1

print('É necessario comprar', la, 'latas.')

print('Valor total:', la * 80)