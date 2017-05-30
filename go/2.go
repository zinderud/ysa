package main

import (
	"fmt"
)

func main() {
	topla := 10
	//go da sadece for var 
	for index := 0; index < 25; index++ {
		if index%3 == 0 {
			topla += index
		}
	}
	fmt.Println("3 ile bölünenlerin toplamı=", topla)

	// While döngüsünün GO dilinde for ile yapılışı
	i := 0
	topla = 0
	for i < 100 {
		i++
		if i%3 == 0 {
			topla += i
		}
	}
	fmt.Println("3 ile bölünebilenlerin toplamı", topla)

	var t5,t4,t3 int
	for i:=0; i<29; i++ {
		if i%3 == 0 {
			t3++
		} else if i%4 ==0 {
			t4++
		} else if i%5==0 {
			t5++
		}
	}
	 	fmt.Println("fd", t5,t4,t3)
	

	//switch case kullanımı
	not:=55
	switch  {
	case not>=0 && not <50:
		fmt.Println("kaldın")
	case not>=50 && not<70:
	    fmt.Println("c aldın")
	case not >=70 && not <=100:
	    fmt.Println("a aldın")
	default:
		fmt.Println("not gecerli aralıkda değil")

	}


	} 
