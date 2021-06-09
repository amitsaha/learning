cargo build --target wasm32-wasi
wasmtime --dir=. ./target/wasm32-wasi/debug/wordcounter.wasm ./Cargo.toml



