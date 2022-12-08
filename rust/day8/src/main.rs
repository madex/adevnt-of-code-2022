use std::fs;

fn mark_visible(m: &Vec<Vec<i64>>, v: &mut Vec<Vec<i64>>, pos: (i32, i32), vec: (i32, i32)) {
    let mut max_hight = -1;
    let mut p = pos.clone();
    for _ in 0..m.len() {
        let h = m[p.0 as usize][p.1 as usize];
        if h > max_hight {
            max_hight = h;
            v[p.0 as usize][p.1 as usize] = 1;
        }
        p.0 += vec.0;
        p.1 += vec.1;
    }
}

fn scenic_score(m: &Vec<Vec<i64>>, pos: (i32, i32), vec: (i32, i32)) -> i64 {
    let mut score = 0;
    let mut p = pos.clone();
    let height = m[p.0 as usize][p.1 as usize];
    let size = m.len() as i32;
    p.0 += vec.0;
    p.1 += vec.1;
    while p.0 >= 0 && p.0 < size && p.1 >= 0 && p.1 < size {
        let cur = m[p.0 as usize][p.1 as usize];
        score += 1;
        if cur >= height {
            break;
        }
        p.0 += vec.0;
        p.1 += vec.1;
    }
    score
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("puzzle input");
    let map = contents.trim_end().split('\n').map(|x| x.chars()
                                                       .map(|y| y as i64 - '0' as i64).collect())
                                                       .collect::<Vec<Vec<i64>>>();
    let mut vis = vec![vec![0_i64; map.len()]; map.len()];
    let size = map.len();
    for x in 0..size {
        for y in 0..size { 
            if x == 0 {
                mark_visible(&map, &mut vis, (x as i32, y as i32), (1, 0));
            } else if x == map.len() - 1 {
                mark_visible(&map, &mut vis, (x as i32, y as i32), (-1, 0));
            } else if y == 0 {
                mark_visible(&map, &mut vis, (x as i32, y as i32), (0, 1));
            } else if y == map.len() - 1 {
                mark_visible(&map, &mut vis, (x as i32, y as i32), (0, -1));
            }
        }
    }
    println!("Part 1: {}", vis.iter().map(|x| x.iter().sum::<i64>()).sum::<i64>());
    let mut max_tss = 0;
    for x in 1..map.len() as i32 - 1 {
        for y in 1..map.len() as i32 - 1 {
            let mut tss = 1_i64;
            for v in [(1, 0), (-1, 0), (0, 1), (0, -1)] {
                tss *= scenic_score(&map, (x, y), v);
            }
            if tss > max_tss {
                max_tss = tss;
            }
        }
    }
    println!("Part 2: {}", max_tss);
}
