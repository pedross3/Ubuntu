import turtle
#Receber string e desenhar
window = turtle.Screen()
trt = turtle.Turtle()
trt.speed(10)
trt.penup()
trt.setpos(50,50)
trt.pendown()
F = 50
a = 30
for t in range (16):
    trt.forward(F)
    trt.forward(-F)
    trt.right(a)
