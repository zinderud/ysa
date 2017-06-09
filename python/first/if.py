cars = ['audi', 'bmw', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
     print(car.title())


for c in cars:
    if c=="audi":
        print (c.title())

age1 = 12
age2 = 20

if (age1 > 10) and (age2 > 18):
    print("all ok")
else:
    print("Not ok")


if (age1 > 10) or (age2 > 18):
    print("all ok")
else:
    print("Not ok")


friends  = ["onur", "cemal", "ali", "ayse", "yasar"]
if "cemal" in friends:
    print("cemal is in the list")

if "kelali" not in friends:
    print("kelali is not in the list")


age = 19
if age >= 65:
    print("old guy")
elif age >= 40:
    print("middle age")
elif age >=20:
    print("prime")
else:
    print("child")


foods = []
if foods:
    print("list is not empty")
else :
    print("list is empty")