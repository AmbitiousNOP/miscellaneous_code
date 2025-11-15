// take in a list of nums
// return the sum of the list

package main

import "fmt"

func Sum(numbers []int) int {
	var sum int
	for _, elem := range numbers {
		sum += elem
	}

	return sum
}

func main() {
	fmt.Println(Sum([]int{1, 2, 3}))
}
