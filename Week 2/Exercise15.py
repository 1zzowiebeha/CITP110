"""A program which reproduces the images depicted in
Starting Out with Python by Tony Gaddis Haywood,
Figure 2-40 via the turtle graphics library."""

import turtle


def shape1():
    """Draw shape 1 from Figure 2-40."""
    
    # Starting position
    turtle.penup()
    turtle.setpos(-300, 200)
    
    # First diamond
    turtle.fillcolor(255, 255, 255)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setpos(-250, 250)
    turtle.setpos(-200, 200)
    turtle.setpos(-250, 150)
    turtle.setpos(-300, 200)
    turtle.end_fill()
    
    # Second start position
    turtle.penup()
    turtle.setpos(-200, 200)
    
    # Second diamond
    turtle.fillcolor(255, 255, 255)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setpos(-150, 250)
    turtle.setpos(-100, 200)
    turtle.setpos(-150, 150)
    turtle.setpos(-200, 200)
    turtle.end_fill()
    

def shape2():
    """Draw shape 2 from Figure 2-40."""
    # Starting Position
    turtle.penup()
    turtle.setpos(150, 200)
    
    # Draw triangle 1
    
    turtle.fillcolor(255, 255, 255)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setpos(250, 200)
    turtle.setpos(200, 250)
    turtle.setpos(150, 200)
    turtle.end_fill()
    
    # Draw triangle 2
    turtle.setpos(200, 300)
    turtle.setpos(250, 200)


def shape3():
    """Draw shape 3 from Figure 2-40."""
    
    # Start position
    turtle.penup()
    turtle.setpos(-250, 50)

    
def shape4():
    """Draw shape 4 from Figure 2-40."""
    pass
    
    
def shape5():
    """Draw shape 5 from Figure 2-40."""
    pass
    
    
def shape6():
    """Draw shape 6 from Figure 2-40."""
    pass
    
    
if __name__ == "__main__":
    # Set color mode to 0-255 instead of 0.0-1.0
    turtle.colormode(255)
    
    # Set drawing to animate instantly
    turtle.speed(0)
    
    # Bluish background
    turtle.bgcolor(255, 255, 244)
    
    # Draw each shape.
    shape1()
    shape2()
    shape3()
    shape4()
    shape5()
    shape6()
    
    # Prevent the window from closing once
    #   images have been drawn.
    turtle.done()