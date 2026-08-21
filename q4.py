
• A Condição: Leia a mensagem digitada pelo usuário. Usando a função len(), verifique o
comprimento do texto:
text = 
if text < 3 or text > 140:
    print("Mensagem bloqueada por violar as diretrizes de spam!")
else:
    print("Mensagem enviada com sucesso!")