"""Exercise #15 from our textbook."""

# Just one repetition
for repetition_count in range(1):
    # Spaces between pound signs
    for space_count in range(6):
        # A string multiplied by a number
        # .. results in that string repeated.
        space_string = ' ' * space_count
        
        print(f"#{space_string}#")