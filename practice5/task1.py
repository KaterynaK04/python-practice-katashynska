name = "Kateryna"
surname = "Katashynska"
group = "IT-31"
year = 2008


def print_card():
    """Print the student's personal card without parameters."""
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {year}")


def print_card_args(name, surname, group=group, year=year):
    """Print the student's personal data passed as arguments."""
    print(f"{name} {surname}, {group}, {year}")


print(f"{name} {surname}, {group}")

print("--- no parameters, call 1 ---")
print_card()

print("--- no parameters, call 2 ---")
print_card()

print("--- no parameters, call 3 ---")
print_card()

print("--- positional arguments ---")
print_card_args(name, surname, group, year)

print("--- keyword arguments ---")
print_card_args(year=year, group=group, surname=surname, name=name)

print("--- mixed arguments ---")
print_card_args(name, surname, group=group, year=year)

print("--- default group ---")
print_card_args(name, surname, year=year)

print("--- missing arguments error ---")
try:
    print_card_args("Ivan")
except TypeError as error:
    print(f"TypeError: {error}")

print("--- invalid syntax example ---")
print('print_card_args(name="Ivan", "Petrenko")')
print("SyntaxError: positional argument follows keyword argument")