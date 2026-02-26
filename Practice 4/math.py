import math
import random

# Example 1: Built-in math functions
numbers = [5, 2, 8, 1, 9, 3]
print("Numbers:", numbers)
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))

# Example 2: abs(), round(), pow()
print("\nabs(-7.5):", abs(-7.5))
print("round(3.7):", round(3.7))
print("round(3.14159, 2):", round(3.14159, 2))
print("pow(2, 3):", pow(2, 3))
print("pow(5, 2):", pow(5, 2))

# Example 3: math.sqrt(), math.ceil(), math.floor()
print("\nmath.sqrt(16):", math.sqrt(16))
print("math.sqrt(2):", math.sqrt(2))
print("math.ceil(4.3):", math.ceil(4.3))
print("math.floor(4.9):", math.floor(4.9))

# Example 4: math.pi and math.e
print("\nmath.pi:", math.pi)
print("math.e:", math.e)

circle_radius = 5
area = math.pi * circle_radius ** 2
circumference = 2 * math.pi * circle_radius
print(f"Circle radius: {circle_radius}")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

# Example 5: Trigonometric functions
angle = math.pi / 4  # 45 degrees
print(f"\nAngle: {angle} radians ({math.degrees(angle)} degrees)")
print("sin:", math.sin(angle))
print("cos:", math.cos(angle))
print("tan:", math.tan(angle))

# Example 6: math.radians() and math.degrees()
angle_deg = 90
angle_rad = math.radians(angle_deg)
print(f"\n{angle_deg} degrees = {angle_rad} radians")
print(f"sin(90°) = {math.sin(angle_rad)}")

angle_rad2 = math.pi
angle_deg2 = math.degrees(angle_rad2)
print(f"{angle_rad2} radians = {angle_deg2} degrees")

# Example 7: math.factorial()
print("\nFactorials:")
for i in range(6):
    print(f"{i}! = {math.factorial(i)}")

# Example 8: math.gcd() and math.lcm()
a, b = 48, 18
print(f"\nGCD of {a} and {b}:", math.gcd(a, b))
print(f"LCM of {a} and {b}:", math.lcm(a, b))

# Example 9: random.random()
print("\nRandom float [0.0, 1.0):")
for _ in range(5):
    print(random.random())

# Example 10: random.randint()
print("\nRandom integers between 1 and 10:")
for _ in range(5):
    print(random.randint(1, 10))

# Example 11: random.choice()
colors = ["red", "blue", "green", "yellow", "purple"]
print("\nRandom color:")
for _ in range(5):
    print(random.choice(colors))

# Example 12: random.shuffle()
cards = ["A", "K", "Q", "J", "10", "9"]
print("\nOriginal:", cards)
random.shuffle(cards)
print("Shuffled:", cards)

# Example 13: random.sample()
numbers = list(range(1, 51))
lottery = random.sample(numbers, 6)
print("\nLottery numbers:", sorted(lottery))

# Example 14: random.uniform()
print("\nRandom float between 10.0 and 20.0:")
for _ in range(5):
    print(f"{random.uniform(10.0, 20.0):.2f}")

# Example 15: Generate random password
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("\nRandom passwords:")
for _ in range(3):
    print(generate_password())

# Example 16: Monte Carlo Pi estimation
def estimate_pi(num_points=10000):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            inside_circle += 1
    return 4 * inside_circle / num_points

estimated_pi = estimate_pi(100000)
print(f"\nEstimated π: {estimated_pi}")
print(f"Actual π: {math.pi}")
print(f"Error: {abs(estimated_pi - math.pi):.6f}")
