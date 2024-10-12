"""Exercise 3 from Chapter 8 of our textbook."""

from datetime import datetime
from dateutil.parser import parse


if __name__ == "__main__":
    # Union type hint. Assign None to parsed_date
    parsed_date: datetime | None = None

    # Newline to separate prior terminal output from current output
    print()
    
    while parsed_date is None:
        # Other formats work with dateutil.parser.parse too.
        # A fix for this might be to design a custom parserinfo subclass to
        #   .. limit available date formats to mm/dd/yyyy.
        date_input = input("Please enter a date in MM/DD/YYYY format: ")
        try:
            parsed_date = parse(date_input)
        except ValueError:
            print("Error: The date you provided was not in an accepted format.")
     
    print(parsed_date.strftime('%B %d, %Y'))