

import figure

myline = figure.line(10,20)
width,height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width,height)
    print(rectangle)
except ValueError:
    print("input positive number for width and height")

myline.set_length(20,30)
width,height = myline.get_length()
try:
    right_triangle = figure.area_right_triangle(width,height)
    print(right_triangle)
except ValueError:
    print("input positive number for width and height")
 
myline.set_length(30,40)
width,height = myline.get_length()
try:
    ellipse = figure.area_ellipse(width,height)
    print(ellipse)
except ValueError:
    print("input positive number for width and height")