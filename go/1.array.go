package main

import (
	"fmt"
)

func main() {
	var a [5]int
	fmt.Println("arr", a)

	 a[4] = 100
    fmt.Println("set:", a)
    fmt.Println("get:", a[4])
	
}
