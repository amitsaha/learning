extern crate mio;
use mio::*;

struct WebSocketServer;

impl Handler for WebSocketServer {
    type Timeout = usize;
    type Message = ();
}

fn main() {
    let mut event_loop = EventLoop::new().unwrap();
    // Create a new instance of our handler struct:
    let mut handler = WebSocketServer;
    // ... and provide the event loop with a mutable reference to it:
    event_loop.run(&mut handler).unwrap();
}

