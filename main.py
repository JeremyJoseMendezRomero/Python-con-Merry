# Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.
# 
# Ingrese un numero: 4.5
# 0.5
# 
# Ingrese un numero: -1.19
# 0.19

while True:
    try :
        unfilteredNumber = float(input('Enter a number with it decimals: '))
        
        # Esta es la manera minificada de la resolución del ejercicio 8
        print(round(abs(unfilteredNumber) % 1, len(str(unfilteredNumber)[(len(str(int(abs(unfilteredNumber) // 1))) + 1):])))

        # Ejemplo del caso 14.578
        # unfilteredNumber // 1 me permíte obtener el entero que sería: 14
        # Ya que estoy midiendo la cantidad de caracteres con la función len(), agrego un + 1 para contar el punto decimal
        # Al tener 3 como resultado, procedo a la variable rounderTwo
        #
        #rounder = len(str(int(abs(unfilteredNumber) // 1))) + 1
        #
        # En rounderTwo, convierto unfilteredNumber a STRING para poder usar la función SLICE[]
        # Función a la cual se le asigna el parametro [3:] ya que 3 es el valor obtenido en la variable rounder
        #
        #rounderTwo = len(str(unfilteredNumber)[rounder:]
        #
        # Luego de cortar los caracteres de inicio a fin con SLICE[rounder:] procede a entrar en el siguiente print()
        # El cual lo convierte nuevamente a un valor numérico y en el parametro de la función round()
        # Se le agrega el valor de rounderTwo, que contiene la cantidad exacta de decimales ingresados en el input
        #
        #print(round(abs(unfilteredNumber) % 1, rounderTwo)))
        #
        # Forma de resolverlo con la lógica de David
        #
        # dataOne = len(str(int(abs(unfilteredNumber)))) + 1
        # dataTwo = len(str(unfilteredNumber)[dataOne:])
        # print(round(abs(unfilteredNumber - int(unfilteredNumber)), dataTwo))


        continueAsk = input( "\nDo you want to do another calculation? (Y/N): " ).strip().lower()
        if continueAsk != "y" :
            print("    Thaks for using the program. Goodbye! \n ")
            break
    except :            
        print("\n        Error: Please enter the correct data ")
        continueAsk = input( "\n    Do you want to calculate again? (Y/N): " ).strip().lower()

        if continueAsk != "y" :
            print("    Thaks for using the program. Goodbye! \n ")
            break

# Exercise 08