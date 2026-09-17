name = "Kateryna"
surname = "Katashynska"
group = "IT-31"
y = 2008


def print_age(year):
    """Print age and return nothing explicitly."""
    age = 2026 - year
    print(f"Age: {age}")


def get_age(year, current_year=2026):
    """Return age or -1 when the year is invalid."""
    if year > current_year or year < 0:
        return -1

    age = current_year - year
    return age
    print("after return")


def main():
    """Run demonstrations of print and return."""
    print(f"{name} {surname}, {group}")

    print_age(y)

    print("print_age returned:", print_age(y))

    age = get_age(y)
    print("Age from get_age:", age)
    print("Age in months:", age * 12)
    print("Age in weeks:", age * 52)

    print("Age in 2030:", get_age(y, current_year=2030))

    print("Invalid year 3000 gives:", get_age(3000))

    try:
        print_age(y) * 12
    except TypeError as error:
        print(f"TypeError: {error}")


main()