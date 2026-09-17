def read_grade(prompt):
    """Read an integer grade from 0 to 100."""
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Error: digits only")
            continue

        grade = int(value)

        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue

        return grade


def to_letter(grade):
    """Convert a numeric grade to a letter from A to F."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 75:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades):
    """Return the arithmetic mean of a list of grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Return the number of grades greater than limit."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    """Print a complete report for the student's grades."""
    avg = average(grades)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades:", *grades)
    print(f"Average: {avg:.2f} -> {to_letter(round(avg))}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {count_above(grades, avg)}")


def main():
    """Read the student's grades and print the report."""
    name = "Kateryna Katashynska"
    group = "IT-31"

    # Kateryna has 8 letters, so we enter 8 grades.
    n = len("Kateryna")

    print(f"{name}, {group}")

    grades = []

    for i in range(1, n + 1):
        grades.append(read_grade(f"Grade {i} (0-100): "))

    print_report(name, group, grades)


main()