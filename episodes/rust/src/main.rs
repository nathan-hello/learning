use std::env;

fn main() {
    // Define an array of strings
    let strings = ["apple", "banana", "orange", "grape", "kiwi"];

    // Get the command line argument
    let args: Vec<String> = env::args().collect();

    // Check if the user provided an argument
    if args.len() < 2 {
        println!("Usage: {} <index>", args[0]);
        return;
    }

    // Parse the argument as an index
    let index: usize = match args[1].parse() {
        Ok(n) => n,
        Err(e) => {
           println!("{}", e);
            return;
        }
    };

    // Check if the index is within bounds
    // if index >= strings.len() {
    //     println!("Index out of bounds.");
    //     return;
    // }

    // Print the selected string
    println!("{}", strings[index]);
}

