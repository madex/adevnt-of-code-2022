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
            test:     l.iter()
                .map(|x| x.strip_prefix("  Test: divisible by "))
                .filter(|y| y.is_some())
                .nth(0)
                .unwrap()
                .unwrap()
                .parse()
                .unwrap(),
            if_true:
                l.iter()
                    .map(|x| x.strip_prefix("    If true: throw to monkey "))
                    .filter(|y| y.is_some())
                    .nth(0)
                    .unwrap()
                    .unwrap()
                    .parse()
                    .unwrap(),
            if_false:
                l.iter()
                    .map(|x| x.strip_prefix("    If false: throw to monkey "))
                    .filter(|y| y.is_some())
                    .nth(0)
                    .unwrap()
                    .unwrap()
                    .parse()
                    .unwrap(),
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
        for i in 0..monkey.len() {
            while monkey[i].item.len() > 0 {
                monkey[i].insp += 1;
                let it = monkey[i].item.remove(0);
                let v = if monkey[i].op.is_some() {monkey[i].op.unwrap()} else {it};
                let r = if monkey[i].mul { it * v } else { it + v } / 3;
                let n = if (r % monkey[i].test) == 0 {monkey[i].if_true} else {monkey[i].if_false};
                monkey[n].item.push(r);
            }
        }
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
        for i in 0..monkey.len() {
            while monkey[i].item.len() > 0 {
                monkey[i].insp += 1;
                let it = monkey[i].item.remove(0);
                let v = if monkey[i].op.is_some() {monkey[i].op.unwrap()} else {it};
                let r = if monkey[i].mul { it * v } else { it + v };
                let n = if (r % monkey[i].test) == 0 {monkey[i].if_true} else {monkey[i].if_false};
                monkey[n].item.push(r % common_divisor);
            }
        }
    }
    insp = monkey.iter().map(|x| x.insp).collect();
    insp.sort_by(|a, b| b.cmp(a));
    println!("Part 2: {}", insp[0]*insp[1]); // 2713310158
}
