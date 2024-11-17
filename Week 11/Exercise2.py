"""Exercise #2 from chapter 11 of the textbook."""


class ShiftSupervisor:
    def __init__(self, name: str, salary: int, yearly_bonus: int) -> None:
        # Private, as it is a bit stateful. Without an
        #   interface for developers, we don't want them
        #   to mess with it.
        # In real codebases, use a single underscore instead of name mangling
        #   to denote private variables, like so:
        self._name = name
        self._salary = salary
        self._yearly_bonus = yearly_bonus
        
        self._exceeded_production_goals = False
        
    def set_yearly_bonus(self, exceeded_production_goals: bool) -> None:
        self._exceeded_production_goals = exceeded_production_goals
        
    def get_w2_earnings(self) -> int:
        earnings = self._salary
        if self._exceeded_production_goals:
            earnings += self._yearly_bonus
            
        return earnings
    
    def __str__(self) -> str:
        return self._name
    
    
if __name__ == "__main__":
    # Underscores within numbers are purely a visual aid for developers.
    supervisor1 = ShiftSupervisor(
        'Jerry', 90_000, 500
    )
    
    supervisor1.set_yearly_bonus(True)
    earnings = supervisor1.get_w2_earnings()
    
    print(f"{supervisor1} will earn ${earnings:,} this year.")