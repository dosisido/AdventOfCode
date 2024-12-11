use cached::proc_macro::cached;
const INPUT: &str = "28591 78 0 3159881 4254 524155 598 1";

fn parse_input(input: &str) -> Vec<i64> {
    input
        .lines()
        .filter(|line| !line.is_empty())
        .flat_map(|line| {
            line.trim()
                .split_whitespace()
                .map(|x| x.parse::<i64>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect()
}

#[cached]
fn apply_rule(x: i64) -> Vec<i64> {
    if x == 0 {
        return vec![1];
    }
    let y = x.to_string().chars().collect::<Vec<_>>();
    if y.len() % 2 == 0 {
        let left = y.iter().take(y.len() / 2).collect::<String>().parse::<i64>().unwrap();
        let right = y.iter().skip(y.len() / 2).collect::<String>().parse::<i64>().unwrap();
        vec![left, right]
    } else {
        vec![x * 2024]
    }
}

fn impl1(data: Vec<i64>, rounds: usize) -> usize{
    let mut data = data.clone();
    for _iter in 0..rounds{
        // println!("Round: {}\r", iter);
        data = data
            .iter()
            .flat_map(|&x| apply_rule(x))
            .collect::<Vec<_>>()
    }

    data.len()
}


#[cached]
fn rico(el: i64, rounds: usize) -> usize{
    let next = apply_rule(el);
    if rounds == 1 {
        return next.len();
    }
    next.iter().map(|&x| rico(x, rounds - 1)).sum()
}

fn impl2(data: Vec<i64>, rounds: usize) -> usize{
    data.iter().map(|&x| rico(x, rounds)).sum()
}


fn main() {
    println!("Part 1: {}", impl1(parse_input(&INPUT), 25));
    println!("Part 2: {}", impl2(parse_input(&INPUT), 75));
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = "
        125 17
    ";

    #[test]
    fn parts_test() {
        assert_eq!(22, impl1(parse_input(INPUT), 6));
        assert_eq!(55312, impl1(parse_input(INPUT), 25));
        assert_eq!(22, impl2(parse_input(INPUT), 6));
        assert_eq!(55312, impl2(parse_input(INPUT), 25));
        assert_eq!(impl1(parse_input(INPUT), 30), impl2(parse_input(INPUT), 30))
    }
}