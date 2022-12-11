use std::fs;

#[derive(Debug)]
struct Monkey {
    item:     Vec<i64>,
    insp:     i64,
    mul:      bool,
    op:       Option<i64>,
    test:     i64,
    if_true:  usize,
    if_false: usize,
}

impl Monkey {
    fn init(str: &str) -> Self {
        let l: Vec<&str> = str.split('\n').collect();
        let ope: Vec<&str> = l.iter()
            .map(|x| x.strip_prefix("  Operation: new = old "))
            .filter(|y| y.is_some())
            .nth(0)
            .unwrap()
            .unwrap()
            .split(' ')
            .collect::<Vec<&str>>();
        Self {
            item:     l.iter()
                .map(|x| x.strip_prefix("  Starting items: "))
                .filter(|y| y.is_some())
                .nth(0)
                .unwrap()
                .unwrap()
                .split(", ")
                .map(|z| z.parse().unwrap())
                .collect(),
            insp:     0,
            mul:      ope[0] == "*",
            op:       if ope[1] == "old" {None} else {Some(ope[1].parse().unwrap())},
            test:
                l[3].split(' ').last().unwrap().parse().unwrap(),
            if_true:
                l[4].split(' ').last().unwrap().parse().unwrap(),
            if_false:
                l[5].split(' ').last().unwrap().parse().unwrap()
        }
    }
}

fn monk_round(m: &mut Vec<Monkey>, part1: bool, cd: i64) {
    for i in 0..m.len() {
        while m[i].item.len() > 0 {
            m[i].insp += 1;
            let it = m[i].item.remove(0);
            let v = if m[i].op.is_some() {m[i].op.unwrap()} else {it};
            let r = if m[i].mul { it * v } else { it + v };
            let n = if (r % m[i].test) == 0 {m[i].if_true} else {m[i].if_false};
            m[n].item.push(if part1 {r / 3} else {r % cd});
        }
    }
}

fn main() {
    //let mut state = State { x: 1, cycle:0, signal: 0 };
    let contents = fs::read_to_string("input.txt").expect("puzzle input");
    let mut monkey: Vec<Monkey> = contents
        .trim()
        .split("\n\n")
        .map(|x| Monkey::init(x))
        .collect();
    let common_divisor: i64 = monkey.iter().map(|x| x.test).product();
    for _ in 0..20 {
        monk_round(&mut monkey, true, common_divisor);
    }
    let mut insp: Vec<i64> = monkey.iter().map(|x| x.insp).collect();
    insp.sort_by(|a, b| b.cmp(a));
    println!("Part 1: {}", insp[0]*insp[1]); // 10605
    monkey = contents
        .trim()
        .split("\n\n")
        .map(|x| Monkey::init(x))
        .collect();
    for _ in 0..10_000 {
        monk_round(&mut monkey, false, common_divisor);
    }
    insp = monkey.iter().map(|x| x.insp).collect();
    insp.sort_by(|a, b| b.cmp(a));
    println!("Part 2: {}", insp[0]*insp[1]); // 2713310158
}
