# Stampa il titolo della tavola pitagorica
print("TAVOLA PITAGORICA")
print("")

Tartosso = True
# Chiede all'utente di inserire il valore di N


while Tartosso:
    N = int(input("Inserire N\n"))
    if N > 10:
        print("Numero troppo grande, inserisci fino a 10")
        print("")
    elif N == 0:
        print("Chiusura")
        Tartosso = False
    else:
        # Stampa l'intestazione della prima riga (con l'asterisco e i numeri da 1 a N)
        print("*", end="\t")
        for i in range(1, N+1):
            print(i, end="\t")
        print("")

        # Stampa una riga di separazione usando il carattere '-'
        for i in range(1, N*9):
            print("-", end="")
        print("")

        for i in range(1,N+1):
            print(i,end="\t|")
            for j in range(1,N+1):
                print(i*j,end="\t")
            print("")