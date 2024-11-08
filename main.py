# Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2
# 
# .
# 
# Ingrese cateto a: 7
# Ingrese cateto b: 5
# La hipotenusa es 8.6023252670426267

import math

print('A program to calculate hypotenuse\n')

while True:
    try :
        cathetusA = float(input('Enter the cathetus A: '))
        cathetusB = float(input('Enter the cathetus B: '))
        hypotenuse = math.sqrt(cathetusA ** 2 + cathetusB ** 2)

        print(f'Here is the hypotenuse: {hypotenuse}')
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

# Exercise 06