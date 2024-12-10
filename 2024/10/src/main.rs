use std::fs;
use std::collections::HashSet;
use std::collections::HashMap;
const FILE: &str = "input.txt";


fn parse_input(input: &str) -> Vec<Vec<usize>> {
    let v: Vec<Vec<usize>> = input
        .lines()
        .filter(|line| !line.is_empty())
        .map(|line| 
            line
                .trim()
                .chars()
                .map(|x| 
                    x.to_digit(10).unwrap() as usize
                ).collect()
        ).collect();
    v.iter().filter(|row| row.len()>0).cloned().collect()
}


fn rico(table: Vec<Vec<usize>>, r:usize, c:usize) -> HashSet<(usize, usize)> {
    let mut res = HashSet::new();
    for dir in vec![(1 as i32, 0 as i32), (0, 1), (-1, 0), (0, -1)] {
        let nr = r as i32 + dir.0;
        let nc = c as i32 + dir.1;
        if nr < 0 || nc < 0 || nr >= table.len() as i32 || nc >= table[0].len() as i32 {
            continue;
        }
        let nr = nr as usize;
        let nc = nc as usize;
        if table[nr][nc] != table[r][c]+1 {continue;}
        // println!("\tChecking ({}, {}) = {}", nr, nc, table[nr][nc]);
        if table[nr][nc] == 9 {
            res.insert((nr, nc));
            continue;
        }
        res.extend(&rico(table.clone(), nr, nc));
    }

    res
}

fn rico2(table: Vec<Vec<usize>>, r:usize, c:usize) -> HashMap<(usize, usize), i32> {
    let mut res = HashMap::new();
    for dir in vec![(1 as i32, 0 as i32), (0, 1), (-1, 0), (0, -1)] {
        let nr = r as i32 + dir.0;
        let nc = c as i32 + dir.1;
        if nr < 0 || nc < 0 || nr >= table.len() as i32 || nc >= table[0].len() as i32 {
            continue;
        }
        let nr = nr as usize;
        let nc = nc as usize;
        if table[nr][nc] != table[r][c]+1 {continue;}
        // println!("\tChecking ({}, {}) = {}", nr, nc, table[nr][nc]);
        if table[nr][nc] == 9 {
            res.insert((nr, nc), 1);
            continue;
        }
        for (key, val) in rico2(table.clone(), nr, nc).iter(){
            if res.contains_key(key){
                res.insert(*key, *val + res[key]);
            } else{
                res.insert(*key, *val);
            }
        }
    }

    res
}


fn part1(table: Vec<Vec<usize>>) -> usize{
    table.iter().enumerate().map(|(r, row)| {
        row.iter().enumerate()
            .filter(|(_c, el)| **el == 0)
            .map(|(c, _el)|{
                // println!("Zeros at ({}, {})", r, c);
                rico(table.clone(), r, c).len()
            }).sum::<usize>()
    }).sum::<usize>()
}

fn part2(table: Vec<Vec<usize>>) -> usize{
    table.iter().enumerate().map(|(r, row)| {
        row.iter().enumerate()
            .filter(|(_c, el)| **el == 0)
            .map(|(c, _el)|{
                // println!("Zeros at ({}, {})", r, c);
                rico2(table.clone(), r, c)
                .values()
                .sum::<i32>() as usize
            }).sum::<usize>()
    }).sum::<usize>()
}


fn main() {
    let input = fs::read_to_string(FILE).expect("Error reading file");
    println!("Part 1: {}", part1(parse_input(&input)));
    println!("Part 2: {}", part2(parse_input(&input)));
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = "
        89010123
        78121874
        87430965
        96549874
        45678903
        32019012
        01329801
        10456732
    ";

    #[test]
    fn part1_test() {
        assert_eq!(36, part1(parse_input(INPUT)));
    }
    #[test]
    fn part2_test() {
        assert_eq!(81, part2(parse_input(INPUT)));
    }
}