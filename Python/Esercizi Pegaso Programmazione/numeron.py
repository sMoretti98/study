print("DA NUMERO A CENTO CON PASSO N")
num = 100
incr = -1
while incr < 0 or incr > 100:
    incr = int(input("Inserire valore incremento:\n"))
while num > 100 - incr:
    num = int(input(f"Inserire numero < {100 - incr}:\n"))
i = 0
while num < 100:
    num+=incr
    i+=1
print(f"Per arrivare/superare 100, sono necessarie {i} somme con {incr}")