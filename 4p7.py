min_value = None
max_value = None

while True:
    tal = int(input("Skriv in ett tal (negativt tal avslutar): "))

    if tal < 0:
        break

    if min_value is None or tal < min_value:
        min_value = tal

    if max_value is None or tal > max_value:
        max_value = tal

if min_value is None:
    print("Inga positiva tal matades in.")
else:
    print("Största positiva tal:", max_value)
    print("Minsta positiva tal:", min_value)