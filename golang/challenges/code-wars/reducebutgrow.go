// given a non-empty array of ints, return the result
// of multiplying the values together in order.

package main

func Grow(arr []int) int {
	var mult int
	mult = 1
	for _, s := range arr {
		mult = s * mult
	}
	return mult
}
