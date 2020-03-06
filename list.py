
thislist = ["apple", "banana", "cherry","orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1]) #Print the last item of the list
print(thislist[2:5])#Return the third, fourth, and fifth item:

print(thislist[:4]) #This example returns the items from the beginning to "orange":

print(thislist[2:]) #This example returns the items from "cherry" and to the end:


#Change the item

thislist[1] = "blackcurrant"
print(thislist)

thislist.append("orange") #Add Items
print(thislist) 

thislist.insert(1, "orange") #Insert an item as the second position:
print(thislist)

thislist.remove("kiwi") #remove the item
print(thislist)




del thislist #keyword removes the specified index /  keyword can also delete the list completely
print(thislist)
