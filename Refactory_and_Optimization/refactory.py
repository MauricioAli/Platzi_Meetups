
currencies ={
        1:{'value':3641,'name':"pesos"},
        2:{'value':1,'name':'dolares'},
        3:{'value':0.7198,'name':'libras'},
        4:{'value':0.8472,'name':'Euros'}
}


def converter(input_coin: int,output_coin: int,amount: float,name: str)-> str:

    conversion = (currencies[output_coin]['value']*amount)/currencies[input_coin]['value']
    request = "{} {} {} es equivalente a {} {}".format(name,amount,currencies[input_coin]['name'],conversion,currencies[output_coin]['name'])
    return request

def main():
    print('bienvenido a MYTRM el programa que ayudará a saber el cambio de divisa internacional ')
    nombre = input('cual es tu nombre?: ')
    moneda1 = int(input('porfavor selecciona el tipo de divisa que quieres conertir \n 1.peso \n 2.dollar \n 3.libra esterlina \n 4.euro \n: ')) 
    cantidad = int(input('que cantidad de la moneda que seleccionaste quieres convertir: '))
    moneda2 = int(input('Aque moneda quieres covertir \n 1.peso \n 2.dollar \n 3.libra esterlina \n 4.euro \n:'))
    print(converter(moneda1,moneda2,cantidad,nombre))



if __name__ == "__main__":
    
    main()
    
   