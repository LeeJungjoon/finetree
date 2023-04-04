from turtle import *
import random


def 원그리기():
    speed(50)
    for count in range(60):
        circle(100)
        left(360/60)

# 원그리기()

def 무작위그리기():
    import random

    speed(0)

    for i in range(30):
        color=random.uniform(1, 10) #uniform함수는 실수를 리턴한다
        r=random.uniform(0, 1) #튜플이라  0,1 중에서 무작위 수
        b=random.uniform(0, 1)
        g=random.uniform(0, 1)
        tup = (r, b, g) #튜플형
        pencolor(tup) #튜플형으로 된 색깔으로 변한다
        wid=random.randint(1, 3) #두께의 값을 무작위로 정한다
        width(wid)
        length=random.randint(1, 100)
        forward(length)
        angle=random.randint(-180, 180)
        right(angle)
# 무작위그리기()

def 회전하는6각형():
    speed(10)
    def n_polygon(n, length):
        for i in range(n):
            forward(length)
            left(360//n)
    for i in range(16):
        left(20)
        n_polygon(6, 160)

# 회전하는6각형()

def 클릭으로임의도형():
    def square(length, angle):
        for i in range(angle):    #각도만큼 반복하는 반복문
            forward(length) 
            left(360//angle)

    def draw(x, y):
        length=random.randint(50, 100)    #길이 랜덤으로 지정
        angle=random.randint(3, 10)    #각도 랜덤으로 지정
        up()
        goto(x, y)
        down()

        r=random.uniform(0, 1)     #red색 랜덤으로 변화하는 변수
        b=random.uniform(0, 1)     #blue색 랜덤으로 변화하는 변수
        g=random.uniform(0, 1)     #green색 랜덤으로 변화하는 변수

        tup=(r, b, g)    #red, blue, green의 랜덤한 색을 튜플로 묶음

        pencolor(tup)    #튜플색으로 펜의 색 변경
        fillcolor(tup)    #튜플색으로 도형 채우기
        begin_fill()
        square(length, angle)    #매개변수 length, angle 지정
        end_fill()

    Screen()
    onscreenclick(draw) #클릭할 시 draw 호출
# 클릭으로임의도형()

def 마우스로그리기():
    def draw(x, y):
        r=random.uniform(0, 1)
        b=random.uniform(0, 1)
        g=random.uniform(0, 1)
        tup=(r, b, g)
        pencolor(tup)
        wid=random.randint(1, 20)
        width(wid)
        goto(x, y)

    t=Turtle()
    s=Screen()
    s.onscreenclick(draw)
# 마우스로그리기()



done()    
