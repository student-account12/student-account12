class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")

# Example usage
student1 = Student("John Doe", "12345", "A")
student1.display_info()