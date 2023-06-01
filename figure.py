#figure.py
#line class -- __length를 받고 __length의 값을 수정 및 반환하는 메소드를 제공
#area_square, arear_circle, area_regular_triangle 함수를 제공. 각각 정사각형, 원, 정삼각형의 넓이를 반환

import math #sqrt 와 pi 를 쓰기위해 import 했다.
#figure 모듈 구성
class line: #length의 값을 저장, 수정, 반환하기 위한 class이다.
    __width = 0 #초기 값은 0이다. __를 사용하여 외부에서 접근이 불가능하게 한다.
    __height = 0
    
    def __init__(self,width,height): #초기 값을 받는다
        self.__width = width
        self.__height = height
        
    def get_length(self): #__length값을 반환해준다.(메소드)
        return self.__width,self.__height
    
    def set_length(self,width,height): #__length값 수정을 가능하게 한다.(메소드)
        self.__width = width
        self.__height = height

def area_rectangle(width,height): #정사각형의 넓이를 반환하는 함수이다.
    if width<=0 or height<=0: raise ValueError
    return width*height
    
def area_ellipse(width,height): #원의 넓이를 반환하는 함수이다.
    if width<=0 or height<=0: raise ValueError
    return width*height*(math.pi)
    
def area_right_triangle(width,height): #정삼각형의 넓이를 반환하는 함수이다.
    if width<=0 or height<=0: raise ValueError
    return width*height/2
    
    