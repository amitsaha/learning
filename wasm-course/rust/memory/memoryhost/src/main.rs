use std::io::Read;
use std::{error::Error, fs::File};

use wasm3::{Environment, Runtime};
use wasm3::Module;

fn main() -> Result<(), Box<dyn Error>> {
  let env = Environment::new()?;
  let rt = env.create_runtime(1024 * 60)?;
  let mut f =
    File::open(
"../memoryguest/target/wasm32-unknown-unknown/release/memoryguest.wasm"
      )?;
  let mut bytes = vec![];
  f.read_to_end(&mut bytes)?;
  let module = Module::parse(&env, &bytes)?;
  let module = rt.load_module(module)?;

  // Get the pointer (index) of the buffer
  let getptr = module.find_function::<(), i32>("get_buffer_ptr")?;
  let ptr = getptr.call()?;
  println!("{}", ptr);

  // Write the name to memory
  let name = b"Tester McTesto";
  write_bytes_to_memory(&rt, ptr, name);

  // tell the guest we set the name
  let set_name = module.find_function::<i32, i32>("set_name")?;
  let new_len = set_name.call(name.len() as i32)?;
  println!("New string length: {}", new_len);

  let new_bytes = get_vec_from_memory(&rt, ptr, new_len);
  let new_string = std::str::from_utf8(&new_bytes)?;
  println!("Response: {}", new_string);

  Ok(())
}

fn get_vec_from_memory(rt: &Runtime, ptr: i32, len: i32) -> Vec<u8> {let data = unsafe { &*rt.memory() };

  data[ptr as usize..][..len as usize].to_vec()
}

fn write_bytes_to_memory(rt: &Runtime, ptr: i32, slice: &[u8]) {
  unsafe {
   (&mut *rt.memory_mut())[ptr as usize..][..slice.len()].copy_from_slice(slice);
  };
}