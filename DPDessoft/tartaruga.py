import turtle
#Receber string e desenhar
window = turtle.Screen()
trt = turtle.Turtle()
trt.speed(100)
trt.penup()
trt.setpos(10,10)
trt.pendown()

string = input("brinco")
jooj = input("Lei")
a = 60
n = input("Iterações")
n = int(n)
F = trt.forward(50)
for i in range(n):
    for b in jooj:
        jooj.replace("F",string)
        if b == "+F":
            trt.forward(50)
            trt.left(a)
        if b == "F":
            trt.forward(50)
            trt.left(a)
        if b == "-F":
            trt.forward(-50)
            trt.left(-a)
#Se +, forward. Se -, -forward.
        #########   PEGA UMA STRING. PEGA OUTRA STRING MAIOR. SUBSTITUI CADA
        #########ELEMENTO DA PRIMEIRA STRING PELA PRIMEIRA STRING.
