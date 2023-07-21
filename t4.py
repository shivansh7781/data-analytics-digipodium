from turtle import*

speed('fastest')
pensize(2)
bgcolor('black')
pencolor('white')
colors=['red','white','green','pink','purple']
side =5
for i in range(side):
    fd(100)
    for i in range(side):
        fd(60)
        lt(360/side)
        begin_fill()
        fillcolor(colors[i%5])
        for i in range(side):
            fd(40)
            lt(360/side)
        end_fill()
    lt(360/side)

hideturtle()
mainloop()
