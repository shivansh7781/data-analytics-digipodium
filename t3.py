from turtle import *

speed('fastest')
colors =['red','blue','purple','pink','black']
pensize=2
for i in range(100):
    #print(i%5,colors[i%5])
    pencolor(colors[i%5])
    fd(i*2)
    lt(100)
    circle(i*2,70)

mainloop()

