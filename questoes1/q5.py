es = int(input("Nota 1: "))
lo = int(input("Nota 2: "))
te = lo + es
gcg = te / 2 
if gcg >= 60:
    print("Parabéns, você foi APROVADO!")
elif gcg < 60 and gcg >= 20:
    print("Você ficou em RECUPERAÇÃO! Estude para a prova final.")
elif gcg < 20:
    print("REPROVADO direto.")