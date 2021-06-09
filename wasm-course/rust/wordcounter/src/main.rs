use std::collections::BTreeMap;
use std::env;
use std::fs;
use std::io::BufRead;

fn process(input_fname: &str) ->
           Result<BTreeMap<String, usize>, String> {

   let input_file = fs::File::open(input_fname)
        .map_err(|err| format!("error opening input {}: {}",
                               input_fname, err))?;

   let mut counts: BTreeMap<String, usize> = BTreeMap::new();

   for line in std::io::BufReader::new(input_file).lines() {
      let line = line.expect("error parsing line!");

     for word in line.split_ascii_whitespace().map(str::to_lowercase)
     {
        let word = word.trim_matches(|c: char| !c.is_alphanumeric());
        *counts.entry(word.into()).or_insert(0) += 1;
     }
   }

   Ok(counts)
}

fn main() {
   let args: Vec<String> = env::args().collect();
   let program = args[0].clone();

   if args.len() < 2 {
      eprintln!("usage: {} <input_file>", program);
      return;
   }

   match process(&args[1]) {
      Ok(counts) => render_counts(&counts),
      Err(err) => eprintln!("{}", err),
   }
}

fn render_counts(counts: &BTreeMap<String, usize>) {
   for (word, count) in counts.iter() {
     println!("Word: {:?} Count: {}", word, count);
   }
}
