

import figure #figure모듈을 불러온다.

myline = figure.line(10,20) #__length의 값을 10으로 설정한다. #figure 모듈에 있는 'line' class를 불러온다.
width,height = myline.get_length()
try:
    rectangle = figure.area_rectangle(width,height) #get_length로 __length값을 받고 이를 area_square 함수의 매개변수로 넣는다.
    print(rectangle)
except ValueError:
    print("input positive number for width and height")

myline.set_length(20,30) #set_length로 __length의 값을 20으로 수정한다.
width,height = myline.get_length()
try:
    right_triangle = figure.area_right_triangle(width,height) #get_length로 __length값을 받고 이를 area_regular_triangle 함수의 매개변수로 넣는다.
    print(right_triangle)
except ValueError:
    print("input positive number for width and height")
 
myline.set_length(30,40) #set_length로 __length의 값을 30으로 수정한다.
width,height = myline.get_length()
try:
    ellipse = figure.area_ellipse(width,height) #get_length로 __length값을 받고 이를 area_circle 함수의 매개변수로 넣는다.
    print(ellipse)
except ValueError:
    print("input positive number for width and height")