//https://doc.rust-lang.org/nightly/book/guessing-game.html

extern crate rand; //Comparison to use rand?
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Welcome to guess the number, Rust Edition!");

    let secret_number = rand::thread_rng().gen_range(1, 101); // Not sure how use rand::Rng and thread_rng() works together

    loop {

        println!("Please input your guess.");
        let mut guess = String::new();
        io::stdin().read_line(&mut guess)
            .ok()
            .expect("Failed to read line");
        let guess: u32 = guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
            }
        println!("You guessed {}", guess);
        match guess.cmp(&secret_number) {
            Ordering::Less    => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal   => {
                println!("You win!");
                break;
            }
        }
    }
}
