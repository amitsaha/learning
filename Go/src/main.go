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
