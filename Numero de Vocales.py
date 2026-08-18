while True:
    
    vocales = "aeiouAEIOU"
    palabra = input("Ingresa una palabra:   ")
    
    
    contador = 0
    
    for letra in palabra:
        if letra in vocales:
            contador +=1
    print("Numero de vocales: ", contador)
        
