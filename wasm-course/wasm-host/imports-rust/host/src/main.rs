use std::io::Read;
use std::{error::Error, fs::File};

use wasm3::{CallContext, Environment};
use wasm3::Module;

fn main() -> Result<(), Box<dyn Error>> {

     let env = Environment::new()?;
     let rt = env.create_runtime(1024 * 60)?;

     let bytes = {
       let mut f =
      File::open(
 "../importer/target/wasm32-unknown-unknown/release/importer.wasm")?;

       let mut bytes = vec![];
       f.read_to_end(&mut bytes)?;
       bytes
     };

     let module = Module::parse(&env, &bytes)?;
     let mut module = rt.load_module(module)?;

     if let Err(_e) = module.link_closure(
        "utilities",
        "random",
        move |_ctx: &CallContext, ()| -> i32 {
           use rand::Rng;
           let mut rng = rand::thread_rng();

           rng.gen_range(0..=100)
         }) {
         return Err("Failed to link closure".into());
     }

     let addto = module.find_function::<i32, i32>("addto")?;

     println!("Result: {}", addto.call(10)?);

     Ok(())
}
