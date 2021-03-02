X ={
    'Name': 'BISHAL',
    'age' :25,
    'Occupuation':'ENGG'
}
print (X)
list=[]

list.append("Mango")
list.append("orange")
print(list)
a=["Apple","Banana"]
list_set=list + a
print(list_set)
X["Phone"] = 123456
X["address"]='KolKata'
X["hobby"]='Cricket'
print
for i in X:
    print(f"{i}:-{X[i]}")

for j in list_set:
    print(j)
    #for v in j:
       # print(v)



print(f"{list.__len__()},{list_set.__len__()}")

