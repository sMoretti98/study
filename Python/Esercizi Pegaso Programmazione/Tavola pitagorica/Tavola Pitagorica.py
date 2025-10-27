print("Tavola Pitagorica")
print("")

Tartosso = True
while Tartosso:
    N = int(input("Inserire N\n"))
    if N > 20:
        print("Troppi numeri")
    elif N == 0:
        print("Chiusura tavola pitagorica")
        Tartosso = False
    else:
        for i in range(1,N+1):
            print(f"Tabellina del {i}")
            for j in range(1,N+1):
                print(f"{i} * {j} = {i*j}")
            print("")