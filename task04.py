from datetime import datetime, timedelta, date
from typing import List, Dict



def is_date_within_days(target_date: datetime, days: int) -> bool:
    """
    Check if a given date (ignoring the year) falls within the next 'days' days from today, including today.
    If the date has already passed this year, consider the date for the next year.

    Parameters:
    target_date (datetime): The date to check.
    days (int): Number of days to look ahead.

    Returns:
    bool: True if the date is within the next 'days' days including today, False otherwise.
    """
    today_date = datetime.now().date()
    
    date_this_year = date(today_date.year, target_date.month, target_date.day)
    
    if date_this_year < today_date:
        target_date = date(today_date.year + 1, target_date.month, target_date.day)
    else:
        target_date = date_this_year
    
    return today_date <= target_date <= (today_date + timedelta(days=days))



def adjust_to_weekday(date_obj: date) -> date:
    """
    Adjust the given date to the next weekday if it falls on a weekend.

    Parameters:
    date_obj (date): The date to adjust.

    Returns:
    date: The adjusted date.
    """
    if date_obj.weekday() == 5:  # Saturday
        return date_obj + timedelta(days=2)
    elif date_obj.weekday() == 6:  # Sunday
        return date_obj + timedelta(days=1)
    return date_obj



def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Generate a list of users whose birthdays fall within the next week.

    Parameters:
    users (List[Dict[str, str]]): A list of user dictionaries with 'name' and 'birthday' keys.

    Returns:
    List[Dict[str, str]]: A list of dictionaries with user names and upcoming congratulation dates.
    """
    upcoming_birthdays_list = []
    days = 7

    for user in users:
        try:
            user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d")

            if is_date_within_days(user_birthday, days):

                current_year = datetime.now().year
                congratulation_date = date(current_year, user_birthday.month, user_birthday.day)
                
                congratulation_date = adjust_to_weekday(congratulation_date)

                upcoming_birthdays_list.append({
                    "name": user["name"],
                    "birthday": congratulation_date.strftime("%Y.%m.%d")
                })

        except ValueError:
            pass

    return upcoming_birthdays_list



users = [
    {"name": "Jane", "birthday": "1990.07.05"},
    {"name": "Ted", "birthday": "1985.07.10"},
    {"name": "Mary", "birthday": "1990.07.13"},
    {"name": "Alice", "birthday": "1995.07.15"},
    {"name": "Bob", "birthday": "1995.07.07"},
    {"name": "Bob", "birthday": "1995.07.06"}
]



upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
