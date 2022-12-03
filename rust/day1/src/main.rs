use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("puzzle input");
    let mut data : Vec<i64>  = contents.split("\n\n")
                                   .map(|x| x.split("\n")
                                             .map(|y| y.parse::<i64>().unwrap())
                                             .sum::<i64>()
                                    )
                                   .collect();
    data.sort_by(|a, b| b.cmp(a));
    println!("{}", data.iter().max().unwrap());
    println!("{}", data.iter().take(3).sum::<i64>());
}
