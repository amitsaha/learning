#[no_mangle]
extern fn add(x: i32, y: i32) -> i32 {
    x.wrapping_add(y)
}

#[no_mangle]
extern fn sub(x: i32, y: i32) -> i32 {
    x.wrapping_sub(y)
}

#[no_mangle]
extern fn div(x: i32, y: i32) -> i32 {
    if y == 0 {
        return 0;
    }
    x.wrapping_div(y)
}

#[no_mangle]
extern fn mul(x: i32, y: i32) -> i32 {
    x.wrapping_mul(y)
}
