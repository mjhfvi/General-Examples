package main

import "fmt"

func main() {
	day := "Tuesday"

	switch day {
	case "Monday":
		fmt.Println("Today is Monday.")
	case "Tuesday":
		fmt.Println("Today is Tuesday.")
	case "Wednesday":
		fmt.Println("Today is Wednesday.")
	default:
		fmt.Println("Today is another day.")
	}
}
