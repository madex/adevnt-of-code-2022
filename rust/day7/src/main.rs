use std::fs::File;
use std::io::{self, prelude::*, BufReader};
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(PartialEq)]
struct Dir {
    name:   &'a str,
    dir:    bool,
    size:   usize,
    parent: Option<Weak<RefCell<Dir>>>,
    sub:    Vec<Rc<RefCell<Dir>>>
}

impl Dir {
    pub fn insert(Self: &mut Rc<RefCell<Dir>>, name: & str, dir: bool, size: usize) {
        Self.sub.push(Dir { name: name, dir: dir, size: size, parent: Some(Rc::downgrade(self)), sub: vec![]});
    }
}

fn main() -> io::Result<()> {
    let file = File::open("test.txt")?;
    let reader = BufReader::new(file);
    let mut root: Dir = Dir { name: "/", dir: true, size: 0, parent: None, sub: vec![] };
    let mut cur: &Dir = &root;
    for line in reader.lines() {
        let l : Vec<&str> = line.as_ref().unwrap().split(' ').collect();
        if l[0] == "$" {
            if l[1] == "cd" {
                match l[2] {
                    "/"  => cur = &root,
                    ".." => cur = &*cur.parent.unwrap(),
                    x    => for a in &cur.sub {
                        if a.name == x {
                            cur = &a;
                            break;
                        }
                    },
                } 
            }
        }
        println!("{:?}", l);
    }
    Ok(())
}
