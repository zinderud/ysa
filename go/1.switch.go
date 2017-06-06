package main

import (
	"fmt"
	"time"
)

func main() {
	i := 22
	fmt.Println("i nin degeri", i)

	switch i {
	case 1:
		fmt.Println("bir")
	case 2:
		fmt.Println("iki")
	default:
		fmt.Println("aralık dışı bir değer")
	}

	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("onikiden önce ")
	default:
		fmt.Println("onikiden sonra ")
	}
}
