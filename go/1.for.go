package main

import "fmt"

func main() {
	a := 1

	//for simple versiyonu
	for a <= 11 {
		fmt.Println(a)
		a++
	}

	//for

	for j := 1; j <= 11; j++ {
		fmt.Println(j)
	}

	//
	for {
		fmt.Println("oldu mu şimdi ?")
		break
	}

	for n := 0; n <= 5; n++ {
		if n%2 == 0 {
			continue
		}
		fmt.Println(n)
	}

}
