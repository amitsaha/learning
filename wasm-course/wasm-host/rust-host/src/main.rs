use std::io::Read;
use std::{error::Error, fs::File};

use wasm3::Environment;
use wasm3::Module;

fn main() -> Result<(), Box<dyn Error>> {
     let env = Environment::new()?;
     let rt = env.create_runtime(1024 * 60)?;
     let mut f = File::open("calc.wasm")?;
     let mut bytes = vec![];
     f.read_to_end(&mut bytes)?;
     let module = Module::parse(&env, &bytes)?;
     let module = rt.load_module(module)?;

     let add = module.find_function::<(i32, i32), i32>("add")?;
     let sub = module.find_function::<(i32, i32), i32>("sub")?;
     let mul = module.find_function::<(i32, i32), i32>("mul")?;
     let div = module.find_function::<(i32, i32), i32>("divide")?;

     println!("Adding 3 and 2: {}", add.call(3, 2)?);
     println!("Subtract 10 and 2: {}", sub.call(10, 2)?);
     println!("Multiply 3 and 2: {}", mul.call(3,2)?);
     println!("Divide 10 and 2: {}", div.call(10,2)?);

     Ok(())
}
