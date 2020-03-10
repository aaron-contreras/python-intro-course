for i in range(1, (int(input("ingrese un numero entero: "))+1), 2):
    print(str(i), end = ',') if i % 2 != 0 else print(str(i))
