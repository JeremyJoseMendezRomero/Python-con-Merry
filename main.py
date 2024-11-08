#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.
# 
# Ingrese longitud: 45
# 45 cm = 17.7165 in
# 
# Ingrese longitud: 13
# 13 cm = 5.1181 in

print('A program to make the convertion from centimeters to inches \n')
formula = 2.54

while True:
    try:
        cm = float(input('Please, enter the cm to be calculated: '))
        convertedNum = cm / formula
        print(f'{cm} Cm is to: {round(convertedNum,4)}')
        continueAsk = input( "\n    Do you want to do another calculation? (Y/N): " ).strip().lower()
        if continueAsk != "y" :
            print("    Thaks for using the program. Goodbye! \n ")
            break
    except :            
        print("\n        Error: Please enter the correct data ")
        continueAsk = input( "\n    Do you want to calculate again? (Y/N): " ).strip().lower()

        if continueAsk != "y" :
            print("    Thaks for using the program. Goodbye! \n ")
    break

# Exercise 04