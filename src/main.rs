use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let word_list: Vec<String> = read_lines("dict.txt")
        .expect("Failed to read file")
        .filter_map(|line| line.ok())
        .map(|line| line.trim().to_lowercase())
        .filter(|line| !line.is_empty())
        .collect();

    // println!("{:?}", word_list);
    for word in word_list {
        println!("{}", word);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
