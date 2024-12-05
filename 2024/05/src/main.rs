use std::fs;
const INPUT_FILE: &str = "input.txt";

type Rule = Vec<i32>;
type Rules = Vec<Rule>;
type Sequence = Vec<i32>;

fn parse_input(data: &str) -> (Rules, Vec<Sequence>){
    let data = data.replace("\r\n", "\n");
    let mut split = data.splitn(2, "\n\n");
    let rules_str = split.next().unwrap_or("");
    let input_str = split.next().unwrap_or("");
    
    let rules: Rules = rules_str
        .lines()
        .map(|line| line.trim().split('|').map(|x| x.trim().parse::<i32>().unwrap()).collect())
        .collect();

    let sequence: Vec<Vec<i32>> = input_str
        .lines()
        .map(|line| line.trim().split(',').map(|x| x.trim().parse::<i32>().unwrap()).collect())
        .collect();

    (rules, sequence)
}

fn one_rule_apply(rule: Rule, sequence: &Sequence) -> bool{
    let i1 = sequence.iter().position(|x| x == &rule[0]);
    let i2 = sequence.iter().position(|x| x == &rule[1]);
    match (i1, i2){
        (Some(i1), Some(i2)) => i1 < i2,
        _ => true
    }
}
fn all_rules_applys(rules: Rules, sequence: &Sequence) -> bool{
    rules.iter().all(|rule| one_rule_apply(rule.clone(), sequence))
}

fn update_to_apply_rules(rules: Rules, sequence: &Sequence) -> Sequence{
    let mut result: Sequence = Vec::new();
    for el in sequence.iter(){
        for i in 0..result.len()+1{
            let mut tmp = result.clone();
            tmp.insert(i, *el);
            if all_rules_applys(rules.clone(), &tmp){
                result = tmp;
                break;
            }
        }
    }
    // println!("{:?} -> {:?}", sequence, result);
    result
}


fn part1(data: &str) -> i32 {
    let (rules, sequences )= parse_input(data);
    
    sequences
        .iter()
        .filter(|&sequence| all_rules_applys(rules.clone(), sequence))
        .cloned()
        .map(|x| x[x.len()/2])
        .sum::<i32>()
}

fn part2(data: &str) -> i32 {
    let (rules, sequences )= parse_input(data);
    
    sequences
        .iter()
        .filter(|&sequence| !all_rules_applys(rules.clone(), sequence))
        .cloned()
        .map(|sequence| update_to_apply_rules(rules.clone(), &sequence))
        .map(|x| x[x.len()/2])
        .sum::<i32>()
}


fn main() {
    let data = fs::read_to_string(INPUT_FILE).expect("Error opening the file");
    println!("part1: {}", part1(&data));
    println!("part2: {}", part2(&data));
}




#[cfg(test)]
mod test {
    use super::*;
    const FILE_TEST: &str = include_str!("../test.txt");
    #[test]
    fn part1_test() {
        assert_eq!(part1(FILE_TEST), 143);
    }
    #[test]
    fn part2_test() {
        assert_eq!(part2(FILE_TEST), 123);
    }
}