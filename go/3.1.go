package main

import (
	"encoding/json" //Basit json serileştirme için kullanacağımız paket
	"fmt"
	"reflect"
)

func main() {

	liste := [5]float32{
		2,
		3,
		4,
		51,
		1,
	}
	var toplam float32
	var eleman_sayisi = len(liste)
	fmt.Println(reflect.TypeOf(eleman_sayisi))
	for i := 0; i < eleman_sayisi; i++ {
		toplam += liste[i]
	}
	fmt.Println(toplam)

	var basarililar int = 0
	puanlar := [5]int{34, 55, 23, 90, 98}
	for _, puan := range puanlar {
		if puan >= 50 {
			basarililar++
		}
	}
	fmt.Printf("Başarılı %d öğrenci var\n", basarililar)

	// iki boyutlu bir dizi örneği. 3X2lik bir matris oluşturduk.
	matris := [3][2]int{{2, 3}, {6, 1}, {-9, 8}}
	for i := 0; i < 3; i++ {
		for j := 0; j < 2; j++ {
			fmt.Printf("%d\t", matris[i][j])
		}
		fmt.Println()
	}

	//Örnek bir slice tanımı. string elemanlardan oluşuyor
	soyadlari := []string{"sa", "de", "ce", "dere", "ken", "sa"}
	// indis değerlerini ele almadık. _ operatörü ile.
	// sadece value'ları işliyoruz. Yani string içerikleri
	for _, value := range soyadlari {
		fmt.Println(value)
	}
	fmt.Println()
	//alt_kume := soyadlari[3:6]
	alt_kume := soyadlari[6:]
	//: işareti ile bir diziden veya kesittten alt kesitler alabiliriz.
	// Baştan itibaren, sondan itibaren veya iki rakam arasındaki kısımlardan
	alt_kume = append(alt_kume, "hera") //append ile slice sonuna eleman eklenebilir
	alt_kume = append(alt_kume, "sizar")
	for _, value := range alt_kume {
		fmt.Println(value)
	}
	var iller []string
	iller = make([]string, 5, 10) //5 eleman içeren 10a kadar genişleyebilen kesit. Eleman sayısı ve başlangıç kapasitesini belirttik
	iller[0] = "istanbul"
	iller[1] = "izmir"
	iller[2] = "ankara"
	iller[3] = "bursa"
	iller[4] = "gaziantep"
	iller = append(iller, "trabzon")
	for i := 0; i < len(iller); i++ {
		fmt.Printf("%d:%s\n", i, iller[i])
	}
	for i, il := range iller {
		fmt.Printf("%d:%s\n", i, il)
	}

	// Basit bir map tanımlaması
	// key ve value içerikleri string tipten olacaklar
	sozluk := make(map[string]string)
	sozluk["white"] = "beyaz"
	sozluk["black"] = "siyah"
	sozluk["red"] = "kirmizi"
	sozluk["blue"] = "mavi"
	for key, value := range sozluk { //hem key hem de value değerlerini alıyoruz.
		fmt.Printf("[%s:%s]\n", key, value)
	}
	// sozluk map içeriğini json formatına dönüştürüyoruz ve ekrana basıyoruz
	jsonContent, _ := json.MarshalIndent(sozluk, "", "   ")
	fmt.Println(string(jsonContent))

	//Bu sefer key içerikleri string value içerikleri int olan
	//bir map değişkeni tanımlandı
	envanvter := map[string]int{
		"Laptop":       34,
		"Desktop":      5,
		"Tablet":       12,
		"Cep Telefonu": 34,
	}
	// Envanterdeki toplam cihaz sayısını buluyoruz.
	var toplam_cihaz int = 0
	for _, value := range envanvter {
		toplam_cihaz += value
	}
	fmt.Printf("Envanterde %d cihaz var\n", toplam_cihaz)
}
