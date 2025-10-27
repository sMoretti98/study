print("Media voti")
somma = 0
i = 0.0
voto = int(input("Inserire voto:\n"))
if voto >= 0:
    while voto >= 0 and voto <= 30:
        somma += voto
        i = i+1
        voto = int(input("Inserire voto:\n"))
    print(f"La somma dei voti è: {somma}")
    print(f"La media dei voti è: {somma / i}")
else:
    print("Voto non valido")