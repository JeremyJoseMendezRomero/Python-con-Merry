# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
# 
# Ingrese numero: 345
# 543
# 
# Ingrese numero: 241
# 142



print('A program to get the inverted number that you enter \n')


while True:
    try :
        number = int(input('Enter the number you want the invert: '))
        invertedNumber = str(number)[::-1]
        print(f'Here is the result: {invertedNumber}')
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

# Exercise 05