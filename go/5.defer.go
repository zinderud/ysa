package main

import (
	"fmt"
)

func main() {
	fmt.Println("main başlangıcı")
	sonuc := dosya_sifrele("bilgiler.dat")
	fmt.Println(sonuc)
	fmt.Println("main bitişi")
	fmt.Println(dosyaAyristir("urunler.json"))
}
func dosya_sifrele(dosya string) bool {
	defer dosyaKapat(dosya) // sonra bu çalışır
	defer temizle()    // fonksiyondan çıkılırken önce bu
	fmt.Println("Şifreleme operasyonu yapılıyor")
	return true
}

func dosyaKapat(dosya string) {
	fmt.Println("dosya ya yazılıp kapatıldı")
 
}
func temizle() {
	fmt.Println("On bellek temizleniyor")
}
func dosyaAyristir(dosya string) string {
	defer func() {
		fmt.Printf("%s için gerekli kapatma operasyonları yapılacaktır\n", dosya)
	}()
	fmt.Println("Dosya açılıyor...")
	fmt.Println("Ayrıştırma işlemi yapılıyor")
	return "operasyon başarılı"
}

