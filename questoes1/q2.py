x = int(input("Quantidade de moedas: "))
y = int(input("Preço da skin, em quantidade de moedas: "))
s = x - y
print(f"Yay, pode comprar a skin, ainda sobram {s} moedas!" if s >= 0 else f"Sinto muito, você não consegue comprar a skin. Faltam {s * -1} moedas")