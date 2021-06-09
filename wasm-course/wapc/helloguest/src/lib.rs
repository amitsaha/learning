extern crate wapc_guest as guest;

use guest::prelude::*;

#[no_mangle]
pub extern "C" fn wapc_init() {
  register_function("SayHello", do_hello);
}

fn do_hello(msg: &[u8]) -> CallResult {
      let name = std::str::from_utf8(msg)?;
      let res =
      host_call("default",
                 "sample",
                 "GetGreeting",
                 &vec![])?;
      let greeting = std::str::from_utf8(&res)?;
      let output = format!("{}, {}!", greeting, name);

      Ok(output.as_bytes().to_vec())
}
