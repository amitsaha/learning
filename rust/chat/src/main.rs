extern crate mio;

use std::net::SocketAddr;
use mio::*;
use mio::tcp::*;

struct WebSocketServer;

impl Handler for WebSocketServer {
    type Timeout = usize;
    type Message = ();
}

fn main() {
    let mut event_loop = EventLoop::new().unwrap();
    // Create a new instance of our handler struct:
    let mut handler = WebSocketServer;
    let address = "0.0.0.0:11000".parse::<SocketAddr>().unwrap();
    let server_socket = TcpListener::bind(&address).unwrap();
    event_loop.register(&server_socket,
                        Token(0),
                        EventSet::readable(),
                        PollOpt::edge()).unwrap();
    // ... and provide the event loop with a mutable reference to it:
    event_loop.run(&mut handler).unwrap();
}

