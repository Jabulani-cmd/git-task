class Course:
    def __init__(self):
        self.course_id = "#12345"
    def contact_details(self):method_over
        print("Please contact us by visiting www.hyperiondev.com")
    def head_office_location(self):
        print("Cape Town")

class OOPCourse(Course):
    def __init__(self):
        super().__init__()
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
    def trainer_details(self):
        print(f"Course: {self.description}")
        print(f"Trainer: {self.trainer}")
    def show_course_id(self):
        print(f"Course ID: {self.course_id}")

course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()