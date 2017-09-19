package main

import ("fmt"
      "time")

func main()  {
	fmt.Printf("merhaba bu gun %s\n\n",time.Now())
	//arrays incele
	var point=[]float32{ 10.45,88.22}
	for i:=0;i<len(point) ;i++  {
		fmt.Printf("%d indis  deger=%f \n\n",i,point[i])

	}
	var isimler=[]string{"ayşe","fatma","hayriye"}

	 for i:=0;i<len(isimler);i++{
	 	fmt.Printf("%s\n ",isimler[i])
	 }

	 var sayilar [33]int

	for j:=0;j<len(sayilar) ;j++  {
		sayilar[j]=j*j*j
		fmt.Printf("%d\t",sayilar[j])
	}
	var a,b,c,d,x,y int
	x=8
	y=2

	a,b,c,d=calc(x,y)
	fmt.Printf("%d+%d=%d\n",x,y,a)
	fmt.Printf("%d*%d=%d\n",x,y,b)
	fmt.Printf("%d/%d=%d\n",x,y,c)
	fmt.Printf("%d-%d=%d\n",x,y,d)
}
func calc(x,y int)(int,int,int,int)  {
	return x+y,x*y,x/y,x-y
}