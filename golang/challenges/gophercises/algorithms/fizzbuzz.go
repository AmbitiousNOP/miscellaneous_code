// given a number N, print out all numbers from 1 to N
// but when a number is div by 3 print out "Fizz"
// when a number is div by 5 print out "Buzz"
// when a number is div by 3 AND 5 print out "Fizz Buzz"
// Example: FizzBuzz(3)
// Output: 1,2 Fizz

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func FizzBuzz(N int) string {
	var answer []string

	for i := 1; i <= N; i++ {
		if i%3 == 0 && i%5 == 0 {
			answer = append(answer, "Fizz Buzz")
		} else if i%5 == 0 {
			answer = append(answer, "Buzz")
		} else if i%3 == 0 {
			answer = append(answer, "Fizz ")
		} else {
			answer = append(answer, strconv.Itoa(i))
		}
	}
	return strings.Join(answer, ", ")
}

func main() {
	fmt.Println(FizzBuzz(15))
}
