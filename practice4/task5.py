print("Kateryna Katashynska, IT-31")

d = 4
c = 11

n = d * c

print(f"n = {d} * {c} = {n}")

divisors = []
divisors_sum = 0

for number in range(1, n + 1):
    if n % number == 0:
        divisors.append(number)
        divisors_sum += number

print("Divisors:", *divisors)
print(f"Divisors count: {len(divisors)}, sum: {divisors_sum}")

# Checking whether n is prime

if n < 2:
    print(f"{n} is not prime")
else:
    for number in range(2, n):
        if n % number == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")

# Finding all prime numbers from 2 to n

primes = []

for number in range(2, n + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        primes.append(number)

print("Primes up to", n, ":", *primes)
print(f"Primes count: {len(primes)}")