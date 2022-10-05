
s = int(input("Informe a Sexualidade: 1 - Sexo Masculino | 2 - Sexo Feminino: "))
h = float(input('Informe sua Altura (Ex.: 1.70):'))
p = float(input('Informe seu Peso (Em Kg):'))

p_i = (72.7 * h ) - 58 if s == 1 else (62.1 * h ) - 44.7


if p < p_i:
    print("Abaixo do peso ideal!")
        	
elif p == p_i:
    print("Dentro do peso ideal!")
        	
else:
    print("Acima do peso ideal!")
    	
print ('Peso: %.2f / Peso ideal: %.2f ' %(p, p_i))