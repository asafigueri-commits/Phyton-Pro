Prin("Hola Mundo")
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuesta a una broma",
            "SHEESH" : "ligera desaprobación",
            "CREEPY" : "aterrador, siniestro",
            "AGGRO" : "ponerse agresivo/enojado",
            }

for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    
    if word in meme_dict.keys():
        print(word, "significa:",meme_dict[word])
    else:
        print(word, "no esta en el diccionario... ")





while True:
    cadena = input("Enter a string: ")
    
    if len(cadena) > 10:  # Cambiado a '>' porque el enunciado pide cortar si tiene MÁS de 10 caracteres
        resultado = cadena[:10] + "..."
    else:
        resultado = cadena
    
    print("Resultado:", resultado)





while True:

    nombre = input("¿Cuál es tu nombre?")
    edad = int(input("¿Cuántos años tienes?"))
    
    edad_el_proximo_ano = edad + 1
    
    print("Hola, ", nombre, "¡en un año tendrás ", edad_el_proximo_ano, " años!")







while True:
    
    vocales = "aeiouAEIOU"
    palabra = input("Ingresa una palabra:   ")
    
    
    contador = 0
    
    for letra in palabra:
        if letra in vocales:
            contador +=1
    print("Numero de vocales: ", contador)
        






