print("Kateryna Katashynska, IT-31")

day = int(input("Enter the day of birth (integer): "))
month = int(input("Enter the month of birth (integer): "))
year = int(input("Enter the year of birth (integer): "))

if year <= 0:
    print("Date is invalid: year must be positive")
elif month < 1 or month > 12:
    print("Date is invalid: month must be between 1 and 12")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_day = 29
        else:
            max_day = 28
    elif month in (4, 6, 9, 11):
        max_day = 30
    else:
        max_day = 31

    if day < 1:
        print("Date is invalid: day must be positive")
    elif day > max_day:
        print(f"Date is invalid: month {month} has only {max_day} days")
    else:
        print("Date is valid")