package main

import( "fmt"
"math"
)
func main() {
	kelimeler:= []string{"ayşe","fatma","hayirye"}
	fmt.Println(kelimeler)
	fmt.Println(kelimeler[1])


	//slice tanımı
	var toplam []float64
	toplam=make([]float64 ,3,33)//3 eleman içerecek şekilde make olmasaydı hata
	fmt.Println("uzunluk =%d,kapasite =%d\n",len(toplam),cap(toplam))
	toplam=append(toplam, math.Pi)// Slice'in sonuna eleman ekledi
	fmt.Println(toplam)
	}
