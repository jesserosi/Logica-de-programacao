
#Quanto vc ganha por hora?

salario_hora = int(input("Quanto você ganha por hora?"))


#Quantas horas trabalha por mês?

hora_trabalhada = int(input("Quantas horas trabalhou no ultimo mês?"))

#Salário recebido

salario_mes = salario_hora * hora_trabalhada
print(salario_mes)

#Impostos: IR 11%, INSS 8%, sintdicato 5%
divisor=100
inss_multiplicacao = salario_mes*8
inss= inss_multiplicacao/divisor

print(inss)

ir_multiplicação = salario_mes*11
ir= ir_multiplicação/divisor

print(ir)

sindicato_multiplicação = salario_mes*5
sindicato=sindicato_multiplicação/divisor

print(sindicato)




##Salário bruto
##Salário líquido
##IR
##INSS
##Sindicato