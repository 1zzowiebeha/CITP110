

class A:
    def __init__(self) -> None:
        self._var = 'hi'
        
    def say(self, message: str) -> None:
        print(message)
        
class B(A):
    def __init__(self) -> None:
        # to learn: how does a call to A differ from super()?
        # how does this work under the hood?
        
        # also: GIL, GIL w/ multithreading, GIL w/ async
        A.__init__(self)
        # alternatively,
        # super().__init__(self)
        self._var2 = 'wow'