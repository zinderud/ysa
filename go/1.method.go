package main

import "fmt"

type kisi struct {
	id int
	isim string
	kilo int
}

func (k kisi) kisiyaz() string   {
	   fmt.Printf( 	"%d \t %s\t %d\t",k.id,k.isim,k.kilo)
	if k.id==1 {
		return "yazma"
	}
	   return "yaz"
}
func add() func(int) int {
	total:=0
	return func(i int) int {
		total+=i
		return total
	}

}
func main() {
kim:=kisi{id:1,isim:"ali",kilo:123}
kim.kisiyaz()
fmt.Println(kim.kisiyaz())


	var ssade=add()
    fmt.Println(ssade(2))
	fmt.Println(ssade(2))
	fmt.Println(ssade(2))

}
