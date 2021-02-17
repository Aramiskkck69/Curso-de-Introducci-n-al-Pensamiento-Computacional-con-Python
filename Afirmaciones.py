def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        if type(palabra) == bool:
            print(f"El valor booleano {palabra} no es un String")
        else:
            try:
                assert type(palabra) == str, f"{palabra} no es String"
                assert len(palabra) > 0, "No se permiten str vacios"

                primeras_letras.append(palabra[0])
            except AssertionError as e:
                print(e)

    return primeras_letras

mi_lista = ["hola",5.1,"",4,True,"Aylen","$10", "=(1)"]

print("Los caracteres validos son",primera_letra(mi_lista))