struct Student {
    name: String,
    grades: Vec<f32>,
}

impl Student {
    fn new(name: &str) -> Self {
        Student {
            name: name.to_string(),
            grades: Vec::new(),
        }
    }

    fn add_grade(&mut self, grade: f32) {
        self.grades.push(grade);
    }

    fn average(&self) -> f32 {
        let sum: f32 = self.grades.iter().sum();
        let count = self.grades.len();
        if count == 0 {
            0.0
        } else {
            sum / count as f32
        }
    }

    fn display(&self) {
        println!("Student: {}", self.name);
        println!("Grades: {:?}", self.grades);
        println!("Average: {:.2}\n", self.average());
    }
}

fn main() {
    let mut alice = Student::new("Alice");
    alice.add_grade(95.0);
    alice.add_grade(88.0);
    alice.add_grade(76.5);

    let mut bob = Student::new("Bob");
    bob.add_grade(82.0);
    bob.add_grade(91.5);

    let students = vec![alice, bob];

    for student in students {
        student.display();
    }
}
