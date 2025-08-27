import pycountry

pais= random.randint(1, 100)
tentativas = 0
acertou = False
nome = input("Digite seu nome:")
print("nome")
tentativas_passadas = []


while not acertou:
        try: 
            numero = int(input("Digite um numero de 1 a 100:"))
            tentativas += 1
            tentativas_passadas.append(numero)

            if numero  == numero_aleatorio:
                acertou = True
                print(f"Parabéns! Você acertou.")
                print(tentativas_passadas)
                break
            elif numero < numero_aleatorio:
                 print("muito baixo. Tente novamente")
            elif numero > numero_aleatorio:
                 print("Muito alto. Tente novamete")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")