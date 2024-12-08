use std::collections::HashMap;
use std::collections::HashSet;
use itertools::Itertools; // Import the Itertools trait
use std::fs;
const FILE: &str = "input.txt";


fn parse_input(input: &str) -> (HashMap<char, Vec<(usize, usize)>>, usize, usize) {
    let mut map = HashMap::new();
    let (mut size_r, mut size_c) = (0, 0);
    input.lines().enumerate().for_each(|(r, line)| {
        line.chars().enumerate().for_each(|(c, car)| {
            if car != '.' {
                map.entry(car).or_insert(Vec::new()).push((r, c));
            }
            size_c = c;
        });
        size_r = r;
    });
    (map, size_r, size_c)
}

fn part1((map, size_r, size_c): (HashMap<char, Vec<(usize, usize)>>, usize, usize)) -> usize{
    map.iter().fold(HashSet::new(), |mut set: HashSet<(usize, usize)>, (_key, value)| {
        value.iter().tuple_combinations()
            .for_each(|((r1, c1), (r2, c2)): (&(usize, usize), &(usize, usize))| {
                let (dx, dy): (i32, i32) = (*r2 as i32 - *r1 as i32, *c2 as i32 - *c1 as i32);
                let p1: (i32, i32) = (*r1 as i32 - dx, *c1 as i32 - dy);
                let p2: (i32, i32) = (*r2 as i32 + dx, *c2 as i32 + dy);

                // println!("{:?}, {:?} -> {:?}: {:?}", (r1,c1), (r2,c2),(dx, dy), (p1, p2));

                for p in (vec![p1, p2]).iter() {
                    if p.0 >= 0 && p.0 <= size_r as i32 && p.1 >= 0 && p.1 <= size_c as i32 {
                        set.insert((p.0 as usize, p.1 as usize));
                        // println!("{}: {:?}", _key, p);
                    }
                }
            });
        set
    })
    .len()
}

fn part2((map, size_r, size_c): (HashMap<char, Vec<(usize, usize)>>, usize, usize)) -> usize{
    map.iter().fold(HashSet::new(), |mut set: HashSet<(usize, usize)>, (_key, value)| {
        value.iter().tuple_combinations()
            .for_each(|((r1, c1), (r2, c2)): (&(usize, usize), &(usize, usize))| {
                let (dx, dy): (i32, i32) = (*r2 as i32 - *r1 as i32, *c2 as i32 - *c1 as i32);
                let mut vec: Vec<(i32, i32)> = Vec::new();

                let mut p = (*r1 as i32 - dx, *c1 as i32 - dy);
                while p.0 >= 0 && p.0 <= size_r as i32 && p.1 >= 0 && p.1 <= size_c as i32{
                    vec.push(p);
                    p = (p.0 - dx, p.1 - dy);
                }

                let mut p = (*r2 as i32 + dx, *c2 as i32 + dy);
                while p.0 >= 0 && p.0 <= size_r as i32 && p.1 >= 0 && p.1 <= size_c as i32{
                    vec.push(p);
                    p = (p.0 + dx, p.1 + dy);
                }
                vec.push((*r1 as i32, *c1 as i32));
                vec.push((*r2 as i32, *c2 as i32));
                // println!("{:?}, {:?} -> {:?}: {:?}", (r1,c1), (r2,c2),(dx, dy), vec);
                vec.iter().for_each(|p| {
                    set.insert((p.0 as usize, p.1 as usize));
                });
            });
        set
    })
    .len()
}


fn main() {
    let input = fs::read_to_string(FILE).expect("Error reading file");
    println!("Part 1: {}", part1(parse_input(&input)));
    println!("Part 2: {}", part2(parse_input(&input)));
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = include_str!("../test.txt");

    #[test]
    fn part1_test() {
        assert_eq!(14, part1(parse_input(INPUT)));
    }
    #[test]
    fn part2_test() {
        assert_eq!(34, part2(parse_input(INPUT)));
    }
}