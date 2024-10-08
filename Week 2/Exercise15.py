"""A program which reproduces the images depicted in
Starting Out with Python by Tony Gaddis Haywood,
Chapter 2 Figure 2-40 via the turtle graphics library."""

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
    # In this intricate and angled shape, it will be easier
    # .. to specify angles via .right() and .left().
    
    # Start position
    turtle.penup()
    turtle.setpos(-250, 50)
    
    # Draw Square 1
    turtle.pendown()
    for repetition in range(4):
        turtle.forward(60)
        turtle.left(90)
    
    # Square 2 start pos
    turtle.forward(60)
    
    # Draw Square 2
    for repetition in range(4):
        turtle.forward(60)
        turtle.right(90)
        
    # Draw line through squares
    turtle.right(45)
    # Meh I'm kind of lazy to use the pythagorean theorem
    #   .. to calculate the correct hypotenuse length.
    #   The numbers 85 & 170 look good enough.
    turtle.forward(85)
    turtle.right(180)
    turtle.forward(170)
    
    # Triangle 1 start pos
    turtle.right(135)
    turtle.forward(60)
    
    # Draw triangle 1
    turtle.right(45)
    # Same here. 85 is a hypotenuse which looks good,
    #   .. but might not be mathematically perfect.
    turtle.forward(85)

    # Start pos for triangle 2
    turtle.right(45)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    
    # Draw Triangle 2
    turtle.right(45)
    turtle.forward(85)

    
def shape4():
    """Draw shape 4 from Figure 2-40."""
 
    # Start pos for shape 4
    turtle.penup()
    turtle.setpos(100, 50)
    
    # Draw 5 circles
    for repetition in range(5):
        turtle.pendown()
        turtle.circle(20)
        
        # This algorithm will make even circles
        #   .. lower in height, and odd circles
        #   .. higher in height, as is displayed
        #   .. in the book figure's pattern.
        if repetition % 2 == 0:
            # Don't draw the position change
            turtle.penup()
            turtle.setpos(turtle.pos()[0] + 25, turtle.pos()[1] - 20)
        else:
            # Don't draw the position change
            turtle.penup()
            turtle.setpos(turtle.pos()[0] + 25, turtle.pos()[1] + 20)
    
    
def shape5():
    """Draw shape 5 from Figure 2-40."""
    turtle.penup()
    turtle.setpos(-250,-160)
    
    # I could write the text a bit away from the
    #   .. line so the text doesn't intersect with
    #   .. the line, but I will leave this for now.
    
    # Draw circle in the middle of + sign
    turtle.pendown()
    turtle.circle(20)
    
    turtle.penup()
    # Reset angle
    turtle.setheading(90)
    # Magic numbers that place the cursor
    #   .. mostly in the center of the circle.
    turtle.setpos(-264,-174)
    
    # Draw + sign
    # Bottom
    turtle.pendown()
    turtle.forward(100)
    turtle.write("South")
    
    # Top
    turtle.right(180)
    turtle.forward(200)
    turtle.write("North")
    
    # (back to center)
    turtle.right(180)
    turtle.forward(100)
    
    # Right
    turtle.right(90)
    turtle.forward(100)
    turtle.write("East")
    
    # To center then Left
    turtle.right(180)
    turtle.forward(200)
    turtle.write("West")
    
    
def shape6():
    """Draw shape 6 from Figure 2-40."""
    
    # Start pos
    turtle.penup()
    turtle.setpos(130, -140)
    turtle.setheading(0)
    
    # Draw 2 dashed lines with dot points at the ends
    for line in range(2):
        # Write line 2:
        if line == 1:
            turtle.penup()
            turtle.setpos(130, -240)
            turtle.pendown()
        
        turtle.dot(10)
        
        turtle.pendown()
        turtle.forward(10)
        
        turtle.penup()
        turtle.forward(10)
        
        turtle.pendown()
        turtle.forward(20)
        
        turtle.penup()
        turtle.forward(10)
        
        turtle.pendown()
        turtle.forward(20)
        
        turtle.penup()
        turtle.forward(10)
        
        turtle.pendown()
        turtle.forward(10)
        
        turtle.dot(10)
        
    # Draw 2 side lines
    turtle.setpos(220, -140)
    turtle.penup()
    turtle.setpos(130, -140)
    turtle.pendown()
    turtle.setpos(130, -240)
    
    # Draw 2 triangle hypotenuses
    # Numbers are estimates and not mathematically accurate
    turtle.setpos(220, -140)
    turtle.penup()
    turtle.setpos(220, -240)
    turtle.pendown()
    turtle.setpos(130, -140)
    
    # Draw dot in the middle of the square
    turtle.penup()
    turtle.setpos(175, -190)
    turtle.dot()
    
    
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