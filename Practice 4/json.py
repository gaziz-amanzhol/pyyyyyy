import json

# Example 1: Converting Python dict to JSON string
python_dict = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

json_string = json.dumps(python_dict)
print("JSON string:")
print(json_string)
print("Type:", type(json_string))

# Example 2: Pretty printing JSON
python_data = {
    "name": "Bob",
    "age": 30,
    "hobbies": ["reading", "gaming", "coding"],
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}

json_formatted = json.dumps(python_data, indent=4)
print("\nFormatted JSON:")
print(json_formatted)

# Example 3: Parsing JSON string to Python
json_string = '{"name": "Charlie", "age": 35, "city": "Paris"}'
python_obj = json.loads(json_string)
print("\nParsed Python object:")
print(python_obj)
print("Name:", python_obj["name"])
print("Age:", python_obj["age"])

# Example 4: Working with JSON arrays
json_array = '[1, 2, 3, 4, 5]'
python_list = json.loads(json_array)
print("\nParsed list:", python_list)

# Example 5: Writing JSON to file
data = {
    "students": [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 78}
    ],
    "class": "Python 101"
}

with open("students.json", "w") as f:
    json.dump(data, f, indent=4)
print("\nData written to students.json")

# Example 6: Reading JSON from file
with open("students.json", "r") as f:
    loaded_data = json.load(f)

print("\nData from file:")
print(json.dumps(loaded_data, indent=2))

# Example 7: Converting Python types to JSON
python_types = {
    "string": "hello",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "null": None,
    "list": [1, 2, 3],
    "dict": {"key": "value"}
}

json_output = json.dumps(python_types, indent=2)
print("\nPython to JSON conversion:")
print(json_output)

# Example 8: Sorting JSON keys
unsorted_dict = {
    "zebra": 1,
    "apple": 2,
    "mango": 3,
    "banana": 4
}

sorted_json = json.dumps(unsorted_dict, indent=2, sort_keys=True)
print("\nSorted JSON:")
print(sorted_json)

# Example 9: Handling special characters
special_data = {
    "message": "Hello \"World\"",
    "path": "C:\\Users\\Documents",
    "unicode": "Привет мир"
}

json_special = json.dumps(special_data, indent=2, ensure_ascii=False)
print("\nJSON with special characters:")
print(json_special)

# Example 10: Working with nested JSON
nested_json = '''
{
    "company": "TechCorp",
    "employees": [
        {
            "name": "Alice",
            "position": "Developer",
            "skills": ["Python", "JavaScript"]
        },
        {
            "name": "Bob",
            "position": "Designer",
            "skills": ["Photoshop", "Illustrator"]
        }
    ]
}
'''

data = json.loads(nested_json)
print("\nCompany:", data["company"])
print("Employees:")
for emp in data["employees"]:
    print(f"  - {emp['name']}: {emp['position']}")
    print(f"    Skills: {', '.join(emp['skills'])}")

# Example 11: Creating JSON from list of objects
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

with open("users.json", "w") as f:
    json.dump(users, f, indent=2)
print("\nUsers saved to users.json")

# Example 12: Reading and modifying JSON
with open("users.json", "r") as f:
    users_data = json.load(f)

users_data.append({"id": 4, "name": "David", "email": "david@example.com"})

with open("users.json", "w") as f:
    json.dump(users_data, f, indent=2)
print("User added and file updated")

# Example 13: JSON validation and error handling
invalid_json = '{"name": "Alice", "age": 25'  # Missing closing brace

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"\nJSON Error: {e}")

# Example 14: Custom JSON encoder
from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

event = {
    "name": "Conference",
    "date": datetime(2024, 12, 25, 14, 30)
}

json_with_date = json.dumps(event, cls=DateTimeEncoder, indent=2)
print("\nJSON with custom encoder:")
print(json_with_date)

# Example 15: Working with sample-data.json (if exists)
sample_data = {
    "products": [
        {"id": 1, "name": "Laptop", "price": 999.99, "in_stock": True},
        {"id": 2, "name": "Mouse", "price": 29.99, "in_stock": True},
        {"id": 3, "name": "Keyboard", "price": 79.99, "in_stock": False}
    ],
    "timestamp": "2024-01-15T10:30:00"
}

with open("sample-data.json", "w") as f:
    json.dump(sample_data, f, indent=2)

print("\nsample-data.json created")

with open("sample-data.json", "r") as f:
    products_data = json.load(f)

print("\nProducts in stock:")
for product in products_data["products"]:
    if product["in_stock"]:
        print(f"  {product['name']}: ${product['price']}")
