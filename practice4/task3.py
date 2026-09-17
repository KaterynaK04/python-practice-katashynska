print("Kateryna Katashynska, IT-31")

name = "Kateryna"
surname = "Katashynska"

text = name + surname

vowels = "aeiouy"

vowels_count = 0
consonants_count = 0

for char in text.lower():
    if char in vowels:
        vowels_count += 1
    else:
        consonants_count += 1

print(f"{name} {surname}")
print(f"Vowels: {vowels_count}, consonants: {consonants_count}")
print(f"Total letters: {len(text)}")
print(f"Check: {vowels_count + consonants_count == len(text)}")