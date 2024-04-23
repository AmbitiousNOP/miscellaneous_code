// Create a function called Points
// Given an array of size 10 with the format "x:y" (x being team points / y being opp points)
// calculate the total number of team points (x) within the arr

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func Points(games []string) int {
	// for each loop in the arr
	var totalPoints int
	for _, s := range games {
		// setting the score to a variable and converting to int
		teamScore, err := strconv.ParseInt(s[0:strings.Index(s, ":")], 10, 0)
		oppScore, err := strconv.ParseInt(s[strings.Index(s, ":")+1:], 10, 0)

		if err != nil {
			fmt.Println("Erro during conversion")
			return 1
		} else if teamScore > oppScore {
			totalPoints = totalPoints + 3
		} else if teamScore == oppScore {
			totalPoints = totalPoints + 1
		}
	}
	//fmt.Println(totalPoints)
	return totalPoints
}

func main() {
	var season = []string{"1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"}

	Points(season)
}
