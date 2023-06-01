#figure.py
#line class -- __width와 __heigth를 받는 메소드와 수정 및 반환하는 메소드를 제공
#area_rectangle, arear_ellipse, area_right_triangle 함수를 제공. 각각 직사각형, 타원, 직각삼각형의 넓이를 반환

import math #pi 를 쓰기위해 import 했다.
#figure 모듈 구성
class line: #__width 와 __height의 값을 저장, 수정, 반환하기 위한 class이다.
    __width = 0 #초기 값은 0이다. __를 사용하여 외부에서 접근이 불가능하게 한다.
    __height = 0
    
    def __init__(self,width,height): #초기 값을 받는다
        self.__width = width
        self.__height = height
        
    def get_length(self): #__width와 __height값을 반환해준다.(메소드)
        return self.__width,self.__height
    
    def set_length(self,width,height): #__width와 __height 값을 수정한다.(메소드)
        self.__width = width
        self.__height = height

#아래 3개의 함수는 0 이하의 수를 넣으면 ValueError가 뜨도록 예외처리가 되어 있다.
def area_rectangle(width,height): #직사각형의 넓이를 반환하는 함수이다.
    if width<=0 or height<=0: raise ValueError
    return width*height
    
def area_ellipse(width,height): #타원의 넓이를 반환하는 함수이다.
    if width<=0 or height<=0: raise ValueError
    return width*height*(math.pi)
    
def area_right_triangle(width,height): #직각삼각형의 넓이를 반환하는 함수이다.
    if width<=0 or height<=0: raise ValueError
    return width*height/2
    
    