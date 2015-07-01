package main

import (
	"fmt"
	"os"
)

/* Copied from gobyexample.com*/
func check (e error) {
	if e!= nil {
		panic(e)
	}
}

func count_lines(s [] string) int64{
	count := int64(0)
	for i := 0; i < len(s); i++ {
		if s[i] == "\n" {
			count++
		}
	}

	return count
}
	
func tail(lines_to_read int64, fname string){
	/* find file size*/
	fi, err := os.Stat(fname)
	check(err)
	/* https://golang.org/pkg/os/#FileInfo*/
	fsize := fi.Size()
	/* Open the file*/
	f, err := os.Open(fname)
	check(err)

	/*Keep reading the file till lines_to_read has been read
          or the end of file has been reached */
	var num_bytes int64 = 2

	buffer := make([]string, 1)
	for {
		if (num_bytes > fsize) {
			break
		}
		c := make([]byte, 1)
		f.Seek(fsize-num_bytes, 0)
		_, err := f.Read(c)
		check(err)
		/* Append the byte read to the buffer, bytes_read
                   http://golang.org/ref/spec#Appending_and_copying_slices
                */
		// XXX: is this right?
		buffer = append(buffer, string(c))
		num_bytes ++
		lines_read := count_lines(buffer)
		if (lines_read >= lines_to_read) {
			break
		}		
	}
	fmt.Println(buffer)
}
func main() {
	tail(5, "tail.go")
}
