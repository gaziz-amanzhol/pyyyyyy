import datetime
from datetime import date, time, timedelta

# Example 1: Current date and time
now = datetime.datetime.now()
print("Current datetime:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Example 2: Creating date objects
my_date = date(2024, 12, 25)
print("\nCustom date:", my_date)

today = date.today()
print("Today:", today)

# Example 3: Creating time objects
my_time = time(14, 30, 45)
print("\nTime:", my_time)
print("Hour:", my_time.hour)
print("Minute:", my_time.minute)
print("Second:", my_time.second)

# Example 4: Date formatting with strftime()
now = datetime.datetime.now()
print("\nFormatted dates:")
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%B %d, %Y"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A, %B %d, %Y"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%I:%M %p"))

# Example 5: Parsing dates with strptime()
date_string = "2024-12-25"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("\nParsed date:", parsed_date)

date_string2 = "December 25, 2024"
parsed_date2 = datetime.datetime.strptime(date_string2, "%B %d, %Y")
print("Parsed date 2:", parsed_date2)

# Example 6: Calculating time differences
date1 = date(2024, 1, 1)
date2 = date(2024, 12, 31)
difference = date2 - date1
print("\nDays between dates:", difference.days)

# Example 7: Adding/subtracting time
today = date.today()
one_week = timedelta(weeks=1)
next_week = today + one_week
last_week = today - one_week

print(f"\nToday: {today}")
print(f"Next week: {next_week}")
print(f"Last week: {last_week}")

# Example 8: Working with timedelta
delta = timedelta(days=30, hours=12, minutes=30)
print(f"\nTimedelta: {delta}")
print(f"Total seconds: {delta.total_seconds()}")

future_date = datetime.datetime.now() + delta
print(f"Future date: {future_date}")

# Example 9: Comparing dates
date1 = date(2024, 1, 1)
date2 = date(2024, 12, 31)

print(f"\n{date1} < {date2}:", date1 < date2)
print(f"{date1} > {date2}:", date1 > date2)
print(f"{date1} == {date2}:", date1 == date2)

# Example 10: Age calculator
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    return age

birth = date(2000, 5, 15)
age = calculate_age(birth)
print(f"\nBirth date: {birth}")
print(f"Age: {age} years")

# Example 11: Days until event
def days_until(target_date):
    today = date.today()
    delta = target_date - today
    return delta.days

new_year = date(2025, 1, 1)
days = days_until(new_year)
print(f"\nDays until New Year 2025: {days}")

# Example 12: Weekday operations
today = date.today()
print(f"\nToday: {today}")
print(f"Weekday: {today.strftime('%A')}")
print(f"Weekday number: {today.weekday()}")  # Monday = 0
print(f"ISO weekday: {today.isoweekday()}")  # Monday = 1
