use serde::{Deserialize, Serialize};
use serde_json;
use wapc_guest::prelude::*;
use wasmcloud_actor_core as actor;
use wasmcloud_actor_http_server as http;
use wasmcloud_actor_keyvalue as kv;

#[actor::init]
fn init() {
      http::Handlers::register_handle_request(handle_http_request);
}

fn handle_http_request(req: http::Request) -> HandlerResult<http::Response> {
      let tokens: Vec<&str> = req.path.split("/").collect();
      if !req.path.starts_with("/vault") {
      return Ok(http::Response::bad_request());
      }
      let player_id = tokens[tokens.len() - 1];

      match req.method.as_ref() {
      "GET" => get_balance(player_id),
      "PUT" => deposit(player_id, &req.body),
      "DELETE" => withdraw(player_id, &req.body),
      _ => Ok(http::Response::bad_request()),
      }
}

fn get_balance(player_id: &str) -> HandlerResult<http::Response> {let balance = kv::default().get(player_id.to_string())?;
     Ok(http::Response::json(
     &Transaction {
          gold: if balance.exists {
               balance.value.parse()?
          } else {
               0
          },
     },
     200,
     "OK",
     ))
}

fn deposit(player_id: &str, raw: &[u8]) -> HandlerResult<http::Response> {
     let tx: Transaction = serde_json::from_slice(raw)?;
     kv::default().add(player_id.to_string(), tx.gold as i32)?;
     Ok(http::Response::ok())
}

fn withdraw(player_id: &str, raw: &[u8]) -> HandlerResult<http::Response> {
     let tx: Transaction = serde_json::from_slice(raw)?;
     kv::default().add(player_id.to_string(), tx.gold as i32 * -1)?;
     Ok(http::Response::ok())
}

#[derive(Serialize, Deserialize, Debug, Clone)]
struct Transaction {
     pub gold: u32,
}
