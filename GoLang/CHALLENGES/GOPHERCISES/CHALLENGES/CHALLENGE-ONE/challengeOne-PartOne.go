// create a program that reads a csv file and then presents a question / answer via the CLI

package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
)

// had to manually enter "Question, Answer" at the top of the CSV
// cuz it does not take the 0th item as csv[0].
func ReadCSV() [][]string {
	//open the csv file
	f, err := os.Open("problems.csv")
	if err != nil {
		log.Fatal(err)
	}

	// close the file
	defer f.Close()

	// read csv values
	csvReader := csv.NewReader(f)
	data, err := csvReader.ReadAll()
	if err != nil {
		log.Fatal(err)
	}

	return data

}

type QuestionAnswer struct {
	Question string
	Answer   string
}

func CreateQnA(data [][]string) []QuestionAnswer {
	var QnAlist []QuestionAnswer
	for _, line := range data {
		var rec QuestionAnswer
		rec.Question = line[0]
		rec.Answer = line[1]
		QnAlist = append(QnAlist, rec)
	}
	return QnAlist
}

func RunQuiz(QnA []QuestionAnswer) string {
	return QnA[0].Question
}

func main() {
	data := ReadCSV()
	QnAlist := CreateQnA(data)

	for _, QnA := range QnAlist {
		fmt.Println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		fmt.Println("Question", QnA.Question)
		fmt.Print("Enter your Answer: ")
		var StudentAnswer string
		fmt.Scanln(&StudentAnswer)
		if StudentAnswer == QnA.Answer {
			fmt.Println("Correct!")
		} else {
			fmt.Println("Wrong. The Correct Answer was ", QnA.Answer)
		}
	}

}
