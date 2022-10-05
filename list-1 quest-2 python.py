
p = int(input("Digite o Peso do Peixe:"))

pex = 0

m = 4 * pex

if p > 50:
    
 pex = p - 50
 
 m = pex * 4
 
 
 print('Limite de pescado ULTRAPASSOU em:', pex, '\nKg. multa: R$', m)
else:
 print('PESO APROVADO')
 