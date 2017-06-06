package main

import (
	"fmt"
	"reflect"
)

const (
	samsun = 55
	isim   = "ali"
)

func main() {
	fmt.Println("nerede\t", samsun, "adı\t", isim)
	var x, y int // değişken adı
	x = 3
	y = 3 + x
	fmt.Println("sayıların toplamı", x+y)

	var cap float32 = 1.2
	var alan = 3.14 * ((cap / 2) * (cap / 2))

	fmt.Println("alan", alan)
	fmt.Println(reflect.TypeOf(alan))
	c := Sekil{Alan: 22}

	fmt.Println(c.Hacim())

}

//go da struct tanımlaması aslında class yapısı
//yerine
type Sekil struct {
	Alan int
}

// funcsiyon tanımlarken o struct için önemli olan  func sonra (s Sekil) yazdığımız gibi belirtiyoruz
func (s Sekil) Hacim() int {

	return 2 * s.Alan

}
