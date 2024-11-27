# Programma Collatz

# funzione con un singolo parametro: numero
# se il numero è pari, la funzione deve stampare il numero // 2 e restituire il valore
# se il numero è dispari, la funzione deve stampare e restitutire 3 * numero + 1

# programma: un utente può inserire un numero intero.
# Il numero intero è utilizzato come argomento di collatz(), e ogni valore dopo verrà usato come argomento di collatz finché non arriva un valore return di 1
# (quanto collatz fornisce un return di 1)
# bisogna stampare ogni volta il valore di collatz

def collatz(num):
    if num % 2 == 0:
        return (num // 2)
    else:
        return (num * 3 + 1)
    
# collatz_number = int(input("Inserisci un numero intero "))
# counter = 0
# while collatz_number > 1:
#     counter = counter + 1
#     collatz_number = collatz(collatz_number)
#     print(f"Numero: {collatz_number} - numero di calcolo: {counter}")