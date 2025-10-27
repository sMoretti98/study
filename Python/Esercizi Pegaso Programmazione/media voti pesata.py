print("MEDIA PESATA")
sommav = 0
sommac = 0
voto = int(input("Inserire voto:\n")) 
if voto >= 0:
    while voto >= 0 and voto <= 30:
        crediti = -1
        while crediti <= 0:
            crediti = float(input("Inserire CFU:\n"))
        sommav += voto*crediti
        sommac += crediti
        voto = int(input("Inserire voto:\n"))
    print(f"La media dei voti è pari a {sommav/sommac}")
else:
    print("Voto non valido")