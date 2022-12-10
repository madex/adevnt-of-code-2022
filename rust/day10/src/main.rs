use std::fs;

struct State {
    x: i64,
    cycle: i64,
    signal: i64,
}

fn update_inc(s: &mut State) {
    s.cycle += 1;
    if (s.cycle - 20) % 40 == 0 {
        s.signal += s.cycle * s.x;  
    }
    let pos = (s.cycle - 1) % 40;
    print!("{}", if pos >= s.x - 1 && pos <= s.x + 1 {'#'} else {'.'});
    if pos == 39 {
        println!("");
    }
}

fn main() {
    let mut state = State { x: 1, cycle:0, signal: 0 };
    let contents = fs::read_to_string("input.txt").expect("puzzle input");
    for line in contents.split('\n') {
        let l :Vec<&str> = line.split(' ').collect();
        if l[0] == "noop" {
            update_inc(&mut state);
        } else if l[0] == "addx" {
            update_inc(&mut state);
            update_inc(&mut state);
            state.x += l[1].parse::<i64>().unwrap();
        }
    }
    println!("Part1 : {}", state.signal);
}
