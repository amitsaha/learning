extern crate wapc;
#[macro_use]
extern crate load_file;

use std::error::Error;
use wapc::WapcHost;
use wasmtime_provider::WasmtimeEngineProvider;

fn handle_callback(
  _binding: &str,
  _namespace: &str,
  operation: &str,
  _payload: &[u8],
) -> Result<Vec<u8>, Box<dyn Error + Send + Sync>> {
  if operation == "GetGreeting" {
    Ok(b"Ahoy There".to_vec())
  } else {
    Err("Unsupported host call!".into())
  }
}


pub fn main() -> Result<(), Box<dyn Error + Send + Sync>> {
  let module = load_bytes!("../../helloguest/target/wasm32-unknown-unknown/release/helloguest.wasm");
  let engine = WasmtimeEngineProvider::new(&module, None);
  let host = WapcHost::new(Box::new(engine), move |_id, bd, ns, op, payload| {
    handle_callback(bd, ns, op, payload)
    })?;

  let res = host.call("SayHello", b"Alice")?;
  let s = std::str::from_utf8(&res)?;
  println!("{}", s);
  assert_eq!(s, "Ahoy There, Alice!");
  Ok(())
}
