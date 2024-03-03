# Create a dictionary to store information about a person
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}

# Accessing values in the dictionary
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Job:", person["job"])

# Adding a new key-value pair
person["email"] = "john@example.com"
print("Email:", person["email"])

# Modifying a value
person["age"] = 31
print("Updated age:", person["age"])

# Removing a key-value pair
del person["job"]
print("Updated dictionary after removing 'job' key:", person)

# Iterating over key-value pairs
print("Iterating over key-value pairs:")
for key, value in person.items():
    print(key + ":", value)
