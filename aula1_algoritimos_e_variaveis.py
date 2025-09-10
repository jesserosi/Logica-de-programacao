# Entrada de dados
tempo_servico = int(input("Digite o tempo de serviço em anos: "))
fgts = float(input("Digite o valor do FGTS: "))

# Processamento
if tempo_servico > 1:
    multa = fgts * 0.40
else:
    multa = 0

# Saída
print(f"Tempo de serviço: {tempo_servico} anos")
print(f"Valor do FGTS: R$ {fgts:,.2f}")
print(f"Valor da multa rescisória: R$ {multa:,.2f}")
