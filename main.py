# Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:
# 
# Primera nota: 55
# Segunda nota: 71
# Tercera nota: 46
# Cuarta nota: 87
# El promedio es: 64.75

print('You need to enter four of your students notes to get the average')


while True:
      try:
           noteOne = float(input('Enter the first note: '))
           noteTwo = float(input('Enter the second note: '))
           noteThree = float(input('Enter the thirdth note: '))
           noteFour = float(input('Enter the fourth note: '))
           average = (noteOne + noteTwo + noteThree + noteFour) / 4
           print(f' \n The average is: {average}')

           continueAsk = input( "\n    Do you want to get another average? (Y/N): " ).strip().lower()
           if continueAsk != "y" :
                print("    Thaks for using the program. Goodbye! \n ")
                break
      except :            
            print("\n        Error: Please enter the correct data ")
            continueAsk = input( "\n    Do you want to calculate again? (Y/N): " ).strip().lower()

            if continueAsk != "y" :
                print("    Thaks for using the program. Goodbye! \n ")
                break