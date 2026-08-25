peso = float(input("Peso do açaí, em gramas: "))
miii = peso * 0.05
if peso > 500:
    print(f"Você ganhou 15% de desconto! Valor final: R$ {miii * 0.85:.2f}")
else:
    print(f"Valor da compra: R$ {miii:.2f}")

