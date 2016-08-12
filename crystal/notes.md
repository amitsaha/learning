install crystal from tarball: https://github.com/crystal-lang/crystal/releases

guest forward

crystal playground ./crystal play --host 0.0.0.0:8080


$ cat hello.cr 


puts "Hello World"



$ ~/work/crystal-0.18.7-1/bin/crystal run hello.cr 

Hello World

[vagrant@localhost crystal]$ ~/work/crystal-0.18.7-1/bin/crystal build hello.cr 

[vagrant@localhost crystal]$ ls

hello  hello.cr

[vagrant@localhost crystal]$ file hello

hello: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=71e4c3d260bb5e2b0eb78824133d6426e364419a, not stripped

[vagrant@localhost crystal]$ ldd ./hello

linux-vdso.so.1 (0x00007ffcd0bf3000)

libpcre.so.1 => /lib64/libpcre.so.1 (0x00007f62f8a44000)

libgc.so.1 => /lib64/libgc.so.1 (0x00007f62f86ea000)

libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f62f84cb000)

libevent-2.0.so.5 => /lib64/libevent-2.0.so.5 (0x00007f62f8282000)

librt.so.1 => /lib64/librt.so.1 (0x00007f62f807a000)

libdl.so.2 => /lib64/libdl.so.2 (0x00007f62f7e75000)

libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f62f7c5e000)

libc.so.6 => /lib64/libc.so.6 (0x00007f62f789d000)

/lib64/ld-linux-x86-64.so.2 (0x00005583a3323000)

libatomic_ops.so.1 => /lib64/libatomic_ops.so.1 (0x00007f62f7699000)



https://github.com/rhysd/vim-crystal

Strings are UTF-8 y default: https://crystal-lang.org/docs/syntax_and_semantics/literals/string.html



