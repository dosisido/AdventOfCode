use std::fs;
const INPUT_FILE: &str = "input.txt";

#[derive(PartialEq)]
enum ExitStatus{
    EXITED = 0,
    LOOP = 1,
}

#[derive(Clone)]
struct Tile{
    _x: usize,
    _y: usize,
    visited: bool,
    obstacle: bool,
    visited_with: Option<(i32, i32)>,
}

impl Tile{
    fn new(x: usize, y: usize, obstacle: bool) -> Self{
        Self{
            _x: x,
            _y: y,
            visited: false,
            obstacle: obstacle,
            visited_with: None,
        }
    }
}
impl std::fmt::Debug for Tile {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "{}",
            if self.obstacle {
                '#'
            } else if self.visited {
                'X'
            } else {
                '.'
            }
        )
    }
}

fn parse_input(data: &str) -> (Vec<Vec<Tile>>, (usize, usize)){
    let mut result = Vec::new();
    let mut start = (0, 0);
    for (row, line) in data.lines().enumerate(){
        let mut row_v = Vec::new();
        for (col, c) in line.chars().enumerate(){
            match c{
                '#' => row_v.push(Tile::new(col, row, true)),
                '.' => row_v.push(Tile::new(col, row, false)),
                '^' => {
                    row_v.push(Tile::new(col, row, false));
                    if start != (0, 0){
                        panic!("Multiple starting points found");
                    }
                    start = (row, col);
                },
                _ => panic!("Invalid character in input"),
            }
        }
        result.push(row_v);
    }
    (result, start)
}

fn walk(table: &mut Vec<Vec<Tile>>, (mut r, mut c): (usize, usize), (mut dr, mut dc): (i32, i32)) -> ExitStatus{
    let mut i = 0;
    loop {
        i += 1;
        if i > 100000 {
            return ExitStatus::LOOP;
        }
        table[r][c].visited = true;
        if table[r][c].visited_with.is_some() && table[r][c].visited_with.unwrap() == (dr, dc) {
            return ExitStatus::LOOP;
        }
        table[r][c].visited_with = Some((dr, dc));
        let (next_r, next_c) = ((r as i32) + dr, (c as i32) + dc);
        if next_r >= table.len() as i32 || next_c >= table[0].len() as i32 || next_r < 0 || next_c < 0 {
            return ExitStatus::EXITED;
        }
        let (next_r, next_c) = (next_r as usize, next_c as usize);
        if table[next_r][next_c].obstacle {
            (dr, dc) = (dc, -dr);
        } else {
            r = next_r;
            c = next_c;
        }
    }
}

fn part1((table, (start_r, start_c)): (Vec<Vec<Tile>>, (usize, usize))) -> i32 {
    let mut table = table;
    walk(&mut table, (start_r, start_c), (-1, 0));
    table.iter().map(|row| row.iter().filter(|tile| tile.visited).count() as i32).sum()
}

fn part2((table, (start_r, start_c)): (Vec<Vec<Tile>>, (usize, usize))) -> i32 {
    let mut table = table;
    let cloned_table = table.clone();
    let n_tiles = table.iter().flat_map(|row| row.iter()).filter(|tile| !tile.obstacle).count();
    let ret = table
        .iter_mut()
        .flat_map(|row| row.iter_mut())
        .filter(|tile| !tile.obstacle)
        .enumerate()
        .map(|(index, tile)| {
            print!("{}%: {} of {}\r", ((index + 1) * 100 / n_tiles), index + 1, n_tiles);
            let mut cloned_table_for_walk = cloned_table.clone();
            let cloned_tile = &mut cloned_table_for_walk[tile._y][tile._x];
            cloned_tile.obstacle = true;
            let is_loop = walk(&mut cloned_table_for_walk, (start_r, start_c), (-1, 0)) == ExitStatus::LOOP;
            match is_loop {
                true => 1,
                false => 0,
            }
        })
        .sum();
    print!("                                                                 \r");
    ret
}


fn main() {
    let data = fs::read_to_string(INPUT_FILE).expect("Error opening the file");
    println!("part1: {}", part1(parse_input(&data)));
    println!("part2: {}", part2(parse_input(&data)));
}

#[cfg(test)]
mod test {
    use super::*;
    const FILE_TEST: &str = include_str!("../test.txt");
    #[test]
    fn part1_test() {
        assert_eq!(part1(parse_input(FILE_TEST)), 41);
    }
    #[test]
    fn part2_test() {
        assert_eq!(part2(parse_input(FILE_TEST)), 6);
    }
}