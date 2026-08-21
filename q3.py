h = int(input("Quantas horas, em média, você passa assistindo a tela por dia? "))
if h < 1:
    print("Espectador Casual")
elif 1 <= h <= 3:
    print("Maratonista Iniciante")
elif 3 < h <= 5:
    print("Maratonista Profissional")
else:
    print("Alerta Vermelho! Desligue a tela e vá ver o sol!")