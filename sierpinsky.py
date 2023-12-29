import turtle
import math

def draw_triangle(x1, y1, x2, y2, x3, y3, t):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    p1 = (0.5 * (x1 + x2), 0.5 * (y1 + y2))
    p2 = (0.5 * (x2 + x3), 0.5 * (y2 + y3))
    p3 = (0.5 * (x1 + x3), 0.5 * (y1 + y3))
    
    if d > 4: #experiment w this line
        draw_triangle(x1, y1, p1[0], p1[1], p3[0], p3[1], t)
        draw_triangle(p1[0], p1[1], x2, y2, p2[0], p2[1], t)
        draw_triangle(p3[0], p3[1], p2[0], p2[1], x3, y3, t)
    else:
        t.up()
        t.setpos(x1, y1)
        t.down()
        t.setpos(x2, y2)
        t.setpos(x3, y3)
        t.setpos(x1, y1)

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    draw_triangle(-150, 0, 150, 0, 0, 259.8076211353316, t)

    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()