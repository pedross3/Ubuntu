from turtlegraphics import Turtle

def ccurve (turtle, x1, y1, x2, y2, level):
    def drawline(x1, y1, x2, y2):
        turtle.up()
        turtle.move(x1, y1)
        turtle.down()
        turtle.move(x2, y2)
    if level == 0:
        drawline(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) / 2
        ym = (x2 + y1 + y2 - x1) / 2
        ccurve(turtle, x1, y1, xm, ym, level -1)
        ccurve(turtle, xm, ym, x2, y2, level -1)
def main():
    turtle = Turtle(300, 350)
    turtle.setWidth(1)
    ccurve(turtle, 75, -75, 75, 75 ,14)
main()
