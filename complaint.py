i = input("Say hi: ")

if i == 'hi':
    offices = {1: 'almaty',
           2: 'paris',
           3: 'pretoria',
           4: 'bishkek',
           5: 'san francisco',
           6: 'berlin',
           7: 'moscow',
           8: 'stockholm'}
    print(offices)

choice = int(input("Pick and office: "))
complaint = input("Write your complaint to the office you picked above: ")

if choice == 1:
    with open("almaty.txt", "a") as file:
        file.write(complaint)
elif choice == 2:
    with open("paris.txt", "a") as file:
        file.write(complaint)

elif choice == 3:
    with open("pretoria.txt", "a") as file:
        file.write(complaint)

elif choice == 4:
    with open("bishkek.txt", "a") as file:
        file.write(complaint)

elif choice == 5:
    with open("san francisco.txt", "a") as file:
        file.write(complaint)

elif choice == 6:
    with open("berlin.txt", "a") as file:
        file.write(complaint)

elif choice == 7:
    with open("moscow.txt", "a") as file:
        file.write(complaint)

elif choice == 8:
    with open("stockholm.txt", "a") as file:
        file.write(complaint)