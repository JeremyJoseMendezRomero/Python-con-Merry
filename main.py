# Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
# 
# El promedio del ramo se calcula con la siguiente formula.
# NC=(C1+C2+C3) / 3
# NF=NC⋅0.7+NL⋅0.3
# 
# Donde NC
# es el promedio de certámenes, NL el promedio de laboratorio y NF
# 
# la nota final.
# 
# Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio,
#  y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.
# 
# Ingrese nota certamen 1: 45
# Ingrese nota certamen 2: 55
# Ingrese nota laboratorio: 65
# Necesita nota 72 en el certamen 3


while True:
    try :
        cOne = float(input('enter your first contest note: '))
        cTwo = float(input('enter your second contest note: '))
        nL = float(input('enter your laboratory note: '))
        print(f'You need {round((3 * (60 - (nL * 0.3)) / 0.7) - cOne - cTwo, 2)} point on your Third note to pass')

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

# Exercise 09