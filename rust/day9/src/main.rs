use std::fs;
use std::collections::HashSet;
use std::collections::HashMap;

struct State {
    r: Vec<(i64, i64)>,
    visit: HashSet<(i64, i64)>
}

fn move_rope(l: &Vec<&str>, s: &mut State, d: &HashMap<&str, (i64, i64)>) {
    let vec = d[l[0]];
    for _ in 0..l[1].parse().unwrap() {
        s.r[0].0 += vec.0;
        s.r[0].1 += vec.1;
        for i in 0..s.r.len() - 1 {
            let d = (s.r[i].0 - s.r[i+1].0, s.r[i].1 - s.r[i+1].1);
            if d.0.abs() > 1  || d.1.abs() > 1 {
                s.r[i+1].0 = s.r[i].0 - if d.0.abs() > 1 {d.0 / 2} else {0};
                s.r[i+1].1 = s.r[i].1 - if d.1.abs() > 1 {d.1 / 2} else {0};    
            }
        }
        s.visit.insert(s.r[s.r.len() - 1]);
    }
}

fn main() {
    let dir: HashMap<&str, (i64, i64)> = HashMap::from([
        ("R", (1, 0)), ("L", (-1, 0)), ("U", (0, 1)), ("D", (0, -1))
    ]);
    let contents = fs::read_to_string("input.txt").expect("puzzle input");
    let mut part1 = State { r: vec![(0, 0), (0, 0)], visit: HashSet::new() };
    let mut part2 = State { r: (0..10).map(|_| (0, 0)).collect(), visit: HashSet::new() };
    for line in  contents.trim().split('\n') {
        let l: Vec<&str> = line.split(' ').collect();
        move_rope(&l, &mut part1, &dir);
        move_rope(&l, &mut part2, &dir);
    }
    println!("Part 1: {}", part1.visit.iter().count());
    println!("Part 2: {}", part2.visit.iter().count());
}
