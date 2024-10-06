"""Exercise 14 from Chapter 7 of our textbook.
Be sure to use a virtual environment and install
matplotlib and numpy via pip if you use a desktop installation of python.
"""

import matplotlib.pyplot as plt
import numpy as np
import os

def get_csv_columns(csv_path: str) -> list:
    """Retrieve csv file column names."""
    with open(csv_path, 'r') as file_object:
        for line in file_object:
            columns = line.split(',')
            # Strip whitespace
            for index, column in enumerate(columns):
                columns[index] = column.strip()

            # exit after first line (since we only need that one)
            return columns
    
    
def get_csv_values(csv_path: str) -> list:
    """Retrieve values in csv file.
    Return a multi-dimensional array to deliminate value rows."""
    with open(csv_path, 'r') as file_object:
        values = []
        
        first_line_skipped = False
        for line in file_object:
            # Skip first column definition line
            if not first_line_skipped:
                first_line_skipped = True
                continue
            
            line_values = line.split(',')
            # Strip whitespace
            for index, value in enumerate(line_values):
                # Convert to float to avoid
                # .. display issues with matplotlib
                line_values[index] = float(value.strip())

            values.append(line_values)
            
        return values


if __name__ == "__main__":
    csv_file_path = os.path.join(os.getcwd(), 'expenses.csv')
    
    categories = get_csv_columns('expenses.csv')
    # Get first row of multi-dimentional array
    values = get_csv_values('expenses.csv')[0]
    
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.set_title('Expense history')

    ax.bar(categories, values)
    
    plt.show()
    # yay