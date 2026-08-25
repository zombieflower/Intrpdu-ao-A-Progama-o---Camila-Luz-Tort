age = int(input("Sua idade, em anos: "))
la = input("Tem carteira de estudante ativa? (sim/não) ")
if age == 60 or age > 60: 
    print("Gratuidade concedida por lei!")
elif age < 18 or la == "sim":
    print("Meia-entrada autorizada!")
else:
    print("Passagem inteira.")