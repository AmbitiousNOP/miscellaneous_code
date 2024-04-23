// given an array of ints
// return the one that appears an odd num of times
// there will allways be one int that appears an off num of times

// loop through searching for each diff num
// drop the num after adding to a variable for count
// if count is odd program can quick
// dropping the nums after counting will make the array shorter each iter

package main

func FindOdd(seq []int) int {
	// creating a map which will serve a set data structure
	dict := make(map[int]int)
	// looping through seq and adding each elem to dict.
	// If there is all ready a value it will increase the value
	for _, num := range seq {
		dict[num] = dict[num] + 1
	}

	// loop through the dictionary for a value that is odd
	for key, count := range dict {
		if count%2 != 0 {
			return key
		}
	}
	return 1
}

func main() {
	//FindOdd([]int{1, 2, 3, 4, 5, 6, 7, 8})
	//fmt.Println(RemoveElems([]int{1, 2, 3, 1, 4}, 1))
	FindOdd([]int{20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5})
}
