def is_leap_year(year):
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year):
    
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28

def find_next_date(day, month, year):
    
    days_in_month = get_days_in_month(month, year)

    if day < days_in_month:
        day += 1
    elif month < 12:
        day = 1
        month += 1
    else:
        day = 1
        month = 1
        year += 1

    return day, month, year

try:
    
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    
    
    next_day, next_month, next_year = find_next_date(day, month, year)

    
    print(f"The next date is: {next_day}-{next_month}-{next_year}")

except ValueError as e:
    print(f"Error: {e}")
