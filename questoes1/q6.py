e = float(input("Velocidade em km/h: ")) 
if e <= 60: 
    print("Velocidade permitida. Boa viagem!")
elif e > 60 and e < 70:
    print("Infração Média! Multa de R$ 130,16.")
else:  
    print("Infração Gravíssima! Multa de R$ 293,47 e perda de pontos na CNH.")    