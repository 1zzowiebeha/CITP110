
#############
# Question: # What is the output of this program?
#############

# def main():
#  x = 1
#  y = 3.4
#  print(x, y)
#  change_us(x, y)
#  print(x, y)
 
# def change_us(a, b):
#  a = 0
#  b = 0
#  print(a, b)
 
 
# main()


###########
# Answer: #
###########

# 1 3.4
# 0 0
# 1 3.4

# Why?

# A new function-scoped variable is created for parameters when
# .. arguments are passed to a function.
# This new variable references the same value passed to it,
# .. but any changes to this variable don't reflect on the
# .. other variable.
# This is because integers and floats (and a few other datatypes) are immutable types.

# With lists however, and a few other collection datatypes,
# .. because both variables reference the same value,
# .. they reference the same value (same as before). These are called mutable datatypes.
# The difference is that
# .. any list operations (mutations) will affect the items in the list,
# .. thus both references to the same list will reflect a change.
# Reassignment however, will not reassign the original variable reference.

# Here is a TOP-TIER explanation:
# https://www.youtube.com/watch?v=_AEJHKGk9ns