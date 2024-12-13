use std::fs;
use regex::Regex;
const FILE: &str = "input.txt";
const MAX_ITER: i64 = 100;
const SCALING_FACTOR : i64 = 10000000000000;

const REGEX : &str = r#"Button A: X\+(?<AX>\d+), Y\+(?<AY>\d+)\s+Button B: X\+(?<BX>\d+), Y\+(?<BY>\d+)\s+Prize: X=(?<PX>\d+), Y=(?<PY>\d+)"#;

struct Machine {
    a: (i64, i64),
    b: (i64, i64),
    p: (i64, i64),
}
impl Machine {
    fn new(ax: i64, ay: i64, bx: i64, by: i64, px: i64, py: i64) -> Self {
        Self {
            a: (ax, ay),
            b: (bx, by),
            p: (px, py),
        }
    }
}

impl std::fmt::Debug for Machine {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "Machine {{ A: ({}, {}), B: ({}, {}), P: ({}, {}) }}",
            self.a.0, self.a.1, self.b.0, self.b.1, self.p.0, self.p.1
        )
    }
}

type Input = Vec<Machine>;

fn parse_input(input: &str) -> Input{
    Regex::new(REGEX).unwrap()
    .captures_iter(input)
    .map(|m| {
        Machine::new(
            m.name("AX").unwrap().as_str().parse::<i64>().unwrap(),
            m.name("AY").unwrap().as_str().parse::<i64>().unwrap(),
            m.name("BX").unwrap().as_str().parse::<i64>().unwrap(),
            m.name("BY").unwrap().as_str().parse::<i64>().unwrap(),
            m.name("PX").unwrap().as_str().parse::<i64>().unwrap(),
            m.name("PY").unwrap().as_str().parse::<i64>().unwrap(),
        )
    })
    .collect()
}

fn det(a:i64, b:i64, c:i64, d:i64) -> i64 {
    a as i64 * d as i64 - b as i64 * c as i64
}


fn run_machine(m: &Machine) -> i64 {
    let den = det(m.a.0, m.a.1, m.b.0, m.b.1);
    if den == 0 {
        return 0;
    }
    let a_coef: f64 = det(m.p.0, m.b.0, m.p.1, m.b.1) as f64 / den as f64;
    let b_coef: f64 = det(m.a.0, m.p.0, m.a.1, m.p.1) as f64 / den as f64;
    if a_coef > MAX_ITER as f64 || b_coef > MAX_ITER as f64 || a_coef < 0.0 || b_coef < 0.0 {
        return 0;
    }
    if a_coef.fract() != 0.0 || b_coef.fract() != 0.0 {
        return 0;
    }
    // println!("A: {:2},\tB: {:2}", a_coef, b_coef);
    3 * a_coef as i64 + 1 * b_coef as i64
}

fn run_machine_2(m: &Machine) -> i64 {
    let den = det(m.a.0, m.a.1, m.b.0, m.b.1);
    if den == 0 {
        return 0;
    }
    let a_coef: f64 = det(m.p.0 + SCALING_FACTOR, m.b.0, m.p.1 + SCALING_FACTOR, m.b.1) as f64 / den as f64;
    let b_coef: f64 = det(m.a.0, m.p.0 + SCALING_FACTOR, m.a.1, m.p.1 + SCALING_FACTOR) as f64 / den as f64;
    if a_coef < 0.0 || b_coef < 0.0 {
        return 0;
    }
    if a_coef.fract() != 0.0 || b_coef.fract() != 0.0 {
        return 0;
    }
    3 * a_coef as i64 + 1 * b_coef as i64
}

fn part1(data: Input) -> i64{
    data.iter().map(run_machine).sum()
}

fn part2(data: Input) -> i64{
    data.iter().map(run_machine_2).sum()
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
        Button A: X+94, Y+34
        Button B: X+22, Y+67
        Prize: X=8400, Y=5400

        Button A: X+26, Y+66
        Button B: X+67, Y+21
        Prize: X=12748, Y=12176

        Button A: X+17, Y+86
        Button B: X+84, Y+37
        Prize: X=7870, Y=6450

        Button A: X+69, Y+23
        Button B: X+27, Y+71
        Prize: X=18641, Y=10279
    ";

    #[test]
    fn part1_test() {
        assert_eq!(480, part1(parse_input(INPUT)));
    }
    #[test]
    fn part2_test() {
        assert_eq!(875318608908, part2(parse_input(INPUT)));
    }
}