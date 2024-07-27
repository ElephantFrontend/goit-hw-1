from datetime import datetime

current_date = datetime.today().date()

def get_days_from_today(date: str) -> str:
    date_format = '%Y-%m-%d'
    
    try:
        date_formatted = datetime.strptime(date, date_format).date()
        result = current_date - date_formatted

        return result.days
    except ValueError:
        print('Format date is wrong')
    

get_days_from_today('2020-10-0')