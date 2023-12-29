import turtle
import math

def draw_snowflake(x1, y1, x2, y2, t):
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    r = d/3.0
    h = r * math.sqrt(3) / 2.0
    p3 = ((x1 + 2 * x2) / 3.0, (y1 + 2 * y2) / 3.0)
    p1 = ((x1 * 2 + x2) / 3.0, (y1 * 2 + y2) / 3.0)
    c = (0.5 * (x1 + x2), 0.5 * (y1 + y2))
    n = ((y1 - y2) / d, (x2 - x1) / d)
    p2 = (c[0] + h * n[0], c[1] + h * n[1])
    
    if d > 200: #experiment w this line
        draw_snowflake(x1, y1, p1[0], p1[1], t)
        draw_snowflake(p1[0], p1[1], p2[0], p2[1], t)
        draw_snowflake(p2[0], p2[1], p3[0], p3[1], t)
        draw_snowflake(p3[0], p3[1], x2, y2, t)
    else:
        t.up()
        t.setpos(p1[0], p1[1])
        t.down()
        t.setpos(p2[0], p2[1])
        t.setpos(p3[0], p3[1])

        t.up()        
        t.setpos(x1, y1)
        t.down()
        t.setpos(p1[0], p1[1])
        
        t.up()
        t.setpos(p3[0], p3[1])
        t.down()
        t.setpos(x2, y2)

def main():
    t = turtle.Turtle()
    t.hideturtle()

    draw_snowflake(-100, 0, 100, 0, t)

    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()