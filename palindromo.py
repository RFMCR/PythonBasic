def verificarpalindromo(palabra):
    palabra = palabra.replace(' ','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1] #Invierte la palabra
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra=input("Escribe una palabra o frase: ")
    es_palindromo=verificarpalindromo(palabra)
    if es_palindromo == True:
        print("Es Palindromo")
    else:
        print("No es Palindromo")

if __name__ =='__main__':
    run()

    #yo hago yoga hoy
    #ana
    