from turtle  import *
import time
import math

def 삼각형():
    shape("turtle")
    for i in range(3):
        forward(100)
        left(120)
# 삼각형()

def  사각형():
    shape("turtle")
    for i in range(4):
        forward(100)
        left(90)
# 사각형()    

def  shape를사용한사각형():
    t1= Turtle(shape="square")
    t1.color("white","red")
    t1.goto(200,100)
    t1.shapesize(1.5,0.5)
    t1.goto(-200,100)
    t1.shapesize(1.5,0.5)

    t2= Turtle(shape="square")
    t2.color("white","blue")
    t2.goto(200,100)
    t2.left(90)
    t2.shapesize(1.5,0.5)
    # t2.goto(-200,100)
    # t1.shapesize(1.5,0.5)

    

shape를사용한사각형()    
    

def 다각형():
    angle=(120, 90, 72, 60, 45, 30)
    colors = ["red", "purple", "blue", "green", "yellow", "orange"]
    speed(0)
    shape("turtle")
    for m in range(len(angle)):
        home()
        setheading(0)
        clear()
        pencolor(colors[m])
        for i in range(0,int(360/angle[m])+1) :
            forward(100)
            left(angle[m])
        left(180- angle[m])            
        time.sleep(2)
# 다각형()
def circle로다각형(): 
    t=Turtle()
    xpos=-350
    for  i in range(3,9, 1):
        t.penup()
        t.goto(xpos+i*50, -50)
        t.pendown()
        t.circle(100, steps=i)

# circle로다각형()    

def 다각형그리기_윈도우사용():
    t=Turtle()
    speed(0)

    # penup()
    # goto(0,200)         
    # pendown()
    s=textinput('', '숫자 입력')
    n=int(s)
    t.circle(100, steps=n)
    # for i in range(n):
    #     forward(100)
    #     left(360/n)

# 다각형그리기_윈도우사용()


def  집그리기():

    size = 100#int(input("집의 크기는 얼마로 할까요? "))

    for i in range(0,4):
        forward(size)
        right(90)
    for i in range(0,3):
        forward(size)
        left(120)
# 집그리기()

def 커지며이동하는원():
    # radius = 50
    # circle(radius)
    # up()
    # goto(100, 0)
    # down()
    # radius = radius + 20
    # circle(radius)
    # up()
    # goto(200, 0)
    # down()
    # radius = radius + 20
    # circle(radius)
    speed(30)
    radius=30
    for i in range(-30,10):
        up()
        goto(i*10,i*10)
        down()
        radius +=20
        circle(radius)

# 커지며이동하는원()
def 네개의사각형():
    speed(10)
    size = 200
    angle = 90

    for m in range(0,4):
        for i in range(0,4):
            forward(size)
            left(90)
        left(90)

# 네개의사각형()

def 회전하는사각형():
    Screen().setup(0.4, 0.6)  # 가로, 세로


    speed(10)
    for j in range(0,90, 5):
        right(j)
        for i in range(4):
            forward(200)
            left(90)

# 회전하는사각형()    

def 두점을삼각형으로():
    
    speed(10)
    x1, y1 = 0,0  
    x2, y2 = 90,180
    dist = ((x1+ -x2)**2 + (y1+ -y2)**2)**0.5

    # print("두점 사이의 거리: ", dist )
    angle=180-int(math.atan(abs(x2-x1)/abs(y2-y1))*180/3.14159)
    # print(angle)
    up()
    goto(x1, y1)
    down()
    forward(abs(x2-x1))
    left(90)
    forward(abs(y2-y1))
    left(angle)
    forward(dist)
# 두점을삼각형으로()

def  컬러풀이동원():
    color_list = [ "yellow", "red", "blue", "green" ]
    up()
    goto(-100,0)
    down()

    for m in range(0,4):
        up()
        forward(50)
        down()
        fillcolor(color_list[m])
        begin_fill()
        circle(100)
        end_fill()

# 컬러풀이동원()  


done()

