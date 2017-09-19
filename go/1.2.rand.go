package main
import(
	"fmt"
	"math/rand"
	
)
func main(){
	fmt.Println("merhaba")
	fmt.Println(Rastgele(33))
}
func Rastgele(deger int64) int{
	rand.Seed(deger)
	var numara int
	numara=rand.Intn(199)
	return numara
}
