# Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
# Ingrese el radio: 5
# Perimetro: 31.4
# Área: 78.5

# Pi value
import math

print('This is a function to calulate the area and perimeter of the entered radius in the next input')

radius = float(input('Enter the radius to be calculated: '))

area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius

print(f'''
      The area of {radius} is: {round(area,2)} cm²
      & the perimeter is: {round(perimeter,1)} cm
      ''')