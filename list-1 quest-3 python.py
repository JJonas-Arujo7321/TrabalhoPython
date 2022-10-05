v = int(input('Digite o ganho por hora: '))

h = int(input('horas trabalhadas ao mes: '))

s = v * h
ir = (11/100.0 * s)
print ('Imposto de renda: ',ir)

inss = (8/100.0 * s)
print ('INSS: ',inss)

sind = (5/100.0 * s)
print ('Sindicato: ',sind)

desc = ir + inss + sind
sL = s - desc

print ('O desconto total do salario bruto(',s,'R$)','foi',desc,'\nO salario liquido ficou,',sL)