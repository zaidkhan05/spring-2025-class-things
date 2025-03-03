class Course:
    def __init__(self, name, number, section, term, year, num_students):
        self.name = name
        self.number = number
        self.section = section
        self.term = term
        self.year = year
        self.num_students = num_students

    def update_course(self, name=None, number=None, section=None, term=None, year=None, num_students=None):
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if section is not None:
            self.section = section
        if term is not None:
            self.term = term
        if year is not None:
            self.year = year
        if num_students is not None:
            self.num_students = num_students

    def display_course(self):
        print(f"Course Name: {self.name}")
        print(f"Course Number: {self.number}")
        print(f"Section: {self.section}")
        print(f"Term and Year: {self.term} {self.year}")
        print(f"Number of Students: {self.num_students}")
        print("-" * 30)


def main():
    courses = []
    
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        name = input("Enter course name: ")
        number = input("Enter course number: ")
        section = input("Enter section: ")
        term = input("Enter term (e.g., Fall, Spring): ")
        year = input("Enter year: ")
        num_students = int(input("Enter number of students: "))
        
        course = Course(name, number, section, term, year, num_students)
        
        change_attr = input("Do you want to modify any attribute? (yes/no): ").strip().lower()
        if change_attr == "yes":
            attr = input("Which attribute would you like to change? (name, number, section, term, year, num_students): ")
            value = input("Enter new value: ")
            if attr == "num_students":
                value = int(value)
            course.update_course(**{attr: value})
        
        courses.append(course)
    
    print("\nCourse Details:")
    for course in courses:
        course.display_course()


if __name__ == "__main__":
    main()
