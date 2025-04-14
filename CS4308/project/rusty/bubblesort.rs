fn bubble_sort(arr: &mut Vec<i32>) {
    let n = arr.len();
    for i in 0..n {
        for j in 0..n - i - 1 {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
            }
        }
        println!("Pass {}: {:?}", i + 1, arr);
    }
}

fn main() {
    let mut nums = vec![64, 34, 25, 12, 22, 11, 90];
    println!("Original array: {:?}", nums);
    bubble_sort(&mut nums);
    println!("Sorted array:   {:?}", nums);
}
