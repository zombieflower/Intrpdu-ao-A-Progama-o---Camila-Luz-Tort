ee = input("Jogador 1, você escolhe 'par' ou 'impar'? ")
eee = int(input("Jogador 2, digite um número inteiro: "))
e = int(input("Jogador 1, digite um número inteiro: "))
myy = e + eee
if myy % 2 == 0 and ee == "par":
    print("Jogador 1 venceu!")
elif ee == "impar" and myy % 2 != 0:
    print("Jogador 1 venceu!")
else:
    print("Jogador 2 venceu!")