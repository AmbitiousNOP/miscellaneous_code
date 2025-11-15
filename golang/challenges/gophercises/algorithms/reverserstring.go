// create a func which takes in a string
// return the string reversed

package main

import "fmt"

func Reverse(word string) string {
	var list []string

	for _, char := range word {
		list = append(list, string(char))
	}

	var revStirng string
	for i := len(list); i != 0; i-- {
		revStirng = revStirng + (list[i-1])
	}
	return revStirng
}

func main() {
	fmt.Println(Reverse("cat"))
	fmt.Println(Reverse("racecar"))
}
