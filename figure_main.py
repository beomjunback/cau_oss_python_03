# %%

import figure #figure모듈을 불러온다.

myline = figure.line(10) #__length의 값을 10으로 설정한다. #figure 모듈에 있는 'line' class를 불러온다.

square = figure.area_square(myline.get_length()) #get_length로 __length값을 받고 이를 area_square 함수의 매개변수로 넣는다.
print(square)

myline.set_length(20) #set_length로 __length의 값을 20으로 수정한다.
regular_triangle = figure.area_regular_triangle(myline.get_length()) #get_length로 __length값을 받고 이를 area_regular_triangle 함수의 매개변수로 넣는다.
print(regular_triangle)

myline.set_length(30) #set_length로 __length의 값을 30으로 수정한다.
circle = figure.area_circle(myline.get_length()) #get_length로 __length값을 받고 이를 area_circle 함수의 매개변수로 넣는다.
print(circle)