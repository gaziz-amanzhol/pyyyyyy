# Example 1: Simple generator function
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))

# Example 2: Generator with loop
def countdown(num):
    while num > 0:
        yield num
        num -= 1

for i in countdown(5):
    print(i)

# Example 3: Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(10):
    print(num, end=" ")
print()

# Example 4: Range generator
def my_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step

for i in my_range(0, 10, 2):
    print(i)

# Example 5: Even numbers generator
def even_numbers(max_num):
    num = 0
    while num <= max_num:
        yield num
        num += 2

for even in even_numbers(20):
    print(even, end=" ")
print()

# Example 6: Generator expression
squares = (x**2 for x in range(1, 6))
for square in squares:
    print(square)

# Example 7: File reader generator
def read_large_file(file_path):
    """Generator for reading large files line by line"""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {file_path} not found")

# Example 8: Infinite sequence generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))

# Example 9: Generator with filtering
def filtered_range(start, end, divisor):
    for num in range(start, end):
        if num % divisor == 0:
            yield num

for num in filtered_range(1, 20, 3):
    print(num, end=" ")
print()

# Example 10: Prime numbers generator
def prime_generator(limit):
    for num in range(2, limit):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

for prime in prime_generator(30):
    print(prime, end=" ")
print()
