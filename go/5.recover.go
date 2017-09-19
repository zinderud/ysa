 
package main

import (
	"fmt"
)
func main(){
	defer func(){
		err:=recover()
		if err!=nil{
			fmt.printf("bir hata oluştu")
		}
	}
	fmt.Println("Uygulama başlıyor")
	sonuc := baglan("net.tcp://localhost:1023/services/data")
	fmt.Println(sonuc) //panic nedeniyle return sonuc çalışmayacağından sonuc boş dönecektir
	sayilar:=make([]int ,5)
	sayilar[7]=100
	fmt.printf("ana program sonu")
}
func baglan(conStr string) string {
	defer func() { 
		err := recover()  
		if err != nil {   
			fmt.Printf("  bağlantı hatası\n\tError:%s\n", err)  
		}
	}()

 
	fmt.Println("Bağlantı açılıyor")
	panic("Bağlantı yapılırken hata oluştu") //sembolik olarak bir hata fırlatıldı
	return "durum bilgisi"
}