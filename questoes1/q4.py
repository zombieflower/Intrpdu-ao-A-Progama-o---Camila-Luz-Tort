text = input("Digite sua mensagem: ")
b = len(text)
if b < 3 or b > 140:
    print("Mensagem bloqueada por violar as diretrizes de spam!")
else:
    print("Mensagem enviada com sucesso!")