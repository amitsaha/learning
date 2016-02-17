// Example of calling out to libc's uname() function
// Thanks to panicbit & aatch on #rust-beginners

extern crate libc;
use std::ffi::CStr;
use std::{str, mem};
use std::os::raw::c_char;
use libc::{utsname, uname};

// Convert a C char[] to a String
// Ripped off from http://stackoverflow.com/a/24148033/59634
fn get_string(buf: *const c_char) -> String {
    let c_str;
    unsafe {
        c_str = CStr::from_ptr(buf);
    }
    let buf: &[u8] = c_str.to_bytes();
    let str_slice: &str = str::from_utf8(buf).unwrap();
    let str_buf: String = str_slice.to_owned();  // if necessary
    return str_buf;
}

fn main() {
    let mut utsname:utsname = unsafe { mem::zeroed() };
    let retcode;
    unsafe {
        retcode = uname(&mut utsname);
    }
    if retcode == 0 {
        println!("Sysname: {0}", get_string(&utsname.sysname[0]));
        println!("Nodename: {0}", get_string(&utsname.nodename[0]));
        println!("Release: {0}", get_string(&utsname.release[0]));
        println!("Version: {0}", get_string(&utsname.version[0]));
        println!("Machine: {0}", get_string(&utsname.machine[0]));
        println!("Domain name: {0}", get_string(&utsname.domainname[0]));
    } else {
        println!("Error!");
    }
}
