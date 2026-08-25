i = float(input("Valor total da conta, em reais: "))
p = int(input("Total de pessoas: "))
n = input("Responda com 'sim' ou 'não'; você deseja pagar a taxa de serviço de 10% do garcom? ")
h = i / p
if n == "sim":
    print(f"O total a ser pago por pessoa é de {h * 1.1:.2f} reais.")
elif n == "não":
    print(f"O total a ser pago por pessoa é de {h:.2f} reais.")
else:
    print("Resposta inválida.") 