use std::fs;
use std::cell::RefCell;
use std::rc::{Rc, Weak};

struct Dir<'a> {
    name:   &'a str,
    dir:    bool,
    size:   usize,
    parent: Option<Weak<RefCell<Dir<'a>>>>,
    sub:    Vec<Rc<RefCell<Dir<'a>>>>
}

fn search_size(dir: &Rc<RefCell<Dir>>, sizes: &mut Vec<i64>) -> i64 {
    let mut size = 0;
    for f in dir.borrow().sub.clone() {
        let dir = f.borrow().dir;
        if dir {
            size += search_size(&f, sizes);
        } else {
            size += f.borrow().size as i64
        }
    }
    sizes.push(size);
    size
}

fn main() {
    let contents = fs::read_to_string("input.txt").expect("puzzle input");
    let root: Rc<RefCell<Dir>> = Rc::new(RefCell::new(
        Dir { name: "/", dir: true, size: 0, parent: None, sub: vec![] }));
    let mut cur = root.clone();
    for line in contents.trim().split('\n') {
        let l : Vec<&str> = line.split(' ').collect();
        if l[0] == "$" {
            if l[1] == "cd" {
                match l[2] {
                    "/"  => {let help = root.clone(); cur = help;}
                    ".." => {let help = cur.borrow().parent.as_ref().unwrap()
                                           .upgrade().unwrap().clone(); cur = help;}
                    x    => {let help = cur.borrow().sub.iter().find(|n| n.borrow().name == x)
                                           .unwrap().clone(); cur = help}
                } 
            } else {
            }
        } else {
            if l[0] == "dir" {
                cur.borrow_mut().sub.push(Rc::new(RefCell::new(
                    Dir { name: l[1], dir: true, size: 0, parent: Some(Rc::downgrade(&cur)), sub: vec![]})));        
            } else {
                let size = l[0].parse().unwrap_or(0);
                cur.borrow_mut().sub.push(Rc::new(RefCell::new(
                    Dir { name: l[1], dir: false, size: size, parent: Some(Rc::downgrade(&cur)), sub: vec![]}))); 
            }
        }
    }
    let mut sizes: Vec<i64> = vec![];
    let total = search_size(&root, &mut sizes);
    println!("Part 1: {}", sizes.iter().filter(|x| **x < 100_000).sum::<i64>());
    sizes.sort();
    println!("Part 2: {}", sizes.iter().find(|x|70_000_000 - total + **x >= 30_000_000).unwrap());
}
