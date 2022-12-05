use std::fs;

fn main() {
    let contents = fs::read_to_string("input.txt").expect("puzzle input");
    let st :Vec<Vec<&str>> = contents.split("\n\n")
                                     .map(|x| x.split("\n")
                                               .collect::<Vec<&str>>())
                                     .collect();
    let mut stack1 :Vec<Vec<char>> = vec![];
    let mut stack2 :Vec<Vec<char>> = vec![]; 
    for l in st[0].iter().rev().skip(1) {
        let stacks = l.len() / 4 + 1;
        if stack1.len() == 0 {
            for _ in 0..stacks {
                stack1.push(vec![]);
                stack2.push(vec![]);
            }
        }
        for i in 0..stacks {
            let c = l.chars().nth(1 + 4*i).unwrap();
            if c != ' ' {
                stack1[i].push(c);
                stack2[i].push(c);
            }
        }
    }
    // do moves
    for x in st[1].iter() {
        let m :Vec<i64> = x.split(' ').skip(1).step_by(2).map(|x| x.parse().unwrap()).collect();
        let mut help : Vec<char> = vec![];
        let from  = m[1] as usize - 1;
        let to    = m[2] as usize - 1;
        for _ in 0..m[0] {
            let obj   = stack1[from].pop().unwrap();
            stack1[to].push(obj);
            help.push(stack2[from].pop().unwrap());
        }
        for _ in 0..m[0] {
            stack2[to].push(help.pop().unwrap());
        }
    }
    println!("Part 1 : {}", stack1.iter().map(|x| x.last().unwrap()).collect::<String>());
    println!("Part 2 : {}", stack2.iter().map(|x| x.last().unwrap()).collect::<String>());
}
