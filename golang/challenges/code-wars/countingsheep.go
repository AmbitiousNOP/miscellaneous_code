// given an array of boolean values
// return the number of true

package main

import "fmt"

func CountSheeps(numbers []bool) int {
	var present int
	for _, i := range numbers {
		if i == true {
			present++
		}
	}
	return present
}

func main() {
	fmt.Println(CountSheeps([]bool{true, false, true}))
}
