package fact

import (
	"testing"
)

func TestFactorial(t *testing.T) {
	expected_fact := make(map[int] int);
	expected_fact[-1] = -1;
	expected_fact[0] = 1;
	expected_fact[1] = 1;
	expected_fact[5] = 120;

	for k, v := range(expected_fact) {
		if actual_fact := Factorial(k); actual_fact != v {
			t.Fatalf("Expected factorial of %d as %d , Got %d", k, v, actual_fact); 
		}		
	}	
}
