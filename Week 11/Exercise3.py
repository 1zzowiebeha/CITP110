"""Exercise #3 from chapter 11 of the textbook."""

# name, address, telephone number - Person
# Customer - customer number, newsletter_subscriber

class Person:
    def __init__(self, name: str, address: str, telephone_number: int) -> None:
        self.name = name
        self.address = address
        self.telephone_number = telephone_number
        
    def __str__(self) -> str:
        return self.name
    
    
class Customer(Person):
    def __init__(self, name: str, address: str, telephone_number: int,
                 customer_number: int, newsletter_subscriber: bool) -> None:
        super().__init__(name, address, telephone_number)
        
        self.customer_number = customer_number
        self.newsletter_subscriber = newsletter_subscriber
        
        
if __name__ == "__main__":
    customer = Customer(
        'Todd', '123 S. Flamingo St.',
        517_555_8372, 1, True
    )
    
    if customer.newsletter_subscriber:
        print(f"{customer} is subscribed.")