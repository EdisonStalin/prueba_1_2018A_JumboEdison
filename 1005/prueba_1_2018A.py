
print("Edison Jumbo")

# binario = input('ingrese el binario')
# cadena = len(binario)
#
# for i in range(cadena):
#     binario[i]
#     print(binario[i])
#
#
#
# for i in range(cadena):
#
#     binario[i]= binario.replace(binario[i],binario[cadena])
#     print(binario[i])

#num = input('ingre el numero en binario')





# def cambio(cadena,binario):
#     for i in range(cadena):
#         binario[i]=binario[cadena]
#         cadena = cadena-1
#         print(binario[i])
#         return

# def cambio(binario,cadena):
binario = [1, 0, 0]






def creartxt():
    archivo1 = open('texto1.txt','w')


    archivo2 = open('texto2.txt', 'w')
    archivo3 = open('texto3.txt', 'w')
    archivo1.close()

    archivo2.close()
    archivo3.close()

def grabartxt():
    archivo1 = open('texto1.txt','a')
    binario = [1, 0, 0]
    cadena = len(binario)
    for i in range(cadena):
        binario[i] = ((binario[i]) * (2 ** cadena))
        cadena = cadena - 1
        print(binario[i])
    archivo1.write('el binario ingresado es: =%s' % binario)



    archivo2 = open('texto2.txt', 'a')

    binario = [1, 0, 0]
    cadena = len(binario)

    for i in range(cadena):
        binario[i] = ((binario[i]) * (2 ** cadena))
        cadena = cadena - 1
        binario




    archivo2.write('la nueva cadena es=%s' % binario)

    archivo3 = open('texto3.txt', 'a')

    lista ={'T':0,'R':1,'W':2,'A':3,'G':4,'M':5,'Y':6,'F':7,'P':8,'D':9,'X':10,'B':11,'N':12,'J':13,'Z':14,'S':15,'Q':16,'V':17,'H':18,'L':19,'C':20,'K':21}

    archivo3.write('mensaje a codigicar :' )
    archivo3.write('mensaje codificado :' )

    archivo1.close()
    archivo2.close()
    archivo3.close()


creartxt()
grabartxt()






