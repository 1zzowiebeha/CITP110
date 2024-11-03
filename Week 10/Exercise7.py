"""Exercise #7 from chapter 10 of the textbook."""

import os
import pickle

from Exercise4 import Employee
from validation import validate_argument_types

HELP_TEXT = """\
Help Menu:
---------------
All changes are automatically saved before you quit the program.

C <name> <job_title> <department> - Create a new employee
A - List all employee information
F <id> - List an employee's information via their ID
D <id> - Delete an employee via their ID
U - (not yet implemented) Discard all changes and revert back to loaded db state

H - Display help text
S - Manually save current database information

Q - Exit the program (and save changes)
Q! - Exit the program and discard changes (DOES NOT save changes)
"""

# Todo:
#   implement argument checks
#   cleanup comments and documentation
#   implement update command
#   implement discard changes command (with an are you sure confirmation)

class CommandSystem:    
    def __init__(self):
        # I would decouple this somehow..
        self._command_table = {
            'C': self.create_employee,       # create employee
            'A': self.show_all_employee_info,# list all employees
            'F': self.show_employee_info,    # list specific employee
            'D': self.delete_employee,       # delete employee
            'H': self.show_helptext,         # show help text
            'S': self.save_state,            # save changes (Creations/Deletions)
            #'Q': self.quit_and_save,         # save changes and quit
            #'U': self.unstage_changes,       # discard changes and reload virtual db with original db
        }
            
        # Load all saved employee data
        # A little too stateful:
        program_parent_dir = os.path.join(os.path.dirname(__file__), '.')
        self.db_file_path = os.path.join(program_parent_dir, 'employees.pickle')
        self._load_data()
        
        # Keep track of employee changes (private)
        # created
        # deleted
        # updated?
        # All changes staged for _loaded_employee_db (unsaved changeset)
        # Currently not in use
        self._employee_db_change_set = []
    
    def interpret_command(self, user_input: str):
        command_pieces = user_input.split(' ')

        if command_pieces:
            try:
                command_to_execute = self._command_table[command_pieces[0].upper()]
            except KeyError:
                # User entered an invalid command
                print("Error: Invalid command. See the help text ('H') to view available commands.")
            else:
                # If any command arguments exist, send them to the command's function.
                # Utilizes list unpacking, lenient list range behavior
                command_to_execute(*command_pieces[1:])
                
        # User didn't enter anything
        else:
            return
        
    def show_all_employee_info(self):
        """Display all employee information."""
        employee_length = len(self._saved_employee_virtual_db)
        
        print("\nAll Employee Information Report:")
        print("###########################")
        print(f"\nThere are {employee_length} employees.\n")
        for employee in self._saved_employee_virtual_db:
            print(employee)
        
    def show_helptext(self):
        """Display user help text."""
        print(HELP_TEXT)
    
    @validate_argument_types
    def show_employee_info(self, employee_id: int) -> None:
        try:
            int(employee_id)
        except ValueError:
            print("Error: Employee ID must be number.\n")
            return
        
        for employee in self._saved_employee_virtual_db:
            if employee.id == employee_id:
                print(employee)
                return
        
        print(f"Error: Employee #{employee_id} not found.\n")
    
    @validate_argument_types
    def create_employee(self, id: int, name: str,
                        job_title: str, department: str) -> Employee:
        """Create an employee."""

        # make id optional and implement this in the future:
        # query the db for highest id and set new employee id to be one higher
        # too much work for a simple app like this though
        #if id is None:
        #    get
        
        employee = Employee(name, id, department, job_title)
        self._employee_db_change_set.append(('create', employee))
        self._saved_employee_virtual_db.append(employee)
        
        print("Employee created.\n")
        
        return employee
    
    @validate_argument_types
    def delete_employee(self, employee_id: int) -> None:
        try:
            int(employee_id)
        except ValueError:
            print("Error: Employee ID must be number.\n")
            return
        
        for employee in self._saved_employee_virtual_db:
            if employee.id == employee_id:
                self._employee_db_change_set.append(('delete', employee))
                self._saved_employee_virtual_db.remove(employee)
                print(f"Removed {employee.name}\n")
        
    def save_state(self):
        """Serialize changes."""
        with open(self.db_file_path, 'wb') as file_object:
            # Eventually make it so the changeset db
            #   is what syncs to the virtual employee db.
            # The user can pick and choose what changes to apply to the virtual db.
            # Or, they can pick and choose what changes to apply to the real db
            #   (like how git operates).
            # Then, save the virtual db to the file upon save.
            # for change_set in self._employee_db_change_set:
            #     # for maintainability I would make this an enum
            #     if change_set[0] == 'create':
            #         self._loaded_employee_db.append(change_set[1])
            #     elif change_set[0] == 'delete':
            #         self._loaded_employee_db.remove(change_set[1])
            # requires keeping track of more stuff
            # ill do this later
            #elif change_set[0] == 'update':
            #    self._loaded_employee_db.append(change_set[1])
            
            # Save virtual employee db to the file
            pickle.dump(self._saved_employee_virtual_db, file_object, protocol=2)
            
        
    def _load_data(self):
        """Rehydrate pickled employee objects."""
        if os.path.exists(self.db_file_path):
            with open(self.db_file_path, 'rb') as file_object:
                self._loaded_employee_db = pickle.load(file_object, encoding="UTF-8")
                # Virtual _loaded_employee_db (unsaved representattion of applied changes)
                # Just a list of employee objects.
                # Make a copy instead of direct reference to loaded db contents
                self._saved_employee_virtual_db = self._loaded_employee_db[:]
        else:
            print("Could not find existing employee data.\nNew empty db created.")
            self._loaded_employee_db = []
            self._saved_employee_virtual_db = []
    

if __name__ == "__main__":
    print("Welcome to the employee management system.\n")
    print(HELP_TEXT)
    print()
    
    processor = CommandSystem()
    
    while True:
        command = input("> ")
        
        # Exit program without saving
        # In the future, decouple this from the main logic loop
        if command.lower() == 'q!':
            print("Shutting down...")
            break
        elif command.lower() == 'q':
            print("Shutting down...")
            processor.save_state()
            break
        
        processor.interpret_command(command)