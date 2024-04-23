// write a function that transforms an int to a string.

package main

import (
	"fmt"
	"strconv"
)

func NumberToString(n int) string {
	return strconv.Itoa(n)
}

func main() {
	fmt.Println(NumberToString(123))
}
