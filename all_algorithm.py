def enumeracion():

    objc = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objc:  #mientras objc es menos a la raiz de respuesta
        # print(respuesta)
        respuesta += 1          #suma 1 a respuesta hasta que se cumpla una condicion
    if respuesta**2 == objc:
        print(f'la raiz cuadrada de {objc} es {respuesta}')
        print('******************************************************')
    else:
        print(f'{objc} no tiene una raiz cuadrada exacta')
        print('******************************************************')

# ************************************************************
def aproximacion():

    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0
    cont = 0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        cont += 1
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada del {objetivo}')
        print('******************************************************')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
        print('******************************************************')
# ************************************************************
def aprox_binary():

    objetivo = int(input('Escoge un numero: '))
    epsilon = 0.0001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo = {bajo}, alto = {alto}, respuesta = {respuesta}')

        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    print('******************************************************')
# ************************************************************

def void():
    a = 0

    while a == 0:
        selction = int(input(""" Selecciona el algortimo que deseas utilizar 
        1 = Enumeración exhaustiva 
        2 = aproximacion 
        3 = aproximacion binaria:  
        """))

        if selction == 1:
           enumeracion()
        elif selction == 2:
            aproximacion()
        elif selction == 3:
            aprox_binary()
        elif selction == 0:
            break
        else:
            print('Algoritmo no valido')


if __name__ == '__main__':
    void()