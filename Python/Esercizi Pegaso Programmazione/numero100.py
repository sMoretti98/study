print("DA NUMERO A 100")
n = 100
while n > 98:
    n = int(input("Inserire numero:\n"))
i = 0
while n < 100:
    n+=2
    i+=1
print(f"Per arrivare/superare 100, sono necessarie {i} somme con 2")