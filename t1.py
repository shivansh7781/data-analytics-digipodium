from turtle import *

# range(stop)
# range(start,stop)
# range(start,stop,stop)

for i in range(6,40,5):
    fd(120)

    lt(360/6)

    dot(10,'green')
write(i,font=('Calibri',20,'bold'))

#reverse 
goto(100,100)
for i in range(10,0,-1):
    fd(60)
    lt(360/10)
    







mainloop()