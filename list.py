#variable can store a single value
name="Anthony"
name="Tanshi"
name="Spiderman"
print(name)
names=["Tanshi","Anthony","Spiderman"]
print(names)

#emoji
emoji="🔥"
print(emoji)

Emolist=[]
for i in range(5):
    Emolist.append("🔥")
print(Emolist)

row=int(input("Enter the number of rows: "))
col=int(input("Enter the number of columns: "))
box=[]#stores a 2d list
for i in range(row):
    rowlist=[]
    for t in range(col):
        rowlist.append("🔥")
    box.append(rowlist) 
for i in range(row)   :
    for a in range(col):
        print(box[i][a],end="")
    print()    


box=[]#stores a 2d list
for i in range(3):
    rowlist=[]
    for t in range(6):
        rowlist.append("🔥")
    box.append(rowlist) 
for i in range(3)   :
    for a in range(6):
        print(box[i][a],end="")
    print()        
