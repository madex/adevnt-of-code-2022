use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn win(y: i64, o: i64) -> i64 {
    let w :Vec<i64> = vec![2, 0, 1];
    if y == o { // win
        3
    } else if y < 3 && w[y as usize] == o { // draw
        6
    } else {
        0
    }
}

fn opp(o: i64, result: i64) -> i64 {
    let w :Vec<i64> = vec![2, 0, 1];
    if result == 0 {
        w[o as usize] + 1 
    } else if result == 1 {
        3 + o + 1
    } else {
        (0..3).find(|x| w[*x as usize] == o).unwrap_or(0) + 7
    }
}

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);
    let mut score1: i64 = 0;
    let mut score2: i64 = 0;
    for line in reader.lines() {
        let o = line.as_ref().unwrap().as_bytes()[0] as i64 - 'A' as i64;
        let y = line.as_ref().unwrap().as_bytes()[2] as i64 - 'X' as i64;
        score1 += win(y, o) + y + 1;
        score2 += opp(o, y);
    }
    println!("{}", score1);
    println!("{}", score2);
    Ok(())
}
