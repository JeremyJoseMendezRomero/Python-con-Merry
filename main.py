# Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
# 
# Hora actual: 3
# Cantidad de horas: 5
# En 5 horas, el reloj marcara las 8
# 
# Hora actual: 11
# Cantidad de horas: 43
# En 43 horas, el reloj marcara las 6

print('A program to calculate what hour will be in n time\n')

hours = list(range(0, 24, 1))

while True:
    try :
        actualTime = int(input('Enter the actual hour (without minutes) in 24 hours format: '))
        skipHours = int(input('Enter the amount of time you want to skip: '))
        if actualTime in hours:
            indexTime = hours.index(actualTime)

            # función .index() para filtrar y ubicar el elemento especificado dentro del array,
            # se le agrega el parametro actualTime para especificar este valor y esto nos da el indice desde el cual se comenzará el recorrido.

            arrayLength = len(hours)

            # función len() para determinar la cantidad de elementos del parametro hours, 24 elementos en este caso

            indexResult = (indexTime + skipHours) % arrayLength

            # indexResult = (indexTime + skipHours) % arrayLength: este paso es clave. Aquí estamos utilizando aritmética modular para calcular cuál sería el índice final después de recorrer "skipHours" veces, de manera cíclica.
            # indexTime + skipHours: calcula el número de pasos a partir del índice de inicio.
            # % arrayLength: con la operación modular (%), nos aseguramos de que el índice sea "envuelto" (ruleta) dentro de los límites del array. Esto simula el comportamiento de moverse en un ciclo.

            # Por ejemplo, si indexTime es 2 y n es 6:
            # 2 + 6 = 8
            # 8 % 24 = 0 (ya que el array tiene longitud 24), por lo que el índice resultante es 8.

            skipedHours = hours[indexResult]
        
            print(f'in {skipHours} hours, will be: {skipedHours} hours')
        else:
            print("escribe en formato 24 h.")

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

# Exercise 07