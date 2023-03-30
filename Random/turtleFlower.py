from turtle import *

ht()
speed()
pensize(1.2)
shape('turtle')

for i in range(24):
    for j in range(6):
        left(60)

        fillcolor('cyan')
        up()
        setpos(0,0)
        down()
        circle((600-(i*25)),60)
        up()
        setpos(0,0)
        down()
        circle(-(600-(i*25)),60)
        end_fill()

        fillcolor('yellow')
        up()
        setpos(0,0)
        down()
        circle((587.5-(i*25)),60)
        up()
        setpos(0,0)
        down()
        circle(-(587.5-(i*25)),60)
        end_fill()

mainloop()