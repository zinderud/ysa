
guzel_kitaplar={"bilim kurgu":"vakif","felsefe":"zerdust","roman":"f.sarkaci"}
print(guzel_kitaplar)

print(guzel_kitaplar["roman"])

guzel_kitaplar["fizik"]="kaos"
print(guzel_kitaplar)


del guzel_kitaplar["fizik"]
print(guzel_kitaplar)


for key,value in guzel_kitaplar.items():
    print(key)
    print("---------------")
    print(value)

