const FILE: &str = "input.txt";
use std::fs;


fn main() {

    let content = fs::read_to_string(FILE)
        .expect("Something went wrong reading the file");

    let mut vec1: Vec<i32> = Vec::new();
    let mut vec2: Vec<i32> = Vec::new();

    for line in content.lines(){
        let (num1, num2) = line.split_at(line.find(' ').unwrap());
        let num1 = num1.trim().parse::<i32>().unwrap();
        let num2= num2.trim().parse::<i32>().unwrap();
        vec1.push(num1);
        vec2.push(num2);
    }

    println!("{}, {}", vec1.len(), vec2.len());

    let mut sum = 0;
    vec1.sort();
    vec2.sort();

    for i in 0..vec1.len(){
        sum += (vec1[i] - vec2[i]).abs();
    }

    println!("part1: {}", sum);

    let mut prod = 0;
    for number in vec1{
        prod+= number * vec2.iter().filter(|&x| *x==number).count() as i32;
    }

    println!("part2: {}", prod);


}
