use std::fs;
const INPUT: &str = "input.txt";
const TO_FIND_1: &[char] = &['X', 'M', 'A', 'S'];
const TO_FIND_2: &[char] = &['M', 'A', 'S'];

const DIRECTIONS_DIAG: [(i32, i32); 4] = [
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1)
];
const DIRECTIONS_AX: [(i32, i32); 4] = [
    (0, 1),
    (0, -1),
    (-1, 0),
    (1, 0)
];


fn map_input(data: &str) -> Vec<Vec<char>> {
    data
        .lines()
        .into_iter()
        .map(|x| x.trim().chars().collect::<Vec<char>>())
        .collect()
}

fn search_string(table: &Vec<Vec<char>>, r:i32, c:i32, (dr, dc): (i32, i32), iter:usize) -> i32{
    if table[r as usize][c as usize] != TO_FIND_1[iter] { return 0; }
    if iter+1 >= TO_FIND_1.len(){return 1;}
    let (nr, nc): (i32, i32) = (r+dr, c+dc);
    if nr < 0 || nr >= table.len() as i32 || nc < 0 || nc >= table[0].len() as i32 { return 0;}
    return search_string(table, nr, nc, (dr, dc), iter+1)
}

fn search_x_string(table: &Vec<Vec<char>>, r:usize, c:usize) -> i32{
    if r < 1 || r >= table.len()-1 || c < 1 || c >= table[0].len()-1 { return 0;}
    if table[r][c] == TO_FIND_2[1] &&
        (table[r+1][c+1] == TO_FIND_2[0] && table[r-1][c-1] == TO_FIND_2[2] ||
        table[r+1][c+1] == TO_FIND_2[2] && table[r-1][c-1] == TO_FIND_2[0]) && 
        (table[r-1][c+1] == TO_FIND_2[0] && table[r+1][c-1] == TO_FIND_2[2] ||
        table[r-1][c+1] == TO_FIND_2[2] && table[r+1][c-1] == TO_FIND_2[0]){
            1
        }else{
            0
        }
}



fn part1(table: &Vec<Vec<char>>) -> i32{
    table.iter().enumerate().map(|(row, row_data)| {
        row_data.iter().enumerate().map(|(col, &_value)| {
            DIRECTIONS_DIAG.iter()
                .chain(DIRECTIONS_AX.iter())
                .map(|dir| search_string(&table, row as i32, col as i32, *dir, 0))
                .sum::<i32>()
        }).sum::<i32>()
    }).sum::<i32>()
}

fn part2(table: &Vec<Vec<char>>) -> i32{
    table.iter().enumerate().map(|(row, row_data)| {
        row_data.iter().enumerate().map(|(col, &_value)| {
            search_x_string(&table, row, col)
        }).sum::<i32>()
    }).sum::<i32>()
}

fn main() {
    let data = fs::read_to_string(INPUT).expect("Error opening the file");
    let data = map_input(&data);
    println!("part1: {}", part1(&data));
    println!("part2: {}", part2(&data));
}



#[cfg(test)]
mod test{
    use super::*;
    const TEST_DATA: &str = include_str!("../test.txt");

    #[test]
    fn part1_test(){
        assert_eq!(part1(&map_input(TEST_DATA)), 18);
    }
    
    #[test]
    fn part2_test(){
        assert_eq!(part2(&map_input(TEST_DATA)), 9);
    }
}