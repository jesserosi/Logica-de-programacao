soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    if numero == 0:
        break  
    
    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"Quantidade de números digitados: {contador}")
    print(f"Soma dos números: {soma}")
    print(f"Média aritmética: {media}")
else:
    print("Nenhum número foi digitado!")
