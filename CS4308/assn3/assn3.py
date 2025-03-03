class Course:
    name = ""
    number = ""
    section = ""
    term = ""
    year = ""
    num_students = 0

    def __init__(self, name, number, section, term, year, num_students):
        self.name = name
        self.number = number
        self.section = section
        self.term = term
        self.year = year
        self.num_students = num_students

    def change_name(self, name):
        self.name = name

    def change_number(self, number):
        self.number = number

    def change_section(self, section):
        self.section = section

    def change_term(self, term):
        self.term = term

    def change_year(self, year):
        self.year = year

    def change_num_students(self, num_students):
        self.num_students = num_students

    def display(self):
        print(f"Name: {self.name}")
        print(f"Number: {self.number}")
        print(f"Section: {self.section}")
        print(f"Term: {self.term}")
        print(f"Year: {self.year}")
        print(f"Number of students: {self.num_students}")

def changeCourseInfo(course):
    loop = True
    while loop:
        print("1: change name")
        print("2: change number")
        print("3: change section")
        print("4: change term")
        print("5: change year")
        print("6: change number of students")
        print("7: exit")
        change_choice = input("Enter your choice: ")
        match change_choice:
            case "1":
                name = input("Enter the new name: ")
                course.change_name(name)
            case "2":
                number = input("Enter the new number: ")
                course.change_number(number)
            case "3":
                section = input("Enter the new section: ")
                course.change_section(section)
            case "4":
                term = input("Enter the new term: ")
                course.change_term(term)
            case "5":
                year = input("Enter the new year: ")
                course.change_year(year)
            case "6":
                num_students = int(input("Enter the new number of students: "))
                course.change_num_students(num_students)
            case "7":
                loop = False
            case _:
                print("Invalid choice")

def newCourse():
    name = input("Enter the course name: ")
    number = input("Enter the course number: ")
    section = input("Enter the section: ")
    term = input("Enter the term: ")
    year = input("Enter the year: ")
    num_students = int(input("Enter the number of students: "))

    course = Course(name, number, section, term, year, num_students)
    return course

def viewCourses(courses):
    for course in courses:
        print("course #" + str(courses.index(course)+1) + ":")
        course.display()

def main():
    courses = []

    #request data from input, show what we have and see if we want to make changes
    #UI
    loop = True
    while loop:
        print("1: view courses")
        print("2: add course")
        print("3: change course")
        print("4: exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                viewCourses(courses)
            case "2":
                course = newCourse()
                courses.append(course)
                course.display()

            case "3": 
                for course in courses:
                    print(courses.index(course), end=": ")
                    course.display()
                course_index = int(input("Enter the index of the course you want to change: "))
                course = courses[course_index]
                changeCourseInfo(course)
            case "4":
                loop = False
            case _:
                print("Invalid choice")
    
    print("\nCourse Details:")
    course.display()
if __name__ == "__main__":
    main()
    







# Develop a complete Python program. Include a Course class with the 
# following components (attributes): 
#  Course Name 
#  Course  number 
#  Section 
#  Term and year 
#  Number of students 
 
# This class must include several methods: to change the values of these 
# attributes, and to display their values. Separately, “main” must: 
 
# • Define an array of courses 
# • request the corresponding data from input and create a course object. 
# • invoke a method to change the value of one of its attributes of the object 
# • store the object in the array 
# • invoke a method that displays the value of each attribute of every course in 
# the array. 