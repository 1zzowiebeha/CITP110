Strings can be compared via >, >=, <=, <
Each ascii code will be compared

Walrus operator assigns in an expression
In terms of order, it assigns last once the whole
expression is evaluated.



Formatting specifiers for interpolated strings

print(f"My balance is {bal:,.2f}")

[alignment][width][,][.precision][type]

# Magic numbers
amount = balance * 0.0069

What is 0.0069?
When we return to this line, we won't have a clue.
So it is good practice to comment what these strange numbers do.
Or use a named constant.

INTEREST_RATE = 0.0069
amount = balance * INTEREST_RATE


# Turtle

Outside of the IDLE program,
the turtle window will close instantly once the drawing is finished.

Add turtle.done() once the drawing is finished to keep the window open.



# Loops:
Total number of iterations in a loop =
    inner loop iterations * outer loop iterations
    
for i in range(900):
    for x in range(2):
        pass
        
900*2 = 1800

for i in range(900):
    for x in range(2):
        for z in range(9):
            pass

900*2*9 = 162000


# Else clause in a while / for loop

The else only runs if execution of the loop ended without the use of `break`.
If there is no `break` statement, the else is not a useful control flow.