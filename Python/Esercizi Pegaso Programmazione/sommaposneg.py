print("SOMMA NUMERI POSITIVI E NEGATIVI")
pos = 0
neg = 0
n = int(input("Inserisci numero:\n"))
while n != 0:
    if n > 0:
        pos += n
    elif n < 0:
        neg -= n
    n = int(input("Inserire numero:\n"))
if pos > neg:
    print(f"La somma dei valori assoluti dei numeri positivi {pos} è maggiore della somma dei valori assoluti dei numeri negativi {neg}")
elif pos < neg:
    print(f"La somma dei valori assoluti dei numeri negativi {neg} è maggiore della somma dei valori assoluti dei numeri positivi {pos}")
else:
    print(f"La somma dei valori assoluti dei numeri negativi {neg} è uguale alla somma dei valori assoluti dei numeri positiv {pos}")
