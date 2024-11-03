"""Validation decorator."""

from typing import Callable
import inspect

def validate_argument_types(func: Callable) -> None:
    def wrapper(*args, **kwargs):
        signature = inspect.signature(func)
        
        #for param, value in signature.parameters.items():
        #    print(param, value)
            
        func(*args, **kwargs)
    
    return wrapper

# runs only upon program start??
# confusing. I'll look into it tomorrow.
# def validate_argument_types(func: Callable) -> None:
#     signature = inspect.signature(func)
    
#     def wrapper(*args, **kwargs):
#         for param, value in signature.parameters.items():
#             print(param, value)
    
#     print('start')
#     wrapper()
#     print('end')
    
#     return func