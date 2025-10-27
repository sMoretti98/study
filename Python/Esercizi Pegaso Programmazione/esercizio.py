number = 0

def main():
    global number
    number = int(input("Inserisci un numero\n"))
    show_number()

def show_number():
    print(f"Il numero che hai inserito è {number}.")

main()