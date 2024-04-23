// write a func that takes in a list of nums and num
// returns true if num is in and false if it is not

package main

import "fmt"

func NumInList(list []int, num int) bool {

	for _, elem := range list {
		if elem == num {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(NumInList([]int{1, 2, 3}, 3))
	fmt.Println(NumInList([]int{1, 2, 3}, 5))
	fmt.Println(NumInList([]int{1, 2, 3, -5}, -5))
	fmt.Println(NumInList(nil, -5))
	fmt.Println(NumInList([]int{}, 10))
}
