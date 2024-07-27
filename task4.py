from datetime import datetime, timedelta
import calendar

users = [
    {"name": "Alice", "birthday": "1990.08.01"},
    {"name": "Bob", "birthday": "1992.08.05"},
    {"name": "Charlie", "birthday": "1988.07.30"},
    {"name": "Diana", "birthday": "1993.07.29"},
]

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    
    for user in users:
        name = user['name']
        birthday_str = user['birthday']
        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= 7:
            if birthday_this_year.weekday() == calendar.SATURDAY:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == calendar.SUNDAY:
                birthday_this_year += timedelta(days=1)
            
            congratulation_date = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({
                'name': name,
                'congratulation_date': congratulation_date
            })
    
    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print(upcoming_birthdays)
