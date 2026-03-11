class Student:
    def __init__(self, name, age, major, gpa, courses):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.course_list = courses  

    def introduce(self):
        print(f"Hello your name is {self.name}, your study is {self.major}")

    def show_gpa(self):
        print(f"your GPA is {self.gpa}")

    def show_major(self):
        print(f"your major is {self.major}")

    def courses(self):
        for course, grade in self.course_list:
            print(f"{course}: {grade}")

    def add_course(self, new_course):
        self.course_list.append(new_course)
        print(f"course {new_course} added")

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        print(f"your gpa updated to {self.gpa}")

    def is_honor(self):
        if float(self.gpa) > 3.5:
            print(f"{self.name} is Honor")
        else:
            print(f"{self.name} is not Honor")



s1 = Student("Ali", 20, "Computer Science", 4, [("math", 86,), ("physics", 67)])


s1.introduce()
s1.show_gpa()
s1.courses()
s1.add_course("IT")
s1.update_gpa(3.8)
s1.is_honor()
s1.show_major()