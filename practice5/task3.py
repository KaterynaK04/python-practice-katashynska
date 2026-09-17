name = "Kateryna"
surname = "Katashynska"
group = "IT-31"
c = len(surname)


def get_initials(name: str, surname: str) -> str:
    """Return initials in the I.P. format."""
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    return text.lower().count(letter.lower())


def count_vowels(text: str) -> int:
    """Return the number of English vowels in text."""
    vowels = "aeiouy"
    return sum(count_letters(text, letter=vowel) for vowel in vowels)


def reverse_text(text: str) -> str:
    """Return text in reverse order using a loop."""
    result = ""

    for char in text:
        result = char + result

    return result


print(f"{name} {surname}, {group}")

print("Initials:", get_initials(name, surname))

print("Letters in surname:", c)

vowels = count_vowels(surname)
consonants = c - vowels

print(f"Vowels: {vowels}, consonants: {consonants}")

for vowel in "aeiou":
    print(f"{vowel}:", count_letters(surname, letter=vowel))

print("Default letter 'a':", count_letters(surname))

print("Reversed surname:", reverse_text(surname))

print("Docstring:", count_letters.__doc__)

print("Annotations:", count_letters.__annotations__)