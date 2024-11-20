from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days from the given date to today.
    
    Parameters:
    date (str): The date string in the format 'YYYY-MM-DD'.
    
    Returns:
    int: The number of days from the given date to today. Returns -1 if the date format is invalid.
    """
    try:
        today_date = datetime.now()
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        delta = today_date - date_obj
        
        return delta.days
    
    except ValueError:
        return -1

# Test cases
print(get_days_from_today("2024-07-05"))
print(get_days_from_today("2026-10-09"))
print(get_days_from_today("2021-10-09"))
