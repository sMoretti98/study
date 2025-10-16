print("SEQUENZA CRESCENTE")

cresc = 0
l = 0
N = 0

while N <= 1:
    N = int(input("Inserire lunghezza della sequenza\n"))
num_prec = int(input("Inserire numero n°1:\n"))

for i in range(1,N):
    num_suc = int(input(f"Inerire numero n°{i + 1}:\n"))
    if num_suc >= num_prec:
        if cresc == 1:
            l += 1
        else:
            cresc = 1
            l = 2
    num_prec = num_suc

print(f"La sequenza crescente è pari a {l} numeri corrispondenti al {l*100/N}% della sequenza")
