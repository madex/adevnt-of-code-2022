use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn get_prior(x :i64) -> i64 {
    if x >= 'a' as i64 {
        x - 'a' as i64 + 1
    } else {
        x - 'A' as i64 + 27
    }
}

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);
    let mut score1: i64 = 0;
    let mut score2: i64 = 0;
    let mut c :Vec<String> = vec![]; 
    for line in reader.lines() {
        let l = line.as_ref().unwrap();
        let (a, b) = l.split_at(l.len() / 2);
        for x in a.chars() {
            if b.contains(x) {
                score1 += get_prior(x as i64);
                break; 
            }
        }
        c.push(line.unwrap());
        if c.len() == 3 {
            for x in c[0].chars() {
                if c[1].contains(x) && c[2].contains(x) {
                    score2 += get_prior(x as i64);
                    break; 
                }
            }
            c.clear();
        }
    }
    println!("{}", score1); // 157
    println!("{}", score2); // 70
    Ok(())
}
