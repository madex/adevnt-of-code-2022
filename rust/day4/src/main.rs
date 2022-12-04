use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);
    let mut score1: i64 = 0;
    let mut score2: i64 = 0;
    for line in reader.lines() {
        let r : Vec<i64> = line.unwrap().split(&[',', '-'][..]).map(|x| x.parse().unwrap()).collect();
        if (r[0] <= r[2] && r[1] >= r[3]) || (r[2] <= r[0] && r[3] >= r[1]) {
            score1 += 1;
        }
        if (r[0] >= r[2] && r[0] <= r[3]) || (r[1] >= r[2] && r[1] <= r[3]) || 
           (r[2] >= r[0] && r[2] <= r[1]) || (r[3] >= r[0] && r[3] <= r[1]) {
            score2 += 1;
        }
    }
    println!("{}", score1); // 2
    println!("{}", score2); // 4
    Ok(())
}
