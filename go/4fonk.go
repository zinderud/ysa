package main

import (
	"fmt"
)

func main() {

	fmt.Println("fonk yaz")
	toplam := Topla(2, 3)
	fmt.Println(toplam)
}

func Topla(x int, y int) int {
	return x + y
}

//recursive fonk örneği
func Faktoriyel(sayi int) int {
	if sayi == 0 || sayi == 1 {
		return 1
	} else {
		return sayi * Faktoriyel(sayi-1)
	}
}

func seriIstek(x, y float32) (toplamaIslemi, bol float32) {
	toplamaIslemi = x + y
	bol = x / y
	return toplamaIslemi, bol
}

//n sayida parametre gönderebiliriz
func toplama(sayilar ...int) int {
	toplam := 0

	for _, sayi := range sayilar {
		toplam += sayi
	}
	return toplam
}

