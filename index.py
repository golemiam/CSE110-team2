import math
print (math.pi)
circle_size = float(input("how big is the radius in centimeters? "))
circle_area = math.pi*circle_size**2
print(f"The area of your circle is {round(circle_area, 4)} centimeters or {round(circle_area/10000, 4)} meters")
sphere_volume = (4/3)*(math.pi)*(circle_size**3)
print(sphere_volume)
print(f"The volume of your circle is {round(sphere_volume, 4)} centimeters or {round(sphere_volume/10000, 4)} meters")

#aquare = float(input(‘What is the length of the side of the square (CM)? ‘))
square = circle_size
area = float(square) ** 2
sqr_cm = area
sqr_m = area/10000
print('The area of the square is ' + str("%.4f"%sqr_cm) + ' CM2')
print('The area of the square is ' + str("%.4f"%sqr_m) + ' M2')
#Square = float(input('What is the length of the side of the square? '))
Area = float(circle_size) ** 2
sqr_cm = Area
sqr_m = Area /10000
print('The area of the square is ' + str("%.4f"%sqr_cm))
print('The area of the square is ' + str("%.4f"%sqr_m))


cube = circle_size ** 3
print('The volume of the cube is ' + str("%.4f"%cube) + ' CM3')

rect_w= input('What is the width of the rectangle in centimeters? ')
rect_h= input('What is the height of the rectangle in centimeters? ')
width= int(rect_w)
height= int(rect_h)
print()
print (f'The area of your rectangle is {(width) * (height)} centimeters or {(width) * (height)/10000}')
