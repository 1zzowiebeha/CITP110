print("Welcome to the vineyard per row calculator.")
length = input("Enter row length in ft: ")
space = input("Enter space available in ft: ")
gap = input("Enter gap between vines desired in ft: ")

grapevines_possible = (float(length) - 2 * float(space)) / float(gap)

print(f"Grapevines that can fit into the specified dimensions: {grapevines_possible}")