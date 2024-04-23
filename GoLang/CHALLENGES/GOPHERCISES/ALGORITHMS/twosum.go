// Given a list and a varibale sum
// find two nums in the list that equate to sum.
// Example: given ([1,2,3,4], 7) return (2,3)

package main

import "fmt"

func FindTwoSum(nums []int, sum int) (int, int) {
	// create a hash map?? key = num + num, value = sum
	// could also only check sum of two elems that are both less than sum
	// could sort list to start with lowest nums first.
	// loop through list
	for pOne, i := range nums {
		for pTwo, j := range nums {
			// add i, j together and checking if positon of j and i are not the same.
			if ((i + j) == sum) && (pOne != pTwo) {
				return i, j
			}

		}
	}
	return 0, 0
}

func main() {
	fmt.Println(FindTwoSum([]int{1, 2, 3, 4}, 7))               //(3, 4)
	fmt.Println(FindTwoSum([]int{10, 1, 12, 3, 7, 2, 2, 1}, 4)) //(1,3)
}
