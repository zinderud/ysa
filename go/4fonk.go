package main
import ("fmt")
func main(){

	fmt.Println("fonk yaz")
	toplam:=Topla(2,3)
	fmt.Println(toplam)
}

func Topla(x int,y int) int{
	return x+y
}


//recursive fonk örneği
func Faktoriyel(sayi int) int{
	if sayii==0 || sayi==1{
		return 1
	} else {
		return sayi*Faktoriyel(sayi-1)
	}
}

func seriIstek (x,y float32)(topla,bol float32)
	Topla =x+y
	bol=x/y
	return topla,bol

//n sayida parametre gönderebiliriz
func toplama (sayilar ...int)int{
	toplam:=0


	for _,sayi:=range sayilar {
		toplam+=sayilar
	}
	return toplam
}