print("Kateryna Katashynska, IT-31")

d = 4
c = 11

count = 0
total = 0
product = 1
even = 0
odd = 0

print(f"Numbers from {d} to 31:", end=" ")

for number in range(d, 32):
    print(number, end=" ")

    count += 1
    total += number
    product *= number

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print()
print(f"Count: {count}")
print(f"Sum: {total}")
print(f"Product: {product}")
print(f"Average: {total / count:.2f}")
print(f"Even: {even}, odd: {odd}")

# while version

count_w = 0
total_w = 0
product_w = 1
even_w = 0
odd_w = 0

number = d

while number <= 31:
    count_w += 1
    total_w += number
    product_w *= number

    if number % 2 == 0:
        even_w += 1
    else:
        odd_w += 1

    number += 1

print("\nWhile version:")
print(f"Count: {count_w}")
print(f"Sum: {total_w}")
print(f"Product: {product_w}")
print(f"Average: {total_w / count_w:.2f}")
print(f"Even: {even_w}, odd: {odd_w}")

print("Countdown:", end=" ")
for number in range(c, 0, -1):
    print(number, end=" ")
print()