use std::fs;
const FILE: &str = "input.txt";


fn parse_input_1(input: &str) -> Vec<i64>{
    let mut vec = Vec::new();
    let mut block = true;
    let mut block_index = 0;
    for car in input.trim().chars() {
        let digit = car.to_digit(10).unwrap();
        match block {
            true => {
                for _ in 0..digit{
                    vec.push(block_index);
                }
                block_index+=1;
            }
            false=> {
                for _ in 0..digit{
                    vec.push(-1);
                }
            }
        }
        block= !block;
    }
    vec
}

fn parse_input_2(input: &str) -> Vec<(i64, u64)>{
    let mut vec = Vec::new();
    let mut block = true;
    let mut block_index = 0;
    for car in input.trim().chars() {
        let digit = car.to_digit(10).unwrap() as u64;
        match block {
            true => {
                vec.push((block_index, digit));
                block_index+=1;
            }
            false=> {
                if digit != 0{
                    vec.push((-1, digit));
                }
            }
        }
        block= !block;
    }
    vec
}

fn part1(disk: Vec<i64>) -> usize{
    let mut disk = disk.clone();
    let mut free_block_index = disk.iter().position(|&x| x == -1).unwrap();
    let mut block_to_move_index = disk.iter().rposition(|&x| x != -1).unwrap();

    while free_block_index <= block_to_move_index{
        let val = disk[block_to_move_index];
        disk[free_block_index] = val;
        disk[block_to_move_index] = -1;
        while disk[free_block_index] != -1{
            free_block_index+=1;
        }
        while disk[block_to_move_index] == -1{
            block_to_move_index-=1;
        }
    }
    disk.iter().enumerate().filter(|(_i, &x)| x != -1).map(|(i, &x)| (i as i64) * x).sum::<i64>() as usize
}

fn part2(disk: Vec<(i64, u64)>) -> usize{
    let mut disk = disk.clone();
    let mut block_to_move_index = disk.iter().rposition(|(x, _)| *x != -1).unwrap();
    // println!("{:?}", disk);

    while block_to_move_index > 0{
        let block = disk[block_to_move_index];
        let pos = disk
            .iter()
            .enumerate()
            .filter(|(i, (x, size))| *x == -1 && *i < block_to_move_index && *size >= block.1)
            .min_by_key(|(i, _)| *i)
            .map(|(i, _)| i);

        if pos.is_none(){
            block_to_move_index-=1;
            while disk[block_to_move_index].0 == -1{
                block_to_move_index-=1;
            }
            continue;
        }
        let pos = pos.unwrap();

        // println!("pos: {:?}", pos);

        let remaining = disk[pos].1 - block.1;
        // println!("remaining: {:?}", remaining);
        disk[pos] = block;
        disk[block_to_move_index].0 = -1;
        if remaining != 0{
            disk.insert(pos+1, (-1, remaining));
        }

        let mut i = 0;
        while i < disk.len()-1{
            if disk[i].0 == disk[i+1].0  && disk[i+1].0 == -1{
                let size = disk[i].1 + disk[i+1].1;
                disk.remove(i);
                disk.remove(i);
                disk.insert(i, (-1, size));
                i-=1;
            }
            i+=1;
        }


        // println!("{:?}", disk);

        block_to_move_index-=1;
        while disk[block_to_move_index].0 > block.0{
            block_to_move_index-=1;
        }

        while disk[block_to_move_index].0 == -1{
            block_to_move_index-=1;
        }
        // println!("next block to move: {:?}", block_to_move_index);
    }

    // println!("{:?}", disk);

    disk
        .iter()
        .flat_map(|(x, size)| {
            let mut v = Vec::new();
            for _ in 0..*size{
                v.push(*x);
            }
            v.into_iter()
        })
        .enumerate()
        .filter(|(_i, x)| *x != -1).map(|(i, x)| (i as i64) * x).sum::<i64>() as usize
}


fn main() {
    let input = fs::read_to_string(FILE).expect("Error reading file");
    println!("Part 1: {}", part1(parse_input_1(&input)));
    println!("Part 2: {}", part2(parse_input_2(&input)));
}

#[cfg(test)]
mod tests {
    use super::*;
    const INPUT: &str = "2333133121414131402";

    #[test]
    fn part1_test() {
        assert_eq!(1928, part1(parse_input_1(INPUT)));
    }
    #[test]
    fn part2_test() {
        assert_eq!(2858, part2(parse_input_2(INPUT)));
    }
}