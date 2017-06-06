package main

import (
	"fmt"
	"math"
)

const s string = "sabit"

func main() {
	fmt.Println(s)
	const n = 400000
	const d = 3e232 / n
	fmt.Println(d)
	fmt.Println(math.Sin(n))

}
