const INPUT : &str = "input.txt"; 
use std::fs;
use regex::{Regex, Captures};

const REGEX_STR_1: &str = r#"mul\((?<op1>\d{1,4}),(?<op2>\d{1,4})\)"#;
const REGEX_STR_2: &str= r#"mul\((?<op1>\d{1,4}),(?<op2>\d{1,4})\)|do\(\)|don't\(\)"#;
const REGEX_STR_2_1: &str = r#"(?<mul>mul)\((?<op1>\d{1,4}),(?<op2>\d{1,4})\)|(?<do>do\(\))|(?<dont>don't\(\))"#;


fn es1(file_data: &str) -> i32{
    Regex::new(REGEX_STR_1).unwrap()
        .captures_iter(&file_data)
        .map(|m| 
            (
                m.name("op1").unwrap().as_str().parse::<i32>().unwrap(),
                m.name("op2").unwrap().as_str().parse::<i32>().unwrap()
            )
        )
        .map(|(op1, op2)| op1*op2)
        .sum::<i32>()
}

fn es2(file_data: &str) -> i32{
    let re= Regex::new(REGEX_STR_2).unwrap();
    let data: Vec<&str> = re
        .find_iter(&file_data)
        .map(|x|x.as_str())
        .collect();
    let mut i=0;
    let mut do_= true;
    let re = Regex::new(REGEX_STR_1).unwrap();
    let mut result: i32 = 0;
    loop{
        if i==data.len(){
            break;
        }
        let el = data[i];
        if el.contains("do()"){
            do_ = true;
        }else if  el.contains("don't()"){
            do_ = false;
        }else{
            if do_{
                // println!("analizing: {}", el);
                result += re
                    .captures_iter(el)
                    .map(|m| 
                        (
                            m.name("op1").unwrap().as_str().parse::<i32>().unwrap(),
                            m.name("op2").unwrap().as_str().parse::<i32>().unwrap()
                        )
                    )
                    .map(|(op1, op2)| op1*op2)
                    .sum::<i32>();
            }
        }
        i+=1;
    }
    result
}

fn es2_1(file_data: &str) -> i32{
    Regex::new(REGEX_STR_2_1).unwrap()
    .captures_iter(&file_data)
    .scan(1, |to_do, el: Captures<'_>| {
        match el.name("mul") {
            Some(_) => {
                if *to_do == 0{
                    return Some(0);
                }
                Some(
                    el.name("op1").unwrap().as_str().parse::<i32>().unwrap() *
                    el.name("op2").unwrap().as_str().parse::<i32>().unwrap()
                )
            },
            None => {
                if let Some(_) = el.name("do") {
                    *to_do = 1;
                }
                if let Some(_) = el.name("dont") {
                    *to_do = 0;
                }
                Some(0)
            }
        }
    })
    .sum::<i32>()
}

fn main() {

    let file_data: String = fs::read_to_string(INPUT)
        .expect("Error opening the file");

    println!("point1 {}", es1(&file_data));
    println!("point2 {}", es2(&file_data));
    println!("point2_1 {}", es2_1(&file_data));

}



#[cfg(test)]
mod test{
    use super::*;
    const TEST_DATA: &str = include_str!(r#"..\test.txt"#);

    #[test]
    fn es1_test(){
        assert_eq!(es1(&TEST_DATA), 161);
    }

    #[test]
    fn es2_test(){
        assert_eq!(es2(&TEST_DATA), 48);
        assert_eq!(es2_1(&TEST_DATA), 48);
    }

}