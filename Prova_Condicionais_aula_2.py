while True: 
    velocidade = int(input("Qual a velocidade do carro? "))

    if velocidade > 80:
        multa = (velocidade - 80) * 7
        print(f"Você foi multado! O valor da multa é R${multa}")
    else:
        print("Parabéns, você está dentro do limite de velocidade!")

    print("-" * 40)  # separar uma execução da outra
