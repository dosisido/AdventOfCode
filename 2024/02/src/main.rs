const FILE: &str = "input.txt";
use std::fs;

fn is_ascending(vec: &Vec<i32>, max_jump: i32) -> bool {
    vec.windows(2).all(|w| w[0] < w[1] && (w[0]-w[1]).abs() <= max_jump)
}
fn is_descending(vec: &Vec<i32>, max_jump: i32) -> bool {
    vec.windows(2).all(|w| w[0] > w[1] && (w[0]-w[1]).abs() <= max_jump)
}

fn generate_subvectors(vec: Vec<i32>) -> Vec<Vec<i32>> {
    let mut result: Vec<Vec<i32>> = Vec::new();
    for i in 0..vec.len(){
        let mut v = vec.clone();
        v.remove(i);
        result.push(v);
    }
    result
}


fn main() {

    let file_buffer: String = fs::read_to_string(FILE)
        .expect("Error reading the file");

    
    let mut data: Vec<Vec<i32>> = Vec::new();
    for line in file_buffer.lines(){
        let v = Vec::from_iter(line.split_whitespace().map(|x: &str| x.parse::<i32>().unwrap()));
        data.push(v);
    }
    println!("Reading {} lines", data.len());


    let sum = 
        data.iter().filter(|x| is_ascending(x, 3)).count()+
        data.iter().filter(|x| is_descending(x, 3)).count();
    
    println!("part1: {}", sum);


    let sum = data.iter().filter(|row: &&Vec<i32>|{
        generate_subvectors((*row).clone()).iter().any(
            |x| is_ascending(x, 3) || is_descending(x, 3)
        )
    }).count();

    println!("part2: {}", sum);

}
