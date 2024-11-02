"""Exercise #4 from chapter 10 of the textbook."""

from typing import List

class Employee:
    def __init__(self, name: str, id: int, department: str, job_title: str) -> None:
        self.name = name
        self.id = id
        self.department = department
        self.job_title = job_title
        
    def __str__(self):
        return f"({self.id}) {self.name} - {self.job_title} in {self.department} dept."


if __name__ == "__main__":
    # A backslash removes the first empty line of a multi-line string.
    data = """\
    Susan Meyers 47899 Accounting Vice President
    Mark Jones 39119 IT Programmer
    Joy Rogers 81774 Manufacturing Engineer
    """
    
    employee1 = Employee(
        "Susan Meyers", 47899, "Accounting", "Vice President"
    )
    employee2 = Employee(
        "Mark Jones", 39119, "IT", "Programmer"
    )
    employee3 = Employee(
        "Joy Rogers", 81774, "Manufacturing", "Engineer"
    )
    
    print("Employees:")
    print("#######################")
    print(employee1, employee2, employee3, sep="\n")