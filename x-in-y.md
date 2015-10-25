# X in Y programming language

### Comments

### Command line arguments

*C*

```
int main(int argc, char **argv) {
  int i;
  /* argv[] is an array containing each argument as a string.
  argv[0] is the program invocation name
  */
  for(i=0; i< argc; i++) {
    printf("%s\n", argv[i]);
  }
  
  return 0;
}

```

*Python*

```
import sys
# sys.argv is a list containing the command line arguments
# sys.argv[0] refers to the program invocation name

# Go over each argument and print it
for arg in sys.argv:
  print(arg)
```

*Golang*

```
package main

import (
	"fmt"
	"os"
)

func main() {

	/* os.Args is a slice, so we can use range to iterate over it
	   os.Args[0] is the name of the program invocation itself
	*/
	for _, arg := range os.Args {
		fmt.Println(arg)
	}
}

```

### Input

### Loops

### Output


### String concatenation

*Golang*

```
package main

import (
	"fmt"
	"strings"
)

func main() {
	str_arr := []string{"hello", "world"} /*https://gobyexample.com/slices*/
	fmt.Println(strings.Join(str_arr, " "))
}

```

### Version of the compiler/interpreter

*Golang*

```
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println(runtime.Version())
}
```

*Python*

```
>>> import sys
>>> sys.version
```
