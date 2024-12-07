use std::fs;
// use std::fs::File;
// use std::io::prelude::*;
// use std::io::LineWriter;
const FILE: &str = "input.txt";
const PRINT_OPERATIONS: bool = false;

fn parse_input(input: &str) -> Vec<(u64, Vec<u64>)>{
    input.lines().enumerate().map(|(_index, line)| {
        let replaced_line = line.replace("\r", "");
        let mut parts = replaced_line.split(": ");
        let test = parts.next().unwrap().parse::<u64>().unwrap();
        let range = parts.next().unwrap().split_whitespace().map(|x| x.parse().unwrap()).collect();
        (test, range)
    }).collect()
}

fn test_operation(test: u64, range: &Vec<u64>, acc: u64, index: usize) -> bool {
    if acc > test{
        return false;
    }
    if acc == test {
        return true;
    }

    if index == range.len() {
        return false;
    }
    test_operation(test, range, acc * range[index], index+1) ||
    test_operation(test, range, acc + range[index], index+1)
}

fn test_operation2(test: u64, range: &Vec<u64>, acc: u64, index: usize) -> bool {
    if acc > test{
        return false;
    }
    if index == range.len() {
        return acc == test;
    }

    if  test_operation2(test, range, acc * range[index], index+1){
        if PRINT_OPERATIONS {print!("* ");}
        return true;
    }
    if  test_operation2(test, range, acc + range[index], index+1){
        if PRINT_OPERATIONS {print!("+ ");}
        return true;
    }
    if  test_operation2(test, range, (acc.to_string() + &range[index].to_string()).parse::<u64>().unwrap(), index+1){
        if PRINT_OPERATIONS {print!("|| ");}
        return true;
    }
    return false;
}

fn part1(input: Vec<(u64, Vec<u64>)>) -> u64 {
    input
        .iter()
        .filter(|(test, range)| test_operation(*test, range, range[0], 1))
        .map(|(test, _)| test)
        .sum::<u64>()
}

fn part2(input: Vec<(u64, Vec<u64>)>) -> u64 {
    input
        .iter()
        .filter(|(test, range)| {if PRINT_OPERATIONS {println!();} test_operation2(*test, range, range[0], 1)})
        .map(|(test, _)| test)
        .sum::<u64>()
}

fn main() {
    let input = fs::read_to_string(FILE).expect("Error reading file");
    println!("Part 1: {}", part1(parse_input(&input)));
    println!("Part 2: {}", part2(parse_input(&input)));

    // let input = parse_input(&input);
    // let result: Vec<_> = input
    //     .iter()
    //     .filter(|(test, range)| test_operation2(*test, range, range[0], 1))
    //     .collect();

    // let file = File::create("output.txt").expect("Error creating file");
    // let mut file = LineWriter::new(file);

    // result.iter().for_each(|(test, range)| {
    //     file.write_all(format!("{}: {}\n", test, range.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" ")).as_bytes());
    // });
    
    // file.flush();
}


#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = include_str!("../test.txt");

    #[test]
    fn part1_test() {
        assert_eq!(3749, part1(parse_input(INPUT)));
    }
    #[test]
    fn part2_test() {
        assert_eq!(11387, part2(parse_input(INPUT)));
    }
}