struct Task {
    id: u32,
    title: String,
    complete: bool,
}

fn main() {
    let tasks = vec![
        Task { id: 1, title: "Learn Rust".to_string(), complete: false },
        Task { id: 2, title: "Write Program".to_string(), complete: true },
        Task { id: 3, title: "Debug Code".to_string(), complete: false },
    ];

    for task in tasks {
        let status = if task.complete { "Complete" } else { "Incomplete" };
        println!("Task {}: {} [{}]", task.id, task.title, status);
    }
}
