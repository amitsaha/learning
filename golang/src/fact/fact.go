package fact

/* Return the factorial of an integer*/

func Factorial(n int) int {
	fact := 1;
	if (n < 0) {
		return -1;
	}
	if (n == 0) {
		return 1;
	}
	for i:=1; i<=n; i++ {
		fact = fact*i;
	}

	return fact;
}
