use std::fs;
use std::collections::HashSet;

fn print_begin(chars :&Vec<char>, window_size :usize, part :usize) {
    for (i, window) in chars.windows(window_size).enumerate() {
        let hash_set :HashSet<char> = window.iter().cloned().collect();
        if hash_set.len() == window_size {
            println!("Part {}: {}", part, i + window_size);
            break;
        }
    }
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("puzzle input");
    let chars = contents.trim_end().chars().collect::<Vec<char>>();
    print_begin(&chars,  4, 1);
    print_begin(&chars, 14, 2);
}
