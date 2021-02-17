def numerocomp():
    num_1= int(input('escoge un entero:'))
    num_2 = int(input('escoge otro entero:'))

    if num_1 > num_2:
        print('El numero 1 es mayor al numero 2')
    elif num_1 < num_2:
        print('El numero 2 es mayor que el numero 1')
    else:
        print('son iguales')


if __name__ == '__main__':
    numerocomp()