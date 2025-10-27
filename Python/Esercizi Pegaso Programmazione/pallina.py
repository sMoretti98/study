print("RIMBALZI PALLINA\n")
h = 0.0
i = 0
while h <= 1:
    h = float(input("Inserire altezza da cui viene lasciata la pallina in cm (h>1):\n"))
while h > 1:
    h*=0.8
    i=i+1
    print(f"Rimbalzo n°{i} e altezza in cm:{h}")
print(f"Il numero di rimbalzi è pari a {i}")
print(f"L'altezza finale è pari a {h}cm")