class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")


student1 = Student("Aamna Ashraf Rajput", 85)
student1.display()
student2 = Student("Ameen Alam", 95)
student2.display()
student3 = Student("Wajahat Ali Khan", 98)
student3.display()