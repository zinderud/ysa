//3Array_Slice_Map.go
/*
arraylarda boyut sabit slicelarda dinamik
map tipleri key:value

range fonskiyonu ile bir dizi,kesit veya harita'yı for döngüsü ile kullanabiliriz
	_ ile istersek bir fonksiyondan dönen değeri kullanmayacağımızı ifade edebiliriz

*/

package main

import (
	"fmt"
)

func main() {

	var isimler [13]string //4 elemanlı dizi tanımladık
	isimler[3] = "kerim"
	isimler[2] = "aslı"
	isimler[1] = "leyla"
	fmt.Println(len(isimler)) //len dizi eleman sayısı

	for i := 0; i < len(isimler); i++ {
		if isimler[i] != "" {
			fmt.Println(isimler[i])
		}
	}
}
