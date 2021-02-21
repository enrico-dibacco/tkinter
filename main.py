from tkinter import *
import math

root = Tk()
root.title("Simple plot using canvas and line")

screen_width = 1200
screen_height = 600
center = screen_height//2


cartesian_w = 40
cartesian_h = 20


def mapToScreen(x, y):
    # convert a point in the cartesian plane to a point on the screen
    X = (x*screen_width)//cartesian_w + screen_width//2
    Y = -(y*screen_height)//cartesian_h + screen_height//2
    return (X, Y)


c = Canvas(width=screen_width, height=screen_height, bg='white')
c.pack()

str1 = "sin(x)=blue"
c.create_text(10, 20, anchor=SW, text=str1)

center_line = c.create_line(0, center, screen_width, center, fill='green')

# create the coordinate list for the sin() curve, have to be integers
xy1 = []
step = cartesian_w/screen_width
x = -cartesian_w/2
for i in range(screen_width):
    y = 4*math.sin(x)
    P = mapToScreen(x, y)
    # x coordinates
    xy1.append(P[0])
    # y coordinates
    xy1.append(P[1])
    x = x + step

sin_line = c.create_line(xy1, fill='blue')

root.mainloop()
