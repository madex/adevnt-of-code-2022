use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn win(y: i64, o: i64) -> i64 {
    match (y) {
        o => 3,
        _ => 6,
    }
}

fn main() -> io::Result<()> {
    let file = File::open("test.txt")?;
    let reader = BufReader::new(file);
    let mut score1: i64 = 0;
    for line in reader.lines() {
        let o = line.as_ref().unwrap().as_bytes()[0] as i64 - 'A' as i64;
        let y = line.as_ref().unwrap().as_bytes()[2] as i64 - 'X' as i64;
        score1 += y + win(y, o) + 1;
    }
    println!("{}", score1);
    Ok(())
}
