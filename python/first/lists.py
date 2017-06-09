friends  = ["onur", "cemal", "ali", "ayse", "yasar"]
print(friends)
print(friends[0])
print(friends[-1])#last element


friends[0] = "cem"
print(friends)

friends.append("selma")
print(friends)

friends.insert(3, "YUsuf")
print(friends)

del friends[3]
print(friends)

last = friends.pop()
print(friends)
print(last)

first = friends.pop(0)
print(friends)
print(first)

friends.remove("ali")
print(friends)

friends.insert(0, "necati")
friends.sort()
print(friends)

friends.insert(0, "zehra")
print(sorted(friends))

friends.reverse() #reverse the order
print(friends)

print(len(friends))