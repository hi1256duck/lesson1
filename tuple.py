#to store a value in variable
x=10

x=(10,11,12,13)

#if you want to store something that never changes then you can use tuple


Address=(67,"Ohio roads", "Sigma town", "Skibiditoilet state","sigma67ohio","6767676767676767")
print(Address)

#unpack a tuple
houseNo,streetName,town,state,country,code= Address

print(houseNo)
print(country)
print(streetName)   

CoolTuple=["Anthony",27,"black",61,5,5,0,["roblox","1minecraft","fortnite"]]
print(CoolTuple)
name,age,colour,weight,height,game=CoolTuple
print(game)
print(game[5][0])

letters=["a","b","c","d","e"]
print(letters[0:3])