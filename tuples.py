thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(thistuple[1])

print(thistuple[2:5])


#Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)



del thistuple
print(thistuple)