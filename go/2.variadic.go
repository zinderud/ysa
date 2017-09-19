package main
// bir metoda değişken sayıda parametre gönderme
import "fmt"
func main() {
	fmt.Println(topla(2,34,5))
}

func topla(sayilar ...int) int  {
	total:=0
	for _,n:=range sayilar{
		total+=n

	}
	return total

}
