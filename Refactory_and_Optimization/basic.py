   
print('bienvenido a MYTRM el programa que ayudará a saber el cambio de divisa internacional ')

nombre = input('cual es tu nombre?: ')
m1 = int(input('porfavor selecciona el tipo de divisa que quieres conertir \n 1.peso \n 2.dollar \n 3.libra esterlina \n 4.euro \n: '))
c = int(input('que cantidad de la moneda que seleccionaste quieres convertir: '))
m2 = int(input('Aque moneda quieres covertir \n 1.peso \n 2.dollar \n 3.libra esterlina \n 4.euro \n:'))

def main():   
   
    peso = 1.0
    dollar = 1.0
    libra_uk = 1.0
    euro = 1.0
    respuesta = 0
    
    if m1 == 1 and m2 == 1:
        peso = 1

        respuesta = (c * peso / peso )
        print('ok'+ nombre + str(c)+  'pesos equivalen a '+str(respuesta)+ 'pesos')


    elif m1 == 2 and m2 == 1:
        peso = 3728.50
        
        respuesta = (c * peso / dollar )
        print('ok'+ nombre + str(c)+  'dollares equivalen  ' +str(respuesta)+ 'pesos')

    elif m1 == 3 and m2 == 1:
        peso = 5118.43

        respuesta = (c * peso / libra_uk)
        print('ok'+ nombre + str(c)+  'libras esterlinas euivalente a ' +str(respuesta)+ 'pesos')

    elif m1 == 4 and m2 == 1:
        peso = 4365.41

        respuesta = (c * peso / euro)
        print('ok'+ nombre + str(c)+  'euros equivalente a '+str(respuesta)+ 'pesos')

    if m1 == 1 and m2 == 2:
        dollar = 1
        peso = 3728.50

        print(c * dollar / peso )

    if m1 == 2 and m2 == 2:
        dollar = 1

        print(c * dollar / dollar )

    else: print('no dispoble')



if __name__ == "__main__":
    main()