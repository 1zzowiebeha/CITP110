"""Code for Algorithm Workbench Question 4 and 5 from the textbook."""

###############
# Question 4: #
###############
score = 30
A_score = 90
B_score = 80
C_score = 50
D_score = 30

if score >= A_score:
    print('Your grade is A.')
else:
    if score >= B_score:
        print('Your grade is B.')
    else:
        if score >= C_score:
            print('Your grade is C.')
        else:
            if score >= D_score:
                print('Your grade is D.')
            else:
                print('Your grade is F.')
                
# Much much better approach:

if score >= A_score:
    print('Your grade is A.')
elif score >= B_score:
    print('Your grade is B.')
elif score >= C_score:
    print('Your grade is C.')
elif score >= D_score:
    print('Your grade is D.')
else:
    print('Your grade is F.')

###############
# Question 5: #
###############
amount1 = 5
amount2 = 15

if amount1 > 10 and amount2 < 100:
    print( max(amount1, amount2) )
    
    # I could have done an if-statement to check
    #   .. for which variable was greater.
    #   .. This approach is simpler, less lines, and more pythonic