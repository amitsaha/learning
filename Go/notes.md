Setup
=====
- Create the following directory structure:
  go/
  └── src
- Setup GOPATH=$HOME/work/go, and "go" executable in PATH
- Documentation: godoc --http=:6060

Language Features
=================

- Compiled, Garbage collected
- No semicolons
- Go's entry point has to be a function called main() in a package, main. Without
  one of these, the program will compile, but you cannot run the program.
- Packages are imported usnig "import" (for e.g. import ("fmt", "os")).
- If you import a package and not use it, it will not compile
- By default int variables are assigned 0, booleans false, strings ""
  * Example: var a int, var a=1; a:=1 
  * var := 1 (The := operator declares as well as assigns the value; it infers the type from the value itself)
- Can also assign multiple variables (Example, x, x_square := 3, "X squared")
- Printing: %s => string, %d => Integer (fmt.Printf)
- No unused variables allowed

*Functions*

- One string parameter, no return values: func log(message string) { }
- Two integer paramters, one return integer: func add(a int, b int) int {}
- A string parameter and return int, bool: func power(name string) (int, bool) {}

*Structures*

```
// Declare a structure
type Point struct {
	x float64
	y float64
}
```

```
// Structure function
func (p *Point) translate(distance float64){
	p.x += distance
	p.y += distance
}
```

- Skipped over: Composition, Constructors

*Arrays*

```

func array_demo() {
	/* Declare an array scores */
	var scores [4] int;
	/* initialize with values */
	scores1 := [4]int{100, 101, 102, 103};
	
	for index, _ := range scores {
		scores[index] = 10*index;
	}
	fmt.Printf("%d\n", scores[1]);

	for index, value := range scores1 {
		fmt.Printf("%d %d\n", index, value);
	}
}
```

``len()`` can be used to find the length of an array.

*Slices*

TODO

*Maps*

```
	/* Create a basic map with string key, integer value */
	lookup := make(map[string]int)
	lookup["red"] = 0;
	lookup["green"] = 1;
	lookup["blue"] = 2;	

	/*Check if a key exists*/
	value, exists := lookup["yellow"];
	if (exists) {
		fmt.Println(value);
	} else {
		fmt.Println("yellow does not exist in lookup");
	}

	/* Get the number of keys */
	fmt.Println("Number of keys:", len(lookup));

	/* Delete a key*/
	delete(lookup, "red");

	/* Iterate over lookup*/
	for k, v := range lookup {
		fmt.Println(k, v);
	}	

```

- How do I return a map? slice? array? from a function.


*Code Organization*

TBD

*Miscellaneous*

- Error handling: Return values.

- Use ``defer`` to defer code execution. The code is executed after a function
returns. For example, ``defer file.Close()``.

- ``go fmt`` to automatically format Go code

- Initialized If: if err := process(); err != nill .. The value is available
inside ``else if`` or ``else``.

- type switch: ``switch a.(type) ``

- Function types: Functions are first class type

*goroutines and channels*

TBD

*Unit testing*

- See ``fact/`` for example.


First code - Hello world
========================
```
package main

func main() {
     println("It's over 9000!")
}
```

Compile & run your code using "go run <file name>":

```
go run --work main.go
WORK=/tmp/go-build200918303
It's over 9000!
```

Compile and run separately:

```
$ go build main.go

$ ls
total 468
-rwxrwxr-x. 1 asaha asaha 474984 May  1 16:25 main
-rw-rw-r--. 1 asaha asaha     61 May  1 16:23 main.go

$ ./main
It's over 9000!
```

Second code - using packages from the standard library
======================================================

```
package main

import (
	"fmt"
        "os"
)

func main() {
	if len(os.Args) != 2 {
		os.Exit(1)
	}
        fmt.Println("Program name", os.Args[0])
	fmt.Println("It's over", os.Args[1])	
}
```

To compile and run:

``
$ go run main.go 9000
```

Examples:
```
$ go run main.go 9000
Program name /tmp/go-build734884651/command-line-arguments/_obj/exe/main
It's over 9000
```

```
$ go build main.go
$./main 9090
Program name ./main
It's over 9090
```

Third code - using packages from the standard library, use function, declare variables
======================================================================================

```
package main

import (
	"fmt"
        "os"
	"math"
)

func power(x float64, y float64) float64 {
	return math.Pow(x, y)
}
    
func main() {
	if len(os.Args) != 2 {
		os.Exit(1)
	}
	fmt.Println("Program name", os.Args[0])
	fmt.Println("It's over", os.Args[1])

	var x, y float64 = 10, 2
	fmt.Printf("%f ^ %f = %f", x, y, power(x, y))
}

```

Using structures, pointers, structure functions
===============================================

```
package main

import (
	"fmt"
        "os"
	"math"
)

// Declare a structure
type Point struct {
	x float64
	y float64
}

// Create a point (x, y)
func create_point(x float64, y float64) Point{
	p1 := Point{ x:x, y:y,}
	return p1
}

// Translate a point by distance in either direction
func translate_point_1(p Point, distance float64) {
	p.x += distance
	p.y += distance
}

func translate_point_2(p *Point, distance float64) {
	p.x += distance
	p.y += distance
}

// Structure function
func (p *Point) translate(distance float64){
	p.x += distance
	p.y += distance
}

func power(x float64, y float64) float64 {
	return math.Pow(x, y)
}
func main() {
	if len(os.Args) != 2 {
		os.Exit(1)
	}
	fmt.Println("Program name", os.Args[0])
	fmt.Println("It's over", os.Args[1])

	var x, y float64 = 10, 2
	fmt.Printf("%f ^ %f = %f\n", x, y, power(x, y))
	
	// Create a point "object"
	p1 := create_point(x, y)
	fmt.Printf("x=%f, y=%f\n", p1.x, p1.y)

	// Call by "value", the changes in translate_point()
	// are not reflected back here
	translate_point_1(p1, 4)
	fmt.Printf("Translated x=%f, Translated y=%f\n", p1.x, p1.y)

	translate_point_2(&p1, 4)
	fmt.Printf("Translated x=%f, Translated y=%f\n", p1.x, p1.y)

	// structure method
	p1.translate(4)
	fmt.Printf("Translated x=%f, Translated y=%f\n", p1.x, p1.y)
}

```

* Next improvements: take these numbers as input
* Accept x,y as command line arguments


References
==========

- [The Little Go Book]([http://openmymind.net/The-Little-Go-Book/)
- [Unit testing example]([http://www.binpress.com/tutorial/getting-started-with-go-and-test-driven-development/160])
- [defer, panic, recover](http://blog.golang.org/defer-panic-and-recover)
- More to come
