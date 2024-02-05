animals = ["Zebra", "Carmel", "Ape"]
print(animals[0])
#start count at 0, reference each element with []
#print(animals[0])
#for animal in animals:
#     print (animal)
for i in animals:
    if(i == "Camel"):
        print("We're in the desert")

#Strings operate like lists
x = "Hello freshman, you all smell"
#print(x[0])
#y = x.upper()
#print(y)
words_list = x.split()
print(len(words_list))