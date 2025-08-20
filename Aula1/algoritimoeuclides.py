#Algorítimo
# AULA 13 - Exercícios de lógica de programação
# Algorítimo de Euclides



'''crie um programa que leia dois numeros inteiros substitua o maior pela diferença e escreva ambos no console'''

# Algoritmo de Euclides usando subtração

# Lê dois números inteiros
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# Enquanto não forem iguais, substitui o maior pela diferença
while primeiro_numero  != segundo_numero:
    if primeiro_numero  > segundo_numero:
        primeiro_numero  = primeiro_numero  - segundo_numero
    else:
        segundo_numero = segundo_numero - primeiro_numero

# Quando iguais, imprime o resultado
print("Os números ficaram iguais:", primeiro_numero , segundo_numero)





#opção
#elif segundo_numero > primeiro_numero 
      #segundo_numero = segundo_numero - primeiro_numero
      #while = loop enquanto não chegar no que eu quero ele repete
      #contador = 0
#while contador < 11:
   #print(contador)
   #contador = contador + 1