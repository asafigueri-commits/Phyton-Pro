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





import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Ingrese la longitud de la contraseña.          "))

contrasena_generada =  ""

for i in range(longitud):
    contrasena_generada += random.choice(caracteres)
    print("")

print("Tu contrasena generada es:", contrasena_generada)
