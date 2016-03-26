use std::io;
use std::io::Write;
use std::fs::File;
use std::env;

fn main() {
    let mut stdout = io::stdout();
    // Process any additional files specified
    let args: Vec<String> = env::args().collect();
    let mut files = Vec::new();
    if args.len() > 1 {
        for file_name in args {
            match File::create(file_name) {
                Ok(f) => {
                    files.push(f);
                }
                Err(error) => {
                    println!("Error when creating file for writing: {}", error);
                }
            }
        }
    }
    // Read from standard input and write to all the files
    let mut line = String::new();
    loop {
        match io::stdin().read_line(&mut line) {
            Ok(n) => {
                // Have we read all the lines, if yes, break
                if n == 0 {
                    break;
                }
                // Write to standard out
                match stdout.write(line.as_bytes()) {
                    Ok(_) => {}
                    Err(error) => {
                        println!("Error writing to stdout: {}", error);
                    }
                }
                // Write to any additional files
                for f in &mut files{
                    match f.write(line.as_bytes()) {
                        Ok(_) => {}
                        Err(error) => {
                            println!("Error when writing to file: {}", error);
                        }
                    }
                }
                // Clear the line we just read so that we don't keep
                // appending
                line.clear();
            }
            Err(error) => {
                println!("Error reading from stdin : {}", error);
            }
        }
    }
}
