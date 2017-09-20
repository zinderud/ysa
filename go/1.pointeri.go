package main

import (
	"fmt"

)

func main()  {
	var point int=2
	fmt.Println(&point) //değişkenin adresi
	pnt:=&point
	fmt.Println(pnt,"bellek adresindeki sayi",*pnt)
	telefon:=urun{id:121,ad:"sade",fiyat:1234.2}
	fmt.Println(telefon.fiyat)
	indirim(&telefon,22)
	fmt.Println(telefon.fiyat)
}

func indirim(u *urun,value float32)  {
	u.fiyat-=value

}

type urun struct {
	id int
	ad string
	fiyat float32
}
//Dikkat edileceği üzere telefon
// değişkeninin fonksiyon çağrısı öncesindeki
// fiyatı, fonksiyon çağrısı sonrası değişmiştir.
// Bunun sebebi fonksiyonda bir Pointer tanımlamış olmamızdır.
// *urun ile tanımladığımız değişkene, &telefon ile telefon isimli
// değişkenin bellek adresini taşımız oluruz