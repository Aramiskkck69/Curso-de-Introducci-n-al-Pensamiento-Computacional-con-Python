def enumeracion():

    objc = int(input('Escoge un entero: '))
    respuesta = 0

    while respuesta**2 < objc:  #mientras objc es menos a la raiz de respuesta
        # print(respuesta)
        respuesta += 1          #suma 1 a respuesta hasta que se cumpla una condicion
    if respuesta**2 == objc:
        print(f'la raiz cuadrada de {objc} es {respuesta}')
    else:
        print(f'{objc} no tiene una raiz cuadrada exacta')


if __name__ == '__main__':
    enumeracion()