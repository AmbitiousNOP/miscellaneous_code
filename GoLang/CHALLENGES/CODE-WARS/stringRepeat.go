// given a string "value"
// return it repeated "repetitions" amount of times

package main

import (
	"fmt"
	"strings"
)

func RepeatStr(repetitions int, value string) string {
	return strings.Repeat(value, repetitions)

}

func NoImports(repetitions int, value string) (ans string) {
	for i := 0; i < repetitions; i++ {
		ans += value
	}
	return ans
}

func main() {
	fmt.Println(RepeatStr(4, "a"))
	fmt.Println(NoImports(4, "a"))
}
