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

func map_demo() {
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
}

func defer_demo() int{
	defer fmt.Println("Called after defer_demo returned");
	return 1;
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

	array_demo();
	map_demo();

	v := defer_demo();
	fmt.Println("Returned from defer_demo", v);
}
