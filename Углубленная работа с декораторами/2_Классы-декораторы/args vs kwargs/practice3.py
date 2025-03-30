# Exercise 3: Combining *args and **kwargs
# Create a class Student that accepts a list of subjects (as *args) and personal information (like name, age, etc., as **kwargs). Write a method that prints the student’s name, age, and list of subjects.

class Student:
    def __init__(self, *a, **kw):
        self.a = a  # Positional arguments (name and subjects)
        self.kw = kw  # Keyword arguments (like age)
    
    def display_info(self):
        name = self.a[0]  # First positional argument is the name
        age = self.kw.get("age", "Unknown")  # Get the age from kwargs, default to "Unknown" if not provided
        subjects = self.a[1:]  # All subjects are after the first argument (name)

        # Print the student's info
        print(f"Name: {name}, Age: {age}, Subjects: {subjects}")
        
# Creating Student objects
student1 = Student("John", "Math", "Science", age=20)
student2 = Student("Alice", "History", age=22)

# Displaying the info for both students
student1.display_info()  # Output: Name: John, Age: 20, Subjects: ['Math', 'Science']
student2.display_info()  # Output: Name: Alice, Age: 22, Subjects: ['History']
