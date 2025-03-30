# Exercise 2: **kwargs Usage
# Create a function that takes keyword arguments and prints out the person's details, including first_name, last_name, and age. If any of these details are missing, print Unknown.

# Hint: Use **kwargs to handle named arguments.

def person_details(**kws):
    for key, value in kws.items():
        # If the value is None, replace it with "Unknown"
        if value is None:
            value = "Unknown"
        print(f"{key}: {value}")

# Test the function with some values
person_details(first_name="John", last_name="Doe", age=30)
# Output: First Name: John, Last Name: Doe, Age: 30

person_details(first_name="Alice", age=25)
# Output: First Name: Alice, Last Name: Unknown, Age: 25


