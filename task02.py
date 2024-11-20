import random
from typing import List

def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """
    Generate a sorted list of unique random numbers for a ticket.

    Parameters:
    min (int): The minimum possible value of the random number (must be at least 1).
    max (int): The maximum possible value of the random number (must be at most 1000).
    quantity (int): The number of unique random numbers to generate (must be between min and max).

    Returns:
    List[int]: A sorted list of unique random numbers, or an empty list if parameters are invalid.
    """
    
    if not (1 <= min <= max <= 1000) or not (min <= quantity <= max - min + 1):
        return []

    picking = set()
    while len(picking) < quantity:
        picking.add(random.randint(min, max))
    
    return sorted(picking)

# Example usage
print(get_numbers_ticket(1, 50, 5))
print(get_numbers_ticket(-1, 50, 5))
print(get_numbers_ticket(1, 1001, 5))
print(get_numbers_ticket(1, 5, 6))